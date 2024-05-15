# Avis.ImageAttributeApi

All URIs are relative to _http://localhost:8000_

| Method                                                                              | HTTP request                          | Description |
| ----------------------------------------------------------------------------------- | ------------------------------------- | ----------- |
| [**imageAttributeCreate**](ImageAttributeApi.md#imageAttributeCreate)               | **POST** /api/image-attribute/        |
| [**imageAttributeDestroy**](ImageAttributeApi.md#imageAttributeDestroy)             | **DELETE** /api/image-attribute/{id}/ |
| [**imageAttributeList**](ImageAttributeApi.md#imageAttributeList)                   | **GET** /api/image-attribute/         |
| [**imageAttributePartialUpdate**](ImageAttributeApi.md#imageAttributePartialUpdate) | **PATCH** /api/image-attribute/{id}/  |
| [**imageAttributeRetrieve**](ImageAttributeApi.md#imageAttributeRetrieve)           | **GET** /api/image-attribute/{id}/    |
| [**imageAttributeUpdate**](ImageAttributeApi.md#imageAttributeUpdate)               | **PUT** /api/image-attribute/{id}/    |

## imageAttributeCreate

> ImageAttribute imageAttributeCreate(imageAttributeRequest)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let imageAttributeRequest = new Avis.ImageAttributeRequest(); // ImageAttributeRequest |
apiInstance.imageAttributeCreate(
  imageAttributeRequest,
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

| Name                      | Type                                                  | Description | Notes |
| ------------------------- | ----------------------------------------------------- | ----------- | ----- |
| **imageAttributeRequest** | [**ImageAttributeRequest**](ImageAttributeRequest.md) |             |

### Return type

[**ImageAttribute**](ImageAttribute.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## imageAttributeDestroy

> imageAttributeDestroy(id)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let id = 56; // Number | A unique integer value identifying this image attribute.
apiInstance.imageAttributeDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                              | Notes |
| ------ | ---------- | -------------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this image attribute. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## imageAttributeList

> PaginatedImageAttributeList imageAttributeList(opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let opts = {
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.imageAttributeList(opts, (error, data, response) => {
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

[**PaginatedImageAttributeList**](PaginatedImageAttributeList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## imageAttributePartialUpdate

> ImageAttribute imageAttributePartialUpdate(id, opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let id = 56; // Number | A unique integer value identifying this image attribute.
let opts = {
  patchedImageAttributeRequest: new Avis.PatchedImageAttributeRequest(), // PatchedImageAttributeRequest |
};
apiInstance.imageAttributePartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                             | Type                                                                | Description                                              | Notes      |
| -------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- | ---------- |
| **id**                           | **Number**                                                          | A unique integer value identifying this image attribute. |
| **patchedImageAttributeRequest** | [**PatchedImageAttributeRequest**](PatchedImageAttributeRequest.md) |                                                          | [optional] |

### Return type

[**ImageAttribute**](ImageAttribute.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## imageAttributeRetrieve

> ImageAttribute imageAttributeRetrieve(id, opts)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let id = 56; // Number | A unique integer value identifying this image attribute.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.imageAttributeRetrieve(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name       | Type       | Description                                              | Notes      |
| ---------- | ---------- | -------------------------------------------------------- | ---------- |
| **id**     | **Number** | A unique integer value identifying this image attribute. |
| **fields** | **String** |                                                          | [optional] |

### Return type

[**ImageAttribute**](ImageAttribute.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## imageAttributeUpdate

> ImageAttribute imageAttributeUpdate(id, imageAttributeRequest)

A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: _ CreateModelMixin: allows creating objects _ UpdateModelMixin: allows updating objects _ DestroyModelMixin: allows deleting objects _ OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the &#x60;fields&#x60; query parameter)

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

let apiInstance = new Avis.ImageAttributeApi();
let id = 56; // Number | A unique integer value identifying this image attribute.
let imageAttributeRequest = new Avis.ImageAttributeRequest(); // ImageAttributeRequest |
apiInstance.imageAttributeUpdate(
  id,
  imageAttributeRequest,
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

| Name                      | Type                                                  | Description                                              | Notes |
| ------------------------- | ----------------------------------------------------- | -------------------------------------------------------- | ----- |
| **id**                    | **Number**                                            | A unique integer value identifying this image attribute. |
| **imageAttributeRequest** | [**ImageAttributeRequest**](ImageAttributeRequest.md) |                                                          |

### Return type

[**ImageAttribute**](ImageAttribute.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
