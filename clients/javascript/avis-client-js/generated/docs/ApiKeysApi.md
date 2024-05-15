# Avis.ApiKeysApi

All URIs are relative to _http://localhost:8000_

| Method                                                 | HTTP request               | Description |
| ------------------------------------------------------ | -------------------------- | ----------- |
| [**keysCreate**](ApiKeysApi.md#keysCreate)             | **POST** /api/keys/        |
| [**keysRevokeCreate**](ApiKeysApi.md#keysRevokeCreate) | **POST** /api/keys/revoke/ |

## keysCreate

> UserAPIKeyCreate keysCreate(opts)

Create a new API key for the current user.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.ApiKeysApi();
let opts = {
  userAPIKeyCreateRequest: new Avis.UserAPIKeyCreateRequest(), // UserAPIKeyCreateRequest |
};
apiInstance.keysCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                        | Type                                                      | Description | Notes      |
| --------------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **userAPIKeyCreateRequest** | [**UserAPIKeyCreateRequest**](UserAPIKeyCreateRequest.md) |             | [optional] |

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## keysRevokeCreate

> UserAPIKeyCreate keysRevokeCreate(opts)

Revoke an API key for the current user. We use the name of the API Key to revoke it, not the ID or actual key to prevent information leakage.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.ApiKeysApi();
let opts = {
  userAPIKeyCreateRequest: new Avis.UserAPIKeyCreateRequest(), // UserAPIKeyCreateRequest |
};
apiInstance.keysRevokeCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                        | Type                                                      | Description | Notes      |
| --------------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **userAPIKeyCreateRequest** | [**UserAPIKeyCreateRequest**](UserAPIKeyCreateRequest.md) |             | [optional] |

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
