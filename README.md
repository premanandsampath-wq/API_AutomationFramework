# API Client Workflow

This document explains the workflow for `scr/core/API_Client.py` in the `API_Basic` project.

## Purpose

`API_Client.py` provides a simple reusable HTTP client for the project. It encapsulates:

- base URL and endpoint configuration
- retry behavior for network requests
- GET and POST request methods

## File path

`c:\Users\prema\Python_API_Project\API_Basic\scr\core\API_Client.py`

## How it works

1. The `APIClient` class is initialized with:
   - `baseurl`: default from `scr.config.config.BASE_URL`
   - `endpoint`: default from `scr.config.config.AUTH_ENDPOINT`
   - `retries`: number of retry attempts for failed requests
   - `delay`: delay in seconds between retries

2. The client builds a request URL by concatenating `baseurl` and `endpoint`.

3. The `retry_request` method executes the request and retries when the response status code is not `200`.

4. The request methods return the `requests.Response` object on success.

## Class and methods

### `APIClient`

Constructor parameters:

- `baseurl` - base API URL
- `endpoint` - API endpoint path
- `retries` - number of retry attempts
- `delay` - wait time between retry attempts

### `retry_request(method, url, **kwargs)`

- Sends a request using `requests.request`
- Retries until a successful `200` response or until retries are exhausted
- Raises an exception on final failure

### `get(headers=None)`

- Builds the full URL
- Sends a GET request
- Returns the `Response` object

### `post(data=None)`

- Builds the full URL
- Sends a POST request with JSON payload
- Returns the `Response` object

## Example usage

```python
from scr.core.API_Client import APIClient

client = APIClient(baseurl="https://dummyjson.com", endpoint="/auth/login")
response = client.post(data={"username": "emilys", "password": "emilyspass"})
print(response.status_code)
print(response.json())
```

## Notes

- This client assumes the API returns `200` on success.
- If the service returns a different success status code, the retry logic will treat it as failure.
- Make sure `scr.config.config` provides valid `BASE_URL` and endpoint values.
