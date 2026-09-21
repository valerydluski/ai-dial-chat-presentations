import path from 'node:path';
import original from '../../ai-dial-chat/apps/chat/vite.config.mts';
const output=path.resolve(import.meta.dirname,'..');
const repository=path.resolve(output,'../ai-dial-chat');
const config=original();
export default {...config,root:path.join(output,'demo'),cacheDir:path.join(output,'.vite-demo'),server:{host:'127.0.0.1',port:4388,strictPort:true,fs:{allow:[output,repository]}},resolve:{...config.resolve,dedupe:['react','react-dom'],alias:{...config.resolve.alias,react:path.join(repository,'node_modules/react'),'react-dom':path.join(repository,'node_modules/react-dom')}},build:{outDir:path.join(output,'demo-dist'),emptyOutDir:true}};
