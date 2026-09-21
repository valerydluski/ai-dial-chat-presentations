# Application source excerpts

Source fragments are cited in the application decks. They are abridged for explanation and are not standalone controllers. The following full source files contain imports, providers and decorators.

## apps/chat/src/server-api/api-client.ts

```typescript
import {
  AppConfigApi,
  ApplicationsApi,
  AuthApi,
  ClientChannelApi,
  Configuration,
  ConversationsApi,
  DeploymentsApi,
  ExternalServicesApi,
  FilesApi,
  HealthApi,
  OfflineCredentialsApi,
  PromptsApi,
  PublishApi,
  RateApi,
  ScheduledTasksApi,
  ShareApi,
  SkillsApi,
  ToolsetsApi,
  TranscriptionApi,
  UserApi,
  UserConfigApi,
} from '@epam/ai-dial-chat-api-client';
import type { Middleware } from '@epam/ai-dial-chat-api-client';
import {
  createCsrfMiddleware,
  createUnauthorizedMiddleware,
  type CsrfRefreshOutcome,
} from '@epam/ai-dial-chat-hooks';
import {
  CsrfRefreshStatus,
  UnauthorizedError,
  getCsrfToken,
  isInvalidCsrfErrorBody,
  notifyUnauthorized,
  refreshCsrfToken,
  setCsrfToken,
} from './base';

const csrfMiddleware = createCsrfMiddleware({ getCsrfToken, setCsrfToken });

/*
 * Adapts `base.ts`'s enum-based `CsrfRefreshResult` to the factory's
 * plain-literal `CsrfRefreshOutcome`, so `libs/chat-hooks` never needs to
 * import an app-owned enum.
 */
const refreshCsrfTokenOutcome = async (): Promise<CsrfRefreshOutcome> => {
  const result = await refreshCsrfToken();
  if (result.status === CsrfRefreshStatus.Ok) {
    return { status: 'ok', token: result.token };
  }
  return {
    status:
      result.status === CsrfRefreshStatus.Unauthorized
        ? 'unauthorized'
        : 'failed',
  };
};

const unauthorizedMiddleware = createUnauthorizedMiddleware({
  notifyUnauthorized,
  refreshCsrfToken: refreshCsrfTokenOutcome,
  isInvalidCsrfErrorBody,
  getCsrfToken,
  setCsrfToken,
  createUnauthorizedError: (url) => new UnauthorizedError(url),
});

const telemetryMiddleware: Middleware = {
  post: async (context) => {
    console.info(
      `[api] ${context.init.method ?? 'GET'} ${context.url} → ${context.response.status}`,
    );
    return context.response;
  },
};

export const createApiConfiguration = (): Configuration =>
  new Configuration({
    basePath: '',
    credentials: 'include',
    middleware: [csrfMiddleware, unauthorizedMiddleware, telemetryMiddleware],
  });

const config = createApiConfiguration();

export const applicationsApi = new ApplicationsApi(config);
export const appConfigApi = new AppConfigApi(config);
export const deploymentsApi = new DeploymentsApi(config);
export const userApi = new UserApi(config);
export const filesApi = new FilesApi(config);
export const conversationsApi = new ConversationsApi(config);
export const userConfigApi = new UserConfigApi(config);
export const authApi = new AuthApi(config);
export const rateApi = new RateApi(config);
export const toolsetsApi = new ToolsetsApi(config);
export const shareApi = new ShareApi(config);
export const skillsApi = new SkillsApi(config);
export const publishApi = new PublishApi(config);
export const promptsApi = new PromptsApi(config);
export const clientChannelApi = new ClientChannelApi(config);
export const scheduledTasksApi = new ScheduledTasksApi(config);
export const offlineCredentialsApi = new OfflineCredentialsApi(config);
export const externalServicesApi = new ExternalServicesApi(config);
export const healthApi = new HealthApi(config);
export const transcriptionApi = new TranscriptionApi(config);

```

## apps/chat/src/server-api/chat-stream.api.ts

```typescript
import { SendCompletionDtoModeEnum } from '@epam/ai-dial-chat-api-client';
import {
  createChatStreamApi,
  getBrowserTimezone,
} from '@epam/ai-dial-chat-hooks';
import { ApiEndpoints, getCsrfToken, setCsrfToken } from './base';

export { SendCompletionDtoModeEnum as CompletionMode };

const chatStreamApi = createChatStreamApi({
  getCsrfToken,
  setCsrfToken,
  completionsBasePath: ApiEndpoints.CONVERSATIONS,
  getTimezone: getBrowserTimezone,
});

export const { streamCompletion, stopCompletion } = chatStreamApi;

```

## apps/chat-api/src/chat/chat.controller.ts

```typescript
import { Body, Controller, Post, Req } from '@nestjs/common';
import { ApiBody, ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import type { Request } from 'express';
import type { SessionUser } from '../auth/session/session.types';
import { ChatCompletionResponseDto } from '../openapi/openapi-response.dto';
import { ChatService } from './chat.service';
import { ChatCompletionDto } from './dto/chat-completion.dto';

@ApiTags('chat')
@Controller({ path: 'chat', version: '1' })
export class ChatController {
  constructor(private readonly chatService: ChatService) {}

  @Post('completions')
  @ApiOperation({ summary: 'Send a chat completion request to DIAL Core' })
  @ApiBody({ type: ChatCompletionDto })
  @ApiResponse({
    status: 200,
    description: 'Chat completion response from DIAL Core',
    type: ChatCompletionResponseDto,
  })
  @ApiResponse({ status: 400, description: 'Invalid request body' })
  @ApiResponse({ status: 404, description: 'Deployment not found' })
  @ApiResponse({
    status: 502,
    description: 'Unexpected response from DIAL Core',
  })
  @ApiResponse({ status: 503, description: 'DIAL Core is unreachable' })
  sendCompletion(@Req() req: Request, @Body() dto: ChatCompletionDto) {
    const { at } = req.user as SessionUser;
    return this.chatService.sendCompletion(dto, at);
  }
}

```
