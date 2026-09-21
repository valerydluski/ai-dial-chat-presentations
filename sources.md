# Source index

Snapshot: `23fa39459d8971c10d5bd1c69734e61b124d249b`. Analysis date: 2026-09-21T18:14:40.584272+00:00.

Paths and line ranges refer to the recorded local working tree. Technical claims are linked per slide; research JSON retains README text, public declarations, source implementations, consumer imports and test assertions.

## overview-01 — AI DIAL Chat

- [docs/architecture.md:1-765](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/architecture.md)
- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)

## overview-02 — Start with the user workflows

- [apps/chat/src/types/routes.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/types/routes.ts)
- [apps/chat/src/pages/Conversation/Conversation.tsx:1-757](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/Conversation/Conversation.tsx)

## overview-03 — Four apps have different responsibilities

- [apps/chat/README.md:1-392](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/README.md)
- [apps/chat-api/README.md:1-1047](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/README.md)
- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)

## overview-04 — Libraries for the conversation workspace

- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)

## overview-05 — Libraries for knowledge and integration

- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)

## overview-06 — Application edges connect the layers

- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)
- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)
- [apps/chat-api/src/app/app.module.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/app.module.ts)

## overview-07 — One message enters the backend

- [apps/chat/src/pages/Conversation/Conversation.tsx:1-757](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/Conversation/Conversation.tsx)
- [apps/chat/src/server-api/chat-stream.api.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/chat-stream.api.ts)
- [libs/chat-hooks/src/conversation/create-chat-stream-api.ts:1-242](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/create-chat-stream-api.ts)
- [apps/chat-api/src/conversations/conversation.controller.ts:1-852](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation.controller.ts)

## overview-08 — Chunks return through a shared lifecycle

- [apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts)
- [apps/chat-api/src/conversations/conversation.controller.ts:1-852](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation.controller.ts)
- [libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts)

## overview-09 — Separate clients, hooks and adapters

- [libs/chat-api-client/src/generated/src/runtime.ts:1-511](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/runtime.ts)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:1-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts)
- [apps/chat/src/server-api/api-client.ts:1-106](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/api-client.ts)
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## overview-10 — Compose a view from focused parts

- [apps/chat/src/components/ConversationView/ConversationView.tsx:1-1263](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationView.tsx)
- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)
- [apps/chat/src/pages/Conversation/Conversation.tsx:1-757](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/Conversation/Conversation.tsx)

## overview-21 — See three libraries in one host

- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx)

## overview-11 — Choose a reuse boundary

- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [tools/publish-lib.mjs:1-282](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/tools/publish-lib.mjs)

## overview-12 — Theme tokens travel from host to component

- [docs/theme-customization.md:1-396](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/theme-customization.md)
- [apps/chat-api/src/themes/theme.controller.ts:1-131](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/themes/theme.controller.ts)
- [apps/chat/src/context/ThemeContext.tsx:1-171](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/context/ThemeContext.tsx)
- [libs/chat-shared/src/utils/build-css-vars.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts)

## overview-13 — Localization support has a clear current limit

- [apps/chat/src/i18n/config.ts:1-32](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/i18n/config.ts)
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)
- [libs/navigation-panel/src/models/navigation-panel-props.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts)

## overview-14 — Authentication belongs at the BFF

- [docs/auth/auth-bff-encrypted-cookie.md:1-442](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/auth/auth-bff-encrypted-cookie.md)
- [apps/chat-api/src/auth/session/session.guard.ts:1-112](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/session/session.guard.ts)
- [apps/chat-api/src/auth/session/session.service.ts:1-58](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/session/session.service.ts)
- [apps/chat-api/src/auth/refresh/refresh.service.ts:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/refresh/refresh.service.ts)

## overview-15 — Two upstream APIs share the browser stream

- [docs/responses-api-integration.md:1-460](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/responses-api-integration.md)
- [apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts)
- [apps/chat-api/src/conversations/generation/generation-api.ts:1-27](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/generation/generation-api.ts)

## overview-16 — Run the applications locally

- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)
- [apps/chat/vite.config.mts:1-267](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/vite.config.mts)
- [apps/chat-api/README.md:1-1047](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/README.md)
- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)

## overview-17 — Use the checks that match the change

- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)
- [nx.json:1-121](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/nx.json)

## overview-18 — Modularity gives specific engineering benefits

- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx:1-151](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx)
- [libs/attachment-canvas/src/models/attachment-canvas.ts:1-620](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts)
- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)

## overview-19 — Tradeoffs remain visible

- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts)
- [apps/chat-api/src/conversations/conversation-generation.service.ts:1-340](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation-generation.service.ts)

## overview-20 — Start with a vertical path through the code

- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)
- [apps/chat/src/app/app.tsx:1-582](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/app/app.tsx)
- [apps/chat/src/server-api/api-client.ts:1-106](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/api-client.ts)

## apps-chat-01 — Chat frontend

- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)
- [apps/chat/src/app/app.tsx:1-582](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/app/app.tsx)

## apps-chat-02 — The frontend owns the user workflow

- [apps/chat/src/types/routes.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/types/routes.ts)

## apps-chat-03 — Bootstrap the application once

- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)
- [apps/chat/src/app/app.tsx:1-582](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/app/app.tsx)

## apps-chat-04 — Providers define state ownership

- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)

## apps-chat-05 — Routes connect reusable screens

- [apps/chat/src/types/routes.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/types/routes.ts)
- [apps/chat/src/app/app.tsx:1-582](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/app/app.tsx)

## apps-chat-06 — Trace a message from UI intent

- [apps/chat/src/pages/Conversation/Conversation.tsx:1-757](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/Conversation/Conversation.tsx)
- [apps/chat/src/server-api/chat-stream.api.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/chat-stream.api.ts)
- [libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts)

## apps-chat-07 — Configure the generated client at the edge

- [apps/chat/src/server-api/api-client.ts:1-106](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/api-client.ts)

## apps-chat-08 — Assemble evidence around each message

- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)
- [apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx)
- [apps/chat/src/app/app.tsx:1-582](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/app/app.tsx)

## apps-chat-09 — Theme, locale and viewport are host concerns

- [apps/chat/src/context/ThemeContext.tsx:1-171](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/context/ThemeContext.tsx)
- [apps/chat/src/i18n/config.ts:1-32](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/i18n/config.ts)
- [apps/chat/src/hooks/breakpoint/useBreakpoint.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/hooks/breakpoint/useBreakpoint.ts)

## apps-chat-10 — A concrete extension: message content slots

- [libs/conversation-messages/src/models/message-bubble.ts:1-177](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts)
- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)

## apps-chat-15 — Inspect the reusable pieces in isolation

- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx)

## apps-chat-11 — Run and build the frontend

- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)
- [apps/chat/vite.config.mts:1-267](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/vite.config.mts)

## apps-chat-12 — Inspect behavior through existing tests

- [apps/chat/src/pages/ConversationRoute/ConversationRoute.integration.spec.tsx:1-332](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/ConversationRoute/ConversationRoute.integration.spec.tsx)
- [apps/chat/src/components/ConversationView/tests/ConversationMessageItem.spec.tsx:1-1491](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/tests/ConversationMessageItem.spec.tsx)
- [apps/chat/src/context/overlay/tests/OverlayContext.spec.tsx:1-1443](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/context/overlay/tests/OverlayContext.spec.tsx)

## apps-chat-13 — Integration limits are part of the design

- [apps/chat/src/main.tsx:1-108](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/main.tsx)
- [apps/chat/src/server-api/chat.api.ts:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/chat.api.ts)
- [apps/chat-api/README.md:1-1047](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/README.md)

## apps-chat-14 — Follow one feature end to end

- [apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/PromptEditor/PromptEditor.tsx)
- [apps/chat/src/server-api/api-client.ts:1-106](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/server-api/api-client.ts)
- [libs/prompt-editor/src/models/prompt-editor-props.ts:1-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts)

## apps-chat-api-01 — Chat backend

- [apps/chat-api/src/main.ts:1-213](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/main.ts)
- [apps/chat-api/src/app/app.module.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/app.module.ts)

## apps-chat-api-02 — Keep three boundaries explicit

- [apps/chat-api/src/main.ts:1-213](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/main.ts)
- [apps/chat-api/src/app/app.module.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/app.module.ts)
- [apps/chat-api/src/dial/dial-client.service.ts:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/dial/dial-client.service.ts)

## apps-chat-api-03 — Bootstrap establishes cross-cutting behavior

- [apps/chat-api/src/main.ts:1-213](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/main.ts)
- [apps/chat-api/src/app/app.module.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/app.module.ts)

## apps-chat-api-04 — Domain modules organize the backend

- [apps/chat-api/src/app/app.module.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/app.module.ts)

## apps-chat-api-05 — Representative HTTP contracts

- [apps/chat-api/src/deployments/deployments.controller.ts:1-194](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/deployments/deployments.controller.ts)
- [apps/chat-api/src/conversations/conversation.controller.ts:1-852](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation.controller.ts)
- [apps/chat-api/src/auth/auth.controller.ts:1-702](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/auth.controller.ts)
- [apps/chat-api/src/themes/theme.controller.ts:1-131](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/themes/theme.controller.ts)

## apps-chat-api-06 — A completion has a persisted lifecycle

- [apps/chat-api/src/conversations/conversation.controller.ts:1-852](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation.controller.ts)
- [apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts)
- [apps/chat-api/src/conversations/conversation-generation.service.ts:1-340](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation-generation.service.ts)

## apps-chat-api-07 — Upstream dispatch is controlled on the server

- [apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts)
- [apps/chat-api/src/conversations/generation/generation-api.ts:1-27](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/generation/generation-api.ts)
- [docs/responses-api-integration.md:1-460](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/responses-api-integration.md)

## apps-chat-api-08 — Authentication has explicit request scope

- [apps/chat-api/src/auth/session/session.guard.ts:1-112](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/session/session.guard.ts)
- [apps/chat-api/src/auth/strategies/cookie-session.strategy.ts:1-147](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/strategies/cookie-session.strategy.ts)
- [apps/chat-api/src/auth/strategies/header-token.strategy.ts:1-256](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/strategies/header-token.strategy.ts)
- [apps/chat-api/src/auth/session/session.service.ts:1-58](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/session/session.service.ts)

## apps-chat-api-09 — Keep controller and DTO changes synchronized

- [apps/chat-api/src/chat/chat.controller.ts:1-33](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/chat/chat.controller.ts)
- [apps/chat-api/src/chat/dto/chat-completion.dto.ts:1-104](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/chat/dto/chat-completion.dto.ts)

## apps-chat-api-10 — Regenerate the contract after API changes

- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)
- [tools/openapi/check-client.mjs:1-46](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/tools/openapi/check-client.mjs)
- [apps/chat-api/src/openapi/openapi.config.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/openapi/openapi.config.ts)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)

## apps-chat-api-11 — Configure the runtime deliberately

- [apps/chat-api/README.md:1-1047](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/README.md)
- [apps/chat-api/src/config/environment.config.ts:1-960](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/config/environment.config.ts)

## apps-chat-api-12 — Run and verify the backend

- [package.json:1-199](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json)
- [apps/chat-api/src/main.ts:1-213](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/main.ts)

## apps-chat-api-13 — Existing tests exercise contracts and failures

- [apps/chat-api/src/conversations/tests/conversation.controller.integration.spec.ts:1-911](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/tests/conversation.controller.integration.spec.ts)
- [apps/chat-api/src/auth/session/tests/session.guard.spec.ts:1-147](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/auth/session/tests/session.guard.spec.ts)
- [apps/chat-api/src/chat/tests/chat.controller.integration.spec.ts:1-117](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/chat/tests/chat.controller.integration.spec.ts)

## apps-chat-api-14 — Operational tradeoffs shape deployment

- [apps/chat-api/src/conversations/conversation-generation.service.ts:1-340](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/conversations/conversation-generation.service.ts)
- [apps/chat-api/src/app/cache.config.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/cache.config.ts)
- [apps/chat-api/src/themes/theme.controller.ts:1-131](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/themes/theme.controller.ts)

## apps-chat-overlay-sandbox-01 — Overlay sandbox

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [apps/chat-overlay-sandbox/src/main.tsx:1-15](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/src/main.tsx)

## apps-chat-overlay-sandbox-02 — Each case demonstrates a distinct contract

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)

## apps-chat-overlay-sandbox-03 — Trace the host-to-chat handshake

- [libs/chat-overlay/src/lib/ChatOverlay.ts:1-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts)
- [apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx)

## apps-chat-overlay-sandbox-04 — Reproduce the local scenario

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [apps/chat-overlay-sandbox/vite.config.mts:1-59](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/vite.config.mts)

## apps-chat-overlay-sandbox-05 — A direct overlay is a small integration

- [apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:1-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts)

## apps-chat-overlay-sandbox-06 — Deployment shares the main chat image

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [Dockerfile:1-70](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/Dockerfile)
- [apps/chat-api/src/app/static-assets.ts:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/app/static-assets.ts)

## apps-chat-overlay-sandbox-07 — Verify cases through the current targets

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [apps/chat-overlay-sandbox/package.json:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/package.json)

## apps-chat-overlay-sandbox-08 — Interpret integration failures at the right layer

- [apps/chat-overlay-sandbox/README.md:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/README.md)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:1-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts)

## apps-mcp-app-sandbox-01 — MCP sandbox proxy

- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)
- [apps/mcp-app-sandbox/src/main.ts:1-49](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/main.ts)

## apps-mcp-app-sandbox-02 — Why a separate application exists

- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)
- [apps/mcp-app-sandbox/src/main.ts:1-49](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/main.ts)
- [apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox-page.ts)

## apps-mcp-app-sandbox-03 — Request validation precedes HTML delivery

- [apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox.controller.ts)
- [apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox.service.ts)

## apps-mcp-app-sandbox-04 — Configure two sides of the connection

- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)
- [apps/mcp-app-sandbox/src/config/environment.config.ts:1-29](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/config/environment.config.ts)

## apps-mcp-app-sandbox-05 — The page and policy are app-owned

- [apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox.controller.ts)
- [apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox.service.ts)
- [apps/mcp-app-sandbox/src/app/csp.ts:1-19](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/csp.ts)
- [apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox-page.ts)

## apps-mcp-app-sandbox-06 — A rendered MCP view needs the whole chain

- [libs/mcp-apps/src/models/mcp-apps.ts:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/models/mcp-apps.ts)
- [libs/attachment-canvas/src/components/McpAppCanvasRenderer/McpAppCanvasRenderer.tsx:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/McpAppCanvasRenderer/McpAppCanvasRenderer.tsx)
- [apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox-page.ts)

## apps-mcp-app-sandbox-07 — Build and check what exists

- [apps/mcp-app-sandbox/package.json:1-103](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/package.json)
- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)
- [apps/mcp-app-sandbox/Dockerfile:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/Dockerfile)

## apps-mcp-app-sandbox-08 — Limits to carry into operations

- [apps/mcp-app-sandbox/README.md:1-60](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/README.md)
- [apps/mcp-app-sandbox/src/main.ts:1-49](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/main.ts)
- [apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/mcp-app-sandbox/src/app/sandbox.service.ts)

## lib-attachment-canvas-01 — Attachment canvas

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-02 — When this library is useful

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-03 — Follow the ownership boundary

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-attachment-canvas-04 — The public contract to start with

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-05 — A minimal workspace integration

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-06 — Wire a realistic host workflow

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-10 — Context-based canvas control

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-07 — Available customization

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`

## lib-attachment-canvas-08 — Find the integration and its checks

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`
- [libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts:1-154](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts)
- [libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts:1-1174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts)
- [libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx:1-85](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx)

## lib-attachment-canvas-09 — Constraints that affect integration

- [libs/attachment-canvas/README.md:1-615](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/README.md)
- [libs/attachment-canvas/src/index.ts:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/index.ts)
- [libs/attachment-canvas/package.json:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/package.json)
- [libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx) — `AttachmentCanvas`
- [libs/attachment-canvas/src/models/attachment-canvas.ts:487-542](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-canvas/src/models/attachment-canvas.ts) — `AttachmentCanvasProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-attachment-input-01 — Attachment input

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-02 — When this library is useful

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-03 — Follow the ownership boundary

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-attachment-input-04 — The public contract to start with

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-05 — A minimal workspace integration

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-06 — Wire a realistic host workflow

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-07 — Available customization

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`

## lib-attachment-input-08 — Find the integration and its checks

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`
- [libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx)
- [libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts:1-181](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts)
- [libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx:1-74](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx)

## lib-attachment-input-09 — Constraints that affect integration

- [libs/attachment-input/README.md:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md)
- [libs/attachment-input/src/index.ts:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/index.ts)
- [libs/attachment-input/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/package.json)
- [libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx) — `AttachmentTray`
- [libs/attachment-input/src/models/attachment-tray.ts:24-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/models/attachment-tray.ts) — `AttachmentTrayProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-builder-form-01 — Builder form

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-02 — When this library is useful

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-03 — Follow the ownership boundary

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-builder-form-04 — The public contract to start with

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-05 — A minimal workspace integration

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-06 — Wire a realistic host workflow

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-10 — Validate without translating

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-07 — Available customization

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`

## lib-builder-form-08 — Find the integration and its checks

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx)
- [libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx:1-183](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx)
- [libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx:1-95](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx)

## lib-builder-form-09 — Constraints that affect integration

- [libs/builder-form/README.md:1-420](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/README.md)
- [libs/builder-form/src/index.ts:1-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/index.ts)
- [libs/builder-form/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/package.json)
- [libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/components/EditorLayout/EditorLayout.tsx) — `EditorLayout`
- [libs/builder-form/src/models/editor-layout-props.ts:24-45](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/builder-form/src/models/editor-layout-props.ts) — `EditorLayoutProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-catalog-01 — Catalog

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-02 — When this library is useful

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-03 — Follow the ownership boundary

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-catalog-04 — The public contract to start with

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-05 — A minimal workspace integration

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-06 — Wire a realistic host workflow

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-10 — Choose the headless entry

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`
- [libs/catalog/src/utils/catalog-filter.ts:37-56](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/utils/catalog-filter.ts)

## lib-catalog-07 — Available customization

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`

## lib-catalog-08 — Find the integration and its checks

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`
- [libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx:1-13](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx)
- [libs/catalog/src/components/Filter/tests/Filter.spec.tsx:1-190](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Filter/tests/Filter.spec.tsx)
- [libs/catalog/src/components/CardGrid/tests/Card.spec.tsx:1-306](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/CardGrid/tests/Card.spec.tsx)

## lib-catalog-09 — Constraints that affect integration

- [libs/catalog/README.md:1-973](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/README.md)
- [libs/catalog/src/index.ts:1-157](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/index.ts)
- [libs/catalog/package.json:1-51](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/package.json)
- [libs/catalog/src/components/Catalog/Catalog.tsx:57-778](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/components/Catalog/Catalog.tsx) — `Catalog`
- [libs/catalog/src/models/catalog-props.ts:89-462](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/catalog/src/models/catalog-props.ts) — `CatalogProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-api-client-01 — Chat API client

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-02 — When this library is useful

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-03 — Follow the ownership boundary

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-api-client-04 — The public contract to start with

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-05 — A minimal workspace integration

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-06 — Wire a realistic host workflow

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-10 — Preserve transport details when needed

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-07 — Available customization

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`

## lib-chat-api-client-08 — Find the integration and its checks

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`
- [libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts)

## lib-chat-api-client-09 — Constraints that affect integration

- [libs/chat-api-client/README.md:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md)
- [libs/chat-api-client/src/index.ts:1-1](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/index.ts)
- [libs/chat-api-client/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/package.json)
- [libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) — `DeploymentsApi`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-hooks-01 — Chat hooks

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-02 — When this library is useful

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-03 — Follow the ownership boundary

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-hooks-04 — The public contract to start with

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-05 — A minimal workspace integration

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-06 — Wire a realistic host workflow

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-10 — A request lifecycle with an injected client

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-07 — Available customization

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`

## lib-chat-hooks-08 — Find the integration and its checks

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`
- [libs/toolset-editor/src/components/AuthSection/AuthSection.tsx:1-504](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/AuthSection/AuthSection.tsx)
- [libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts:1-63](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts)
- [libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts:1-84](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts)

## lib-chat-hooks-09 — Constraints that affect integration

- [libs/chat-hooks/README.md:1-3809](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/README.md)
- [libs/chat-hooks/src/index.ts:1-184](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/index.ts)
- [libs/chat-hooks/package.json:1-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/package.json)
- [libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/useShareLink/useShareLink.ts) — `useShareLink`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-overlay-01 — Chat overlay

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-02 — When this library is useful

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-03 — Follow the ownership boundary

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-overlay-04 — The public contract to start with

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-05 — A minimal workspace integration

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-06 — Wire a realistic host workflow

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-10 — Subscribe and clean up

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-07 — Available customization

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`

## lib-chat-overlay-08 — Find the integration and its checks

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`
- [apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx:1-317](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx)
- [libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts:1-1060](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts)
- [libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts)

## lib-chat-overlay-09 — Constraints that affect integration

- [libs/chat-overlay/README.md:1-307](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/README.md)
- [libs/chat-overlay/src/index.ts:1-4](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/index.ts)
- [libs/chat-overlay/package.json:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/package.json)
- [libs/chat-overlay/src/lib/ChatOverlay.ts:110-494](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-overlay/src/lib/ChatOverlay.ts) — `ChatOverlay`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-shared-01 — Chat shared

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-02 — When this library is useful

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-03 — Follow the ownership boundary

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-chat-shared-04 — The public contract to start with

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-05 — A minimal workspace integration

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-06 — Wire a realistic host workflow

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-10 — Reuse the Markdown entry

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-07 — Available customization

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`

## lib-chat-shared-08 — Find the integration and its checks

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx)
- [libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx:1-484](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx)
- [libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts:1-258](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts)

## lib-chat-shared-09 — Constraints that affect integration

- [libs/chat-shared/README.md:1-986](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/README.md)
- [libs/chat-shared/src/index.ts:1-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts)
- [libs/chat-shared/package.json:1-80](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/package.json)
- [libs/chat-shared/src/utils/build-css-vars.ts:4-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/utils/build-css-vars.ts) — `buildCssVars`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-input-01 — Conversation input

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-02 — When this library is useful

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-03 — Follow the ownership boundary

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-input-04 — The public contract to start with

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-05 — A minimal workspace integration

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-06 — Wire a realistic host workflow

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-07 — Available customization

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`

## lib-conversation-input-08 — Find the integration and its checks

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`
- [apps/chat/src/hooks/conversation/useAudioTranscription.ts:1-100](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/hooks/conversation/useAudioTranscription.ts)
- [libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx:1-309](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx)
- [libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts:1-265](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts)

## lib-conversation-input-09 — Constraints that affect integration

- [libs/conversation-input/README.md:1-355](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/README.md)
- [libs/conversation-input/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/index.ts)
- [libs/conversation-input/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/package.json)
- [libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx) — `ConversationInput`
- [libs/conversation-input/src/models/ConversationInput.ts:182-455](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-input/src/models/ConversationInput.ts) — `ConversationInputProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-messages-01 — Conversation messages

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-02 — When this library is useful

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-03 — Follow the ownership boundary

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-messages-04 — The public contract to start with

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-05 — A minimal workspace integration

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-06 — Wire a realistic host workflow

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-07 — Available customization

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`

## lib-conversation-messages-08 — Find the integration and its checks

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`
- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)
- [libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx:1-269](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx)
- [libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx:1-92](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx)

## lib-conversation-messages-09 — Constraints that affect integration

- [libs/conversation-messages/README.md:1-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/README.md)
- [libs/conversation-messages/src/index.ts:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/index.ts)
- [libs/conversation-messages/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/package.json)
- [libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx) — `AssistantMessageBubble`
- [libs/conversation-messages/src/models/message-bubble.ts:143-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-messages/src/models/message-bubble.ts) — `AssistantMessageBubbleProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-panel-01 — Conversation panel

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-02 — When this library is useful

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-03 — Follow the ownership boundary

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-panel-04 — The public contract to start with

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-05 — A minimal workspace integration

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-06 — Wire a realistic host workflow

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-07 — Available customization

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`

## lib-conversation-panel-08 — Find the integration and its checks

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`
- [apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx:1-1510](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx)
- [libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx:1-61](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx)
- [libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx:1-356](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx)

## lib-conversation-panel-09 — Constraints that affect integration

- [libs/conversation-panel/README.md:1-406](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/README.md)
- [libs/conversation-panel/src/index.ts:1-28](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/index.ts)
- [libs/conversation-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/package.json)
- [libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx) — `ConversationPanel`
- [libs/conversation-panel/src/models/panel-props.ts:162-223](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-panel/src/models/panel-props.ts) — `ConversationPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-stages-01 — Conversation stages

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-02 — When this library is useful

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-03 — Follow the ownership boundary

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-conversation-stages-04 — The public contract to start with

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-05 — A minimal workspace integration

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-10 — See a streaming stage in context

- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx)

## lib-conversation-stages-06 — Wire a realistic host workflow

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-07 — Available customization

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`

## lib-conversation-stages-08 — Find the integration and its checks

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`
- [apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationView/ConversationMessageItem.tsx)
- [libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx)
- [libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx:1-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx)

## lib-conversation-stages-09 — Constraints that affect integration

- [libs/conversation-stages/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/README.md)
- [libs/conversation-stages/src/index.ts:1-17](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/index.ts)
- [libs/conversation-stages/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/package.json)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx) — `StagesPanel`
- [libs/conversation-stages/src/models/stages-props.ts:78-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/models/stages-props.ts) — `StagesPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-mcp-apps-01 — MCP Apps

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-02 — When this library is useful

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-03 — Follow the ownership boundary

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-mcp-apps-04 — The public contract to start with

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-05 — A minimal workspace integration

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-06 — Wire a realistic host workflow

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-07 — Available customization

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`

## lib-mcp-apps-08 — Find the integration and its checks

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`
- [libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts:1-118](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts)
- [libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx:1-141](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx)

## lib-mcp-apps-09 — Constraints that affect integration

- [libs/mcp-apps/README.md:1-148](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/README.md)
- [libs/mcp-apps/src/index.ts:1-31](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/index.ts)
- [libs/mcp-apps/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/package.json)
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreview`
- [libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx) — `McpAppInlinePreviewProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-navigation-panel-01 — Navigation panel

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-02 — When this library is useful

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-03 — Follow the ownership boundary

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-navigation-panel-04 — The public contract to start with

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-05 — A minimal workspace integration

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-06 — Wire a realistic host workflow

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-07 — Available customization

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`

## lib-navigation-panel-08 — Find the integration and its checks

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`
- [apps/chat/src/components/Navigation/Navigation.tsx:1-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/Navigation/Navigation.tsx)
- [libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx:1-143](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx)
- [libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx)

## lib-navigation-panel-09 — Constraints that affect integration

- [libs/navigation-panel/README.md:1-208](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/README.md)
- [libs/navigation-panel/src/index.ts:1-54](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/index.ts)
- [libs/navigation-panel/package.json:1-40](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/package.json)
- [libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx) — `NavigationPanel`
- [libs/navigation-panel/src/models/navigation-panel-props.ts:60-73](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/navigation-panel/src/models/navigation-panel-props.ts) — `NavigationPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-prompt-editor-01 — Prompt editor

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-02 — When this library is useful

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-03 — Follow the ownership boundary

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-prompt-editor-04 — The public contract to start with

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-05 — A minimal workspace integration

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-06 — Wire a realistic host workflow

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-07 — Available customization

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`

## lib-prompt-editor-08 — Find the integration and its checks

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`
- [apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/PromptEditor/PromptEditor.tsx)
- [libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx)
- [libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx:1-247](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx)

## lib-prompt-editor-09 — Constraints that affect integration

- [libs/prompt-editor/README.md:1-160](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/README.md)
- [libs/prompt-editor/src/index.ts:1-16](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/index.ts)
- [libs/prompt-editor/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/package.json)
- [libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx) — `PromptEditor`
- [libs/prompt-editor/src/models/prompt-editor-props.ts:125-162](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompt-editor/src/models/prompt-editor-props.ts) — `PromptEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-prompts-01 — Prompts

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-02 — When this library is useful

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-03 — Follow the ownership boundary

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-prompts-04 — The public contract to start with

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-05 — A minimal workspace integration

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-06 — Wire a realistic host workflow

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-07 — Available customization

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`

## lib-prompts-08 — Find the integration and its checks

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`
- [apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx:1-71](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx)
- [libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx:1-205](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx)
- [libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx:1-151](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx)

## lib-prompts-09 — Constraints that affect integration

- [libs/prompts/README.md:1-145](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md)
- [libs/prompts/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/index.ts)
- [libs/prompts/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/package.json)
- [libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx) — `PromptParametersPopup`
- [libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) — `PromptParametersPopupProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-publish-panel-01 — Publish panel

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-02 — When this library is useful

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-03 — Follow the ownership boundary

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-publish-panel-04 — The public contract to start with

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-05 — A minimal workspace integration

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-06 — Wire a realistic host workflow

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-07 — Available customization

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`

## lib-publish-panel-08 — Find the integration and its checks

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`
- [libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts:1-79](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts)
- [libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx:1-503](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx)
- [libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx:1-97](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx)

## lib-publish-panel-09 — Constraints that affect integration

- [libs/publish-panel/README.md:1-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/README.md)
- [libs/publish-panel/src/index.ts:1-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/index.ts)
- [libs/publish-panel/package.json:1-44](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/package.json)
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanel`
- [libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx) — `PublishPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-quotations-01 — Quotations

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-02 — When this library is useful

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-03 — Follow the ownership boundary

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-quotations-04 — The public contract to start with

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-05 — A minimal workspace integration

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-06 — Wire a realistic host workflow

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-07 — Available customization

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`

## lib-quotations-08 — Find the integration and its checks

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`
- [libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts:1-102](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts)
- [libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx:1-545](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx)
- [libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx:1-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx)

## lib-quotations-09 — Constraints that affect integration

- [libs/quotations/README.md:1-245](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/README.md)
- [libs/quotations/src/index.ts:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/index.ts)
- [libs/quotations/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/package.json)
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarker`
- [libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/quotations/src/components/CitationMarker/CitationMarker.tsx) — `CitationMarkerProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-scheduled-tasks-01 — Scheduled tasks

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-02 — When this library is useful

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-03 — Follow the ownership boundary

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-scheduled-tasks-04 — The public contract to start with

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-05 — A minimal workspace integration

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-06 — Wire a realistic host workflow

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-07 — Available customization

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`

## lib-scheduled-tasks-08 — Find the integration and its checks

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`
- [apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx:1-413](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx)
- [libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx:1-201](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx)
- [libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx:1-89](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx)

## lib-scheduled-tasks-09 — Constraints that affect integration

- [libs/scheduled-tasks/README.md:1-215](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/README.md)
- [libs/scheduled-tasks/src/index.ts:1-68](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/index.ts)
- [libs/scheduled-tasks/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/package.json)
- [libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx) — `ScheduledTasks`
- [libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/scheduled-tasks/src/models/scheduled-tasks-props.ts) — `ScheduledTasksProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-settings-panel-01 — Settings panel

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-02 — When this library is useful

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-03 — Follow the ownership boundary

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-settings-panel-04 — The public contract to start with

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-05 — A minimal workspace integration

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-10 — See controlled selection in the browser

- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx)

## lib-settings-panel-06 — Wire a realistic host workflow

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-07 — Available customization

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`

## lib-settings-panel-08 — Find the integration and its checks

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`
- [apps/chat/src/pages/SettingsPage/SettingsPage.tsx:1-35](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/SettingsPage/SettingsPage.tsx)
- [libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx:1-225](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx)

## lib-settings-panel-09 — Constraints that affect integration

- [libs/settings-panel/README.md:1-115](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/README.md)
- [libs/settings-panel/src/index.ts:1-9](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/index.ts)
- [libs/settings-panel/package.json:1-37](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/package.json)
- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx) — `SettingsPanel`
- [libs/settings-panel/src/models/settings-panel-props.ts:52-65](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/models/settings-panel-props.ts) — `SettingsPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-share-01 — Share

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-02 — When this library is useful

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-03 — Follow the ownership boundary

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-share-04 — The public contract to start with

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-05 — A minimal workspace integration

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-06 — Wire a realistic host workflow

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-07 — Available customization

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`

## lib-share-08 — Find the integration and its checks

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`
- [apps/chat-api/src/share/dto/create-share-link.dto.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/share/dto/create-share-link.dto.ts)
- [libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx:1-460](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx)

## lib-share-09 — Constraints that affect integration

- [libs/share/README.md:1-123](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/README.md)
- [libs/share/src/index.ts:1-18](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/index.ts)
- [libs/share/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/package.json)
- [libs/share/src/components/SharePopover/SharePopover.tsx:326-326](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/components/SharePopover/SharePopover.tsx) — `SharePopover`
- [libs/share/src/models/share-popover-props.ts:108-129](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/share/src/models/share-popover-props.ts) — `SharePopoverProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-sidebar-01 — Sidebar

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-02 — When this library is useful

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-03 — Follow the ownership boundary

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-sidebar-04 — The public contract to start with

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-05 — A minimal workspace integration

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-06 — Wire a realistic host workflow

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-07 — Available customization

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`

## lib-sidebar-08 — Find the integration and its checks

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx)
- [libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx:1-312](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx)
- [libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx:1-87](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx)

## lib-sidebar-09 — Constraints that affect integration

- [libs/sidebar/README.md:1-173](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/README.md)
- [libs/sidebar/src/index.ts:1-14](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/index.ts)
- [libs/sidebar/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/package.json)
- [libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx) — `SidebarPanel`
- [libs/sidebar/src/models/panel-props.ts:51-90](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/sidebar/src/models/panel-props.ts) — `SidebarPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-skill-editor-01 — Skill editor

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-02 — When this library is useful

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-03 — Follow the ownership boundary

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-skill-editor-04 — The public contract to start with

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-05 — A minimal workspace integration

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-06 — Wire a realistic host workflow

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-07 — Available customization

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`

## lib-skill-editor-08 — Find the integration and its checks

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`
- [libs/chat-hooks/src/skill/skill.ts:1-256](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-hooks/src/skill/skill.ts)
- [libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts:1-84](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts)
- [libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx)

## lib-skill-editor-09 — Constraints that affect integration

- [libs/skill-editor/README.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/README.md)
- [libs/skill-editor/src/index.ts:1-23](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/index.ts)
- [libs/skill-editor/package.json:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/package.json)
- [libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx) — `SkillEditor`
- [libs/skill-editor/src/models/skill-editor-props.ts:236-315](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skill-editor/src/models/skill-editor-props.ts) — `SkillEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-skills-01 — Skills

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-02 — When this library is useful

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-03 — Follow the ownership boundary

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-skills-04 — The public contract to start with

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-05 — A minimal workspace integration

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-06 — Wire a realistic host workflow

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-07 — Available customization

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`

## lib-skills-08 — Find the integration and its checks

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`
- [apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx:1-120](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx)
- [libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx:1-72](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx)

## lib-skills-09 — Constraints that affect integration

- [libs/skills/README.md:1-378](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/README.md)
- [libs/skills/src/index.ts:1-30](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/index.ts)
- [libs/skills/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/package.json)
- [libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx) — `FavoriteSkillsPanel`
- [libs/skills/src/models/favorite-skills-panel-props.ts:34-62](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/skills/src/models/favorite-skills-panel-props.ts) — `FavoriteSkillsPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-source-panel-01 — Source panel

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-02 — When this library is useful

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-03 — Follow the ownership boundary

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-source-panel-04 — The public contract to start with

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-05 — A minimal workspace integration

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-06 — Wire a realistic host workflow

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-07 — Available customization

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`

## lib-source-panel-08 — Find the integration and its checks

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`
- [apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx)
- [libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx:1-116](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx)
- [libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx)

## lib-source-panel-09 — Constraints that affect integration

- [libs/source-panel/README.md:1-142](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/README.md)
- [libs/source-panel/src/index.ts:1-10](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/index.ts)
- [libs/source-panel/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/package.json)
- [libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx) — `ConversationSourcesPanel`
- [libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/source-panel/src/models/conversation-sources-panel-props.ts) — `ConversationSourcesPanelProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-starter-buttons-01 — Starter buttons

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-02 — When this library is useful

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-03 — Follow the ownership boundary

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-starter-buttons-04 — The public contract to start with

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-05 — A minimal workspace integration

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-06 — Wire a realistic host workflow

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-07 — Available customization

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`

## lib-starter-buttons-08 — Find the integration and its checks

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`
- [apps/chat/src/components/StarterButtons/StarterButtons.tsx:1-34](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/components/StarterButtons/StarterButtons.tsx)
- [libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx:1-48](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx)
- [libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx:1-64](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx)

## lib-starter-buttons-09 — Constraints that affect integration

- [libs/starter-buttons/README.md:1-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/README.md)
- [libs/starter-buttons/src/index.ts:1-7](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/index.ts)
- [libs/starter-buttons/package.json:1-39](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/package.json)
- [libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx) — `StarterButtons`
- [libs/starter-buttons/src/models/starter-props.ts:20-38](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/starter-buttons/src/models/starter-props.ts) — `StarterButtonsProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-toolset-editor-01 — Toolset editor

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-02 — When this library is useful

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-03 — Follow the ownership boundary

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-toolset-editor-04 — The public contract to start with

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-05 — A minimal workspace integration

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-06 — Wire a realistic host workflow

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-10 — Validate a candidate endpoint

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-07 — Available customization

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`

## lib-toolset-editor-08 — Find the integration and its checks

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`
- [apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx:1-463](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx)
- [libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx:1-63](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx)
- [libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx:1-808](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx)

## lib-toolset-editor-09 — Constraints that affect integration

- [libs/toolset-editor/README.md:1-383](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/README.md)
- [libs/toolset-editor/src/index.ts:1-47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/index.ts)
- [libs/toolset-editor/package.json:1-41](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/package.json)
- [libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx) — `ToolsetEditor`
- [libs/toolset-editor/src/models/toolset-editor-props.ts:74-150](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/models/toolset-editor-props.ts) — `ToolsetEditorProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-usage-dashboard-01 — Usage dashboard

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-02 — When this library is useful

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-03 — Follow the ownership boundary

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)

## lib-usage-dashboard-04 — The public contract to start with

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-05 — A minimal workspace integration

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-10 — See preformatted usage data in context

- [libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx)
- [libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx)

## lib-usage-dashboard-06 — Wire a realistic host workflow

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-07 — Available customization

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`

## lib-usage-dashboard-08 — Find the integration and its checks

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`
- [apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx:1-264](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx)
- [libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx:1-267](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx)
- [libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx:1-517](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx)

## lib-usage-dashboard-09 — Constraints that affect integration

- [libs/usage-dashboard/README.md:1-425](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/README.md)
- [libs/usage-dashboard/src/index.ts:1-43](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/index.ts)
- [libs/usage-dashboard/package.json:1-42](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/package.json)
- [libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx) — `UsageLimitCard`
- [libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/models/usage-limit-card-props.ts) — `UsageLimitCardProps`
- [AGENTS.md:1-176](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md)
