import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const root=path.resolve(process.env.DIAL_REPO || '../ai-dial-chat');
const require=createRequire(path.join(root,'package.json'));
const ts=require('typescript');
const manifest=JSON.parse(fs.readFileSync('manifest.json','utf8'));
const base=ts.readConfigFile(path.join(root,'tsconfig.base.json'),ts.sys.readFile).config;
const opts=ts.convertCompilerOptionsFromJson({...base.compilerOptions,noEmit:true,emitDeclarationOnly:false,composite:false,incremental:false,jsx:'react-jsx',module:'esnext',moduleResolution:'bundler',lib:['es2022','dom','dom.iterable'],types:[],skipLibCheck:true},root).options;
const dossiers=manifest.decks.filter(x=>x.id!=='overview').map(x=>JSON.parse(fs.readFileSync(`content/research/${x.path.split('/')[1]}.json`,'utf8')));
const roots=dossiers.flatMap(d=>Object.keys(d.exports)).map(x=>path.join(root,x));
const program=ts.createProgram(roots,opts);const checker=program.getTypeChecker();
for(const d of dossiers){
 const all={};
 for(const entry of Object.keys(d.exports)){
  const sf=program.getSourceFile(path.join(root,entry));if(!sf)continue;
  const mod=checker.getSymbolAtLocation(sf);if(!mod)continue;
  all[entry]=checker.getExportsOfModule(mod).map(exp=>{
   let sym=exp;if(sym.flags&ts.SymbolFlags.Alias){try{sym=checker.getAliasedSymbol(sym)}catch{}}
   const decl=sym.getDeclarations()?.[0];if(!decl)return {name:exp.name};
   const sf=decl.getSourceFile();const file=path.relative(root,sf.fileName);const start=sf.getLineAndCharacterOfPosition(decl.getStart()).line+1;const end=sf.getLineAndCharacterOfPosition(decl.getEnd()).line+1;
   const type=checker.getTypeOfSymbolAtLocation(sym,decl);const sig=type.getCallSignatures()?.[0];let props=[];
   if(sig?.parameters.length){const first=sig.parameters[0];const t=checker.getTypeOfSymbolAtLocation(first,decl);props=t.getProperties().map(p=>({name:p.name,optional:!!(p.flags&ts.SymbolFlags.Optional),type:checker.typeToString(checker.getTypeOfSymbolAtLocation(p,decl),decl,ts.TypeFormatFlags.NoTruncation)}));}
   return {name:exp.name,file,start,end,declaration:decl.getText(),signature:sig?checker.signatureToString(sig,decl,ts.TypeFormatFlags.NoTruncation):null,props};
  });
 }
 d.contracts=all;
 d.implementationEvidence=Object.values(all).flat().filter(x=>x.file?.startsWith(d.project.path+'/')&&x.signature).slice(0,10);
 d.testEvidence=d.tests.filter(x=>/\.(spec|test)\.[cm]?[jt]sx?$/.test(x)).map(file=>({file,assertions:[...fs.readFileSync(path.join(root,file),'utf8').matchAll(/(?:it|test|describe)\s*\(\s*['"`]([^'"`]+)/g)].slice(0,15).map(m=>m[1])}));
 d.consumerEvidence=d.consumers.filter(x=>!x.includes('.spec.')).slice(0,8).map(file=>{const lines=fs.readFileSync(path.join(root,file),'utf8').split('\n');const matches=[];lines.forEach((s,i)=>{if(s.includes(d.project.package))matches.push({start:Math.max(1,i-8),end:i+2,excerpt:lines.slice(Math.max(0,i-9),i+2).join('\n')})});return {file,matches};});
 fs.writeFileSync(`content/research/${d.project.path.split('/')[1]}.json`,JSON.stringify(d,null,2)+'\n');
 console.log(d.project.id,Object.values(all).reduce((s,a)=>s+a.length,0),'export records');
}
