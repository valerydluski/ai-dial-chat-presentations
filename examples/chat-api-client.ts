import { Configuration, DeploymentsApi } from '@epam/ai-dial-chat-api-client';

/* Run from an authenticated host page against a running chat-api. */
export function createDemoApi() {
  return new DeploymentsApi(new Configuration({ basePath: '', credentials: 'include' }));
}
export async function listDemoDeployments() {
  const api = createDemoApi();
  return await api.listDeployments();
}
export async function readDemoHeaders() {
  const response = await createDemoApi().listDeploymentsRaw({});
  return { status: response.raw.status, data: await response.value() };
}
