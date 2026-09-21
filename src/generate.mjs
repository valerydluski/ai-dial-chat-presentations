import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import pptxgen from 'pptxgenjs';import {makeSlide} from './layouts.mjs';import {T} from './theme.mjs';
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const m=JSON.parse(fs.readFileSync('manifest.json','utf8'));const requested=process.argv[2];const selected=m.decks.filter(d=>!requested||d.id===requested||d.path.split('/').pop()===requested);
if(!selected.length)throw new Error(`No presentation matches ${requested}`);
for(const entry of selected){
 if(!entry.content){console.log('Pending content:',entry.id);continue;}
 if(fs.existsSync(entry.output)&&(!entry.outputSha256||hash(entry.output)!==entry.outputSha256)){console.error('Protected manual/untracked output:',entry.output);entry.status='protected-manual-edit';continue;}
 const inputs=[entry.content,'src/generate.mjs','src/layouts.mjs','src/theme.mjs','assets/favicon.png', ...JSON.parse(fs.readFileSync(entry.content,'utf8')).slides.filter(s=>s.image).map(s=>s.image)];
 const fingerprint=crypto.createHash('sha256').update(inputs.map(hash).join('')).digest('hex');
 if(fs.existsSync(entry.output)&&entry.generationFingerprint===fingerprint){console.log('Up to date:',entry.id);continue;}
 const deck=JSON.parse(fs.readFileSync(entry.content,'utf8'));const pres=new pptxgen();pres.layout='LAYOUT_WIDE';pres.author='AI DIAL technical knowledge sharing';pres.subject=entry.purpose;pres.title=deck.shortTitle;pres.company='AI DIAL';pres.lang='en-US';pres.theme={headFontFace:T.font,bodyFontFace:T.font,lang:'en-US'};pres.revision='1';
 const geometry=deck.slides.map((s,i)=>makeSlide(pres,deck,s,i));fs.mkdirSync(path.dirname(entry.output),{recursive:true});await pres.writeFile({fileName:entry.output,compression:true});
 entry.generationFingerprint=fingerprint;entry.outputSha256=hash(entry.output);entry.contentSha256=hash(entry.content);entry.slideCount=deck.slides.length;entry.status='generated';entry.generatedAt=new Date().toISOString();
 fs.mkdirSync('qa/geometry',{recursive:true});fs.writeFileSync(`qa/geometry/${entry.id.replaceAll('/','-')}.json`,JSON.stringify(geometry,null,2));
 fs.writeFileSync('manifest.json',JSON.stringify(m,null,2)+'\n');console.log(entry.id,entry.slideCount,entry.output);
}

fs.writeFileSync("manifest.json",JSON.stringify(m,null,2)+"\n");
