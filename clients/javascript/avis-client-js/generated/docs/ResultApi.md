# ViunAvisClientJs.ResultApi

All URIs are relative to _http://localhost:8000_

| Method                                                      | HTTP request                 | Description |
| ----------------------------------------------------------- | ---------------------------- | ----------- |
| [**resultCreate**](ResultApi.md#resultCreate)               | **POST** /api/result/        |
| [**resultDestroy**](ResultApi.md#resultDestroy)             | **DELETE** /api/result/{id}/ |
| [**resultList**](ResultApi.md#resultList)                   | **GET** /api/result/         |
| [**resultPartialUpdate**](ResultApi.md#resultPartialUpdate) | **PATCH** /api/result/{id}/  |
| [**resultRetrieve**](ResultApi.md#resultRetrieve)           | **GET** /api/result/{id}/    |
| [**resultUpdate**](ResultApi.md#resultUpdate)               | **PUT** /api/result/{id}/    |

## resultCreate

> Result resultCreate(resultRequest)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let resultRequest = new ViunAvisClientJs.ResultRequest(); // ResultRequest |
apiInstance.resultCreate(resultRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name              | Type                                  | Description | Notes |
| ----------------- | ------------------------------------- | ----------- | ----- |
| **resultRequest** | [**ResultRequest**](ResultRequest.md) |             |

### Return type

[**Result**](Result.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## resultDestroy

> resultDestroy(id)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let id = 56; // Number | A unique integer value identifying this result.
apiInstance.resultDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                     | Notes |
| ------ | ---------- | ----------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this result. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## resultList

> PaginatedResultList resultList(opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let opts = {
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.resultList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name         | Type                      | Description                                    | Notes      |
| ------------ | ------------------------- | ---------------------------------------------- | ---------- |
| **fields**   | **String**                |                                                | [optional] |
| **id**       | [**[Number]**](Number.md) | Multiple values may be separated by commas.    | [optional] |
| **ordering** | **String**                | Which field to use when ordering the results.  | [optional] |
| **page**     | **Number**                | A page number within the paginated result set. | [optional] |
| **pageSize** | **Number**                | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedResultList**](PaginatedResultList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## resultPartialUpdate

> Result resultPartialUpdate(id, opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let id = 56; // Number | A unique integer value identifying this result.
let opts = {
  patchedResultRequest: new ViunAvisClientJs.PatchedResultRequest(), // PatchedResultRequest |
};
apiInstance.resultPartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                     | Type                                                | Description                                     | Notes      |
| ------------------------ | --------------------------------------------------- | ----------------------------------------------- | ---------- |
| **id**                   | **Number**                                          | A unique integer value identifying this result. |
| **patchedResultRequest** | [**PatchedResultRequest**](PatchedResultRequest.md) |                                                 | [optional] |

### Return type

[**Result**](Result.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## resultRetrieve

> Result resultRetrieve(id, opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let id = 56; // Number | A unique integer value identifying this result.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.resultRetrieve(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name       | Type       | Description                                     | Notes      |
| ---------- | ---------- | ----------------------------------------------- | ---------- |
| **id**     | **Number** | A unique integer value identifying this result. |
| **fields** | **String** |                                                 | [optional] |

### Return type

[**Result**](Result.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## resultUpdate

> Result resultUpdate(id, resultRequest)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new ViunAvisClientJs.ResultApi();
let id = 56; // Number | A unique integer value identifying this result.
let resultRequest = new ViunAvisClientJs.ResultRequest(); // ResultRequest |
apiInstance.resultUpdate(id, resultRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name              | Type                                  | Description                                     | Notes |
| ----------------- | ------------------------------------- | ----------------------------------------------- | ----- |
| **id**            | **Number**                            | A unique integer value identifying this result. |
| **resultRequest** | [**ResultRequest**](ResultRequest.md) |                                                 |

### Return type

[**Result**](Result.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
