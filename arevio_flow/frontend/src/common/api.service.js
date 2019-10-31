import { CSRF_TOKEN } from "./csrf_token.js"

function handleResponse(response) {
  if (response.ok && response.status != 204) {
    return response.json();
  }
  return null;
}

function apiService(endpoint, method, data) {
  // D.R.Y. code to make HTTP requests to the REST API backend using fetch
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      'content-type': 'application/json',
      'X-CSRFTOKEN': CSRF_TOKEN
    }
  };
  return fetch(endpoint, config)
           .then(handleResponse)
}

export { apiService };
