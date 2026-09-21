import {T} from './theme.mjs';
export function makeSlide(pres,deck,s,index){
 const slide=pres.addSlide();slide.background={color:T.bg};const geo=[];
 function text(t,x,y,w,h,size=24,extra={}){slide.addText(t,{x,y,w,h,fontFace:T.font,fontSize:size,color:T.text,margin:0,breakLine:false,valign:'top',paraSpaceAfterPt:8,...extra});geo.push({type:'text',text:t,x,y,w,h,font:size,...extra});}
 function box(x,y,w,h,fill=T.panel){slide.addShape(pres.ShapeType.roundRect,{x,y,w,h,rectRadius:0.12,radius:0.12,line:{color:T.edge,width:0.7},fill:{color:fill},radius:0.1});}
 function arrow(x,y,w){slide.addShape(pres.ShapeType.line,{x,y,w,h:0,line:{color:T.accent,width:1.7,beginArrowType:'none',endArrowType:'triangle'}});}
 slide.addImage({path:'assets/favicon.png',x:12.30,y:0.42,w:0.42,h:0.42});
 text('AI DIAL  /  '+deck.series.toUpperCase(),0.60,0.45,11.25,0.22,11,{color:T.muted,charSpacing:1.4});
 text(deck.shortTitle,0.60,7.00,8.5,0.20,10,{color:T.muted});
 text(s.id,9.0,7.0,3.0,0.2,9,{color:T.muted,align:'right'});
 text(String(index+1).padStart(2,'0'),12.30,6.98,0.42,0.25,12,{color:T.accent,align:'right'});
 if(s.layout==='cover'){
  text(s.title,0.65,1.65,11.7,1.50,48,{bold:true});
  text(s.subtitle,0.68,3.44,11.3,1.15,28,{color:T.accent});
  const chips=s.chips||['Architecture','Contracts','Integration'];chips.forEach((c,i)=>{box(0.68+i*4.1,5.20,3.8,0.70);text(c,0.90+i*4.1,5.42,3.35,0.24,16)});
  text(s.caption||'Technical knowledge sharing · source-verified workspace snapshot',0.68,6.22,11.6,0.32,14,{color:T.muted});
 }else{
  text(s.title,0.6,1.03,12.0,1.10,36,{bold:true});
  if(s.kicker)text(s.kicker,0.63,2.08,12.0,0.5,17,{color:T.accent});
  if(s.layout==='code'){
   box(0.60,2.85,12.1,3.62);text(s.code,0.86,3.06,11.55,3.20,18,{fontFace:T.code,breakLine:false,paraSpaceAfterPt:0,lineSpacingMultiple:1.04,color:T.text});
   if(s.caption)text(s.caption,0.65,6.58,11.9,0.24,12,{color:T.muted});
  }else if(s.layout==='flow'){
   const nodes=s.nodes; const n=nodes.length;const gap=0.34,w=(12.1-(n-1)*gap)/n;
   nodes.forEach((node,i)=>{const x=0.6+i*(w+gap);box(x,3.13,w,2.23);text(String(i+1).padStart(2,'0'),x+0.22,3.32,w-0.44,0.32,16,{color:T.accent});text(node.title.replace(/([a-z])([A-Z])/g,'$1 $2'),x+0.22,3.79,w-0.44,0.68,21,{bold:true});text(node.body.replace(/([a-z])([A-Z])/g,'$1 $2'),x+0.22,4.57,w-0.44,0.63,17,{color:T.muted});if(i<n-1)arrow(x+w+0.04,4.13,gap-0.08)});
   if(s.takeaway)text(s.takeaway,0.66,5.85,11.95,0.74,24,{color:T.accent});
  }else if(s.layout==='table'){
   slide.addTable([s.headers.map(t=>({text:t,options:{bold:true,color:T.accent,fill:'22324A'}})),...s.rows],{x:0.63,y:2.83,w:12.04,h:3.55,border:{type:'solid',color:T.edge,pt:0.5},fill:T.panel,color:T.text,fontFace:T.font,fontSize:20,margin:0.16,rowH:0.75,autoPage:false,colW:s.colW||[3.8,8.24],bold:false,paraSpaceAfterPt:0});
   if(s.takeaway)text(s.takeaway,0.65,6.49,11.8,0.25,13,{color:T.accent});
  }else if(s.layout==='image'){
   slide.addImage({path:s.image,x:0.65,y:2.66,w:8.05,h:3.97});box(9.0,2.66,3.68,3.97);text(s.sideTitle,9.25,2.95,3.1,0.8,25,{bold:true});text(s.body,9.25,3.95,3.1,2.27,21);text('DEMO · real components rendered from this source snapshot',0.68,6.70,11.3,0.19,10,{color:T.muted});
  }else{
   const cards=s.cards;const n=cards.length;const gap=0.34,w=(12.1-(n-1)*gap)/n;
   cards.forEach((card,i)=>{const x=0.6+i*(w+gap);box(x,2.80,w,3.70);text(card.label||String(i+1).padStart(2,'0'),x+0.25,3.04,w-0.5,0.34,15,{color:T.accent});text(card.title,x+0.25,3.58,w-0.5,0.85,26,{bold:true});text(card.body,x+0.25,4.62,w-0.5,1.63,22)});
   if(s.takeaway)text(s.takeaway,0.65,6.55,11.9,0.25,12,{color:T.muted});
  }
 }
 slide.addNotes(`Slide ID: ${s.id}\n\n${s.notes}\n\nSources:\n${s.sources.map(x=>`${x.file}:${x.start}-${x.end}${x.symbol?' — '+x.symbol:''}`).join('\n')}\n\nSnapshot: ${deck.snapshot.commit}; analysis ${deck.snapshot.analysisDate}. Working tree state is recorded in manifest.json.`);
 return {id:s.id,elements:geo};
}
