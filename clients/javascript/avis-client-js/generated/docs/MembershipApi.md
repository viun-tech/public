# ViunAvisClientJs.MembershipApi

All URIs are relative to _http://localhost:8000_

| Method                                                        | HTTP request                     | Description |
| ------------------------------------------------------------- | -------------------------------- | ----------- |
| [**membershipCreate**](MembershipApi.md#membershipCreate)     | **POST** /api/membership/        |
| [**membershipDestroy**](MembershipApi.md#membershipDestroy)   | **DELETE** /api/membership/{id}/ |
| [**membershipList**](MembershipApi.md#membershipList)         | **GET** /api/membership/         |
| [**membershipRetrieve**](MembershipApi.md#membershipRetrieve) | **GET** /api/membership/{id}/    |
| [**membershipUpdate**](MembershipApi.md#membershipUpdate)     | **PUT** /api/membership/{id}/    |

## membershipCreate

> Membership membershipCreate(membershipRequest)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import ViunAvisClientJs from "@viun/avis-client-js";
let defaultClient = ViunAvisClientJs.ApiClient.instance;
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

let apiInstance = new ViunAvisClientJs.MembershipApi();
let membershipRequest = new ViunAvisClientJs.MembershipRequest(); // MembershipRequest |
apiInstance.membershipCreate(membershipRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                  | Type                                          | Description | Notes |
| --------------------- | --------------------------------------------- | ----------- | ----- |
| **membershipRequest** | [**MembershipRequest**](MembershipRequest.md) |             |

### Return type

[**Membership**](Membership.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## membershipDestroy

> membershipDestroy(id)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import ViunAvisClientJs from "@viun/avis-client-js";
let defaultClient = ViunAvisClientJs.ApiClient.instance;
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

let apiInstance = new ViunAvisClientJs.MembershipApi();
let id = 56; // Number | A unique integer value identifying this membership.
apiInstance.membershipDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                         | Notes |
| ------ | ---------- | --------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this membership. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## membershipList

> PaginatedMembershipList membershipList(opts)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import ViunAvisClientJs from "@viun/avis-client-js";
let defaultClient = ViunAvisClientJs.ApiClient.instance;
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

let apiInstance = new ViunAvisClientJs.MembershipApi();
let opts = {
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.membershipList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name         | Type       | Description                                    | Notes      |
| ------------ | ---------- | ---------------------------------------------- | ---------- |
| **page**     | **Number** | A page number within the paginated result set. | [optional] |
| **pageSize** | **Number** | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedMembershipList**](PaginatedMembershipList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## membershipRetrieve

> Membership membershipRetrieve(id)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import ViunAvisClientJs from "@viun/avis-client-js";
let defaultClient = ViunAvisClientJs.ApiClient.instance;
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

let apiInstance = new ViunAvisClientJs.MembershipApi();
let id = 56; // Number | A unique integer value identifying this membership.
apiInstance.membershipRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                         | Notes |
| ------ | ---------- | --------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this membership. |

### Return type

[**Membership**](Membership.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## membershipUpdate

> Membership membershipUpdate(id, membershipRequest)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import ViunAvisClientJs from "@viun/avis-client-js";
let defaultClient = ViunAvisClientJs.ApiClient.instance;
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

let apiInstance = new ViunAvisClientJs.MembershipApi();
let id = 56; // Number | A unique integer value identifying this membership.
let membershipRequest = new ViunAvisClientJs.MembershipRequest(); // MembershipRequest |
apiInstance.membershipUpdate(id, membershipRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                  | Type                                          | Description                                         | Notes |
| --------------------- | --------------------------------------------- | --------------------------------------------------- | ----- |
| **id**                | **Number**                                    | A unique integer value identifying this membership. |
| **membershipRequest** | [**MembershipRequest**](MembershipRequest.md) |                                                     |

### Return type

[**Membership**](Membership.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
