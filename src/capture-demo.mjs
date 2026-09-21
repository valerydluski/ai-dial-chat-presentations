import {createRequire} from 'node:module';import path from 'node:path';import fs from 'node:fs';
const require=createRequire(path.resolve('../ai-dial-chat/package.json'));const {chromium}=require('playwright');
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:710},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto('http://127.0.0.1:4388/',{waitUntil:'networkidle'});console.log('Page errors',errors); console.log((await page.locator('body').innerText()).slice(0,1500)); await page.locator('[data-demo="usage"]').waitFor({timeout:10000});await page.screenshot({path:'assets/component-demo.png'});
const tabs=page.getByRole('tab');if(await tabs.count()>0){await page.getByRole('tab',{name:'Profile',exact:true}).click();if(await page.getByRole('tab',{name:'Profile',exact:true}).getAttribute('aria-selected')!=='true')errors.push('Settings selection failed');}
await page.setViewportSize({width:390,height:844});await page.screenshot({path:'assets/component-demo-mobile.png',fullPage:true});
const overflow = await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);if(overflow)errors.push('Mobile horizontal overflow');
fs.writeFileSync('qa/demo-browser.json',JSON.stringify({url:'http://127.0.0.1:4388',browser:await browser.version(),errors,viewport:[1440,710],data:'Synthetic local data; no backend calls',source:'demo/main.tsx'},null,2));await browser.close();console.log(JSON.stringify({errors}));
