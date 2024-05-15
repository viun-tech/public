# ViunAvisClientJs.QualityCriteriaApi

All URIs are relative to _http://localhost:8000_

| Method                                                                                 | HTTP request                           | Description |
| -------------------------------------------------------------------------------------- | -------------------------------------- | ----------- |
| [**qualityCriteriaCreate**](QualityCriteriaApi.md#qualityCriteriaCreate)               | **POST** /api/quality-criteria/        |
| [**qualityCriteriaDestroy**](QualityCriteriaApi.md#qualityCriteriaDestroy)             | **DELETE** /api/quality-criteria/{id}/ |
| [**qualityCriteriaList**](QualityCriteriaApi.md#qualityCriteriaList)                   | **GET** /api/quality-criteria/         |
| [**qualityCriteriaPartialUpdate**](QualityCriteriaApi.md#qualityCriteriaPartialUpdate) | **PATCH** /api/quality-criteria/{id}/  |
| [**qualityCriteriaRetrieve**](QualityCriteriaApi.md#qualityCriteriaRetrieve)           | **GET** /api/quality-criteria/{id}/    |
| [**qualityCriteriaUpdate**](QualityCriteriaApi.md#qualityCriteriaUpdate)               | **PUT** /api/quality-criteria/{id}/    |

## qualityCriteriaCreate

> QualityCriteria qualityCriteriaCreate(qualityCriteriaRequest)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let qualityCriteriaRequest = new ViunAvisClientJs.QualityCriteriaRequest(); // QualityCriteriaRequest |
apiInstance.qualityCriteriaCreate(
  qualityCriteriaRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                       | Type                                                    | Description | Notes |
| -------------------------- | ------------------------------------------------------- | ----------- | ----- |
| **qualityCriteriaRequest** | [**QualityCriteriaRequest**](QualityCriteriaRequest.md) |             |

### Return type

[**QualityCriteria**](QualityCriteria.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## qualityCriteriaDestroy

> qualityCriteriaDestroy(id)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let id = 56; // Number | A unique integer value identifying this quality criteria.
apiInstance.qualityCriteriaDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                               | Notes |
| ------ | ---------- | --------------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this quality criteria. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## qualityCriteriaList

> PaginatedQualityCriteriaList qualityCriteriaList(opts)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let opts = {
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.qualityCriteriaList(opts, (error, data, response) => {
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

[**PaginatedQualityCriteriaList**](PaginatedQualityCriteriaList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## qualityCriteriaPartialUpdate

> QualityCriteria qualityCriteriaPartialUpdate(id, opts)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let id = 56; // Number | A unique integer value identifying this quality criteria.
let opts = {
  patchedQualityCriteriaRequest:
    new ViunAvisClientJs.PatchedQualityCriteriaRequest(), // PatchedQualityCriteriaRequest |
};
apiInstance.qualityCriteriaPartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                              | Type                                                                  | Description                                               | Notes      |
| --------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------- | ---------- |
| **id**                            | **Number**                                                            | A unique integer value identifying this quality criteria. |
| **patchedQualityCriteriaRequest** | [**PatchedQualityCriteriaRequest**](PatchedQualityCriteriaRequest.md) |                                                           | [optional] |

### Return type

[**QualityCriteria**](QualityCriteria.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## qualityCriteriaRetrieve

> QualityCriteria qualityCriteriaRetrieve(id, opts)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let id = 56; // Number | A unique integer value identifying this quality criteria.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.qualityCriteriaRetrieve(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name       | Type       | Description                                               | Notes      |
| ---------- | ---------- | --------------------------------------------------------- | ---------- |
| **id**     | **Number** | A unique integer value identifying this quality criteria. |
| **fields** | **String** |                                                           | [optional] |

### Return type

[**QualityCriteria**](QualityCriteria.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## qualityCriteriaUpdate

> QualityCriteria qualityCriteriaUpdate(id, qualityCriteriaRequest)

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

let apiInstance = new ViunAvisClientJs.QualityCriteriaApi();
let id = 56; // Number | A unique integer value identifying this quality criteria.
let qualityCriteriaRequest = new ViunAvisClientJs.QualityCriteriaRequest(); // QualityCriteriaRequest |
apiInstance.qualityCriteriaUpdate(
  id,
  qualityCriteriaRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                       | Type                                                    | Description                                               | Notes |
| -------------------------- | ------------------------------------------------------- | --------------------------------------------------------- | ----- |
| **id**                     | **Number**                                              | A unique integer value identifying this quality criteria. |
| **qualityCriteriaRequest** | [**QualityCriteriaRequest**](QualityCriteriaRequest.md) |                                                           |

### Return type

[**QualityCriteria**](QualityCriteria.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
