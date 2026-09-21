# Complete example modules

All `.ts` / `.tsx` modules are checked against the actual workspace source exports with strict TypeScript and Vite resource declarations. No examples perform production requests during verification.

Use them inside a React 19 browser host configured with the same source aliases and peer dependencies as this workspace. Each UI example imports its library stylesheet. Load the UI Kit base stylesheet once in the host. Host parameters in a function signature are required integration inputs; they are not fabricated API clients.

Examples with Core, sharing, overlay or MCP behavior require a running, configured backend/deployment and a host adapter. `example.com`, demo ids and synthetic amounts are illustrative.

```bash
npm run check:examples
```

| Module | Scope |
|---|---|
| [attachment-canvas.tsx](attachment-canvas.tsx) | attachment-canvas |
| [attachment-input.tsx](attachment-input.tsx) | attachment-input |
| [builder-form.tsx](builder-form.tsx) | builder-form |
| [catalog.tsx](catalog.tsx) | catalog |
| [chat-api-client.ts](chat-api-client.ts) | chat-api-client |
| [chat-hooks.tsx](chat-hooks.tsx) | chat-hooks |
| [chat-overlay.ts](chat-overlay.ts) | chat-overlay |
| [chat-shared.tsx](chat-shared.tsx) | chat-shared |
| [conversation-input.tsx](conversation-input.tsx) | conversation-input |
| [conversation-messages.tsx](conversation-messages.tsx) | conversation-messages |
| [conversation-panel.tsx](conversation-panel.tsx) | conversation-panel |
| [conversation-stages.tsx](conversation-stages.tsx) | conversation-stages |
| [mcp-apps.tsx](mcp-apps.tsx) | mcp-apps |
| [navigation-panel.tsx](navigation-panel.tsx) | navigation-panel |
| [prompt-editor.tsx](prompt-editor.tsx) | prompt-editor |
| [prompts.tsx](prompts.tsx) | prompts |
| [publish-panel.tsx](publish-panel.tsx) | publish-panel |
| [quotations.tsx](quotations.tsx) | quotations |
| [scheduled-tasks.tsx](scheduled-tasks.tsx) | scheduled-tasks |
| [settings-panel.tsx](settings-panel.tsx) | settings-panel |
| [share.tsx](share.tsx) | share |
| [sidebar.tsx](sidebar.tsx) | sidebar |
| [skill-editor.tsx](skill-editor.tsx) | skill-editor |
| [skills.tsx](skills.tsx) | skills |
| [source-panel.tsx](source-panel.tsx) | source-panel |
| [starter-buttons.tsx](starter-buttons.tsx) | starter-buttons |
| [toolset-editor.tsx](toolset-editor.tsx) | toolset-editor |
| [usage-dashboard.tsx](usage-dashboard.tsx) | usage-dashboard |

`source-excerpts.md` retains source-backed application code fragments that are explanatory excerpts rather than independently executable controllers.

The optional live component demo can be run with the existing repository Node/Vite dependencies:

```bash
node ../ai-dial-chat/node_modules/vite/bin/vite.js --config src/demo-vite.config.mts
node src/capture-demo.mjs
```

Run the commands from the bundle root with a compatible Node version (Node 24 was used for Vite). The demo source is under `demo/`; browser-capture prerequisites and outcomes are in `qa/demo-browser.json`.
