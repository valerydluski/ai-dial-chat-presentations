import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const require=createRequire(path.resolve(process.env.DIAL_REPO||'../ai-dial-chat','package.json'));
const {chromium}=require('playwright');
const base=process.env.SITE_URL||'http://127.0.0.1:4390/_site/';
const executablePath=process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const browser=await chromium.launch({executablePath,headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
const errors=[];const viewports=[];
page.on('pageerror',e=>errors.push(e.message));
page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`);});
const manifest=JSON.parse(fs.readFileSync('manifest.json','utf8'));
try{
  for(const [width,height] of [[1440,1000],[390,844],[360,800]]){
    await page.setViewportSize({width,height});
    await page.goto(base,{waitUntil:'networkidle'});
    const cards=await page.locator('.card').count();
    const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
    if(cards!==33||overflow)errors.push(`Gallery ${width}px: cards=${cards}, overflow=${overflow}`);
    if(width!==390)await page.screenshot({path:`qa/site-gallery-${width}.png`});
    await page.getByRole('link',{name:'View slides',exact:true}).first().click();
    await page.locator('.slide').first().waitFor();
    const slides=await page.locator('.slide').count();
    await page.locator('summary').first().click();
    const notesOpen=await page.locator('details').first().evaluate(e=>e.open);
    const viewerOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
    if(slides!==21||!notesOpen||viewerOverflow)errors.push(`Viewer ${width}px: slides=${slides}, notes=${notesOpen}, overflow=${viewerOverflow}`);
    viewports.push({width,height,galleryCards:cards,galleryOverflow:overflow,overviewSlides:slides,notesOpened:notesOpen,viewerOverflow});
    if(width===1440){
      const downloadPromise=page.waitForEvent('download');
      await page.getByRole('link',{name:'Download PowerPoint',exact:true}).click();
      const download=await downloadPromise;
      const bytes=fs.readFileSync(await download.path());
      const hash=crypto.createHash('sha256').update(bytes).digest('hex');
      if(hash!==manifest.decks[0].outputSha256)errors.push('Downloaded PowerPoint hash mismatch');
    }
  }
}finally{
  const result={base,browser:await browser.version(),viewports,downloadHashMatches:!errors.includes('Downloaded PowerPoint hash mismatch'),errors};
  fs.writeFileSync('qa/site-browser.json',JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result,null,2));
  await browser.close();
}
process.exitCode=errors.length?1:0;
