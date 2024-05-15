# Avis.ImageAttributeCategoryApi

All URIs are relative to _http://localhost:8000_

| Method                                                                                                      | HTTP request                                   | Description |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------- |
| [**imageAttributeCategoryCreate**](ImageAttributeCategoryApi.md#imageAttributeCategoryCreate)               | **POST** /api/image-attribute-category/        |
| [**imageAttributeCategoryDestroy**](ImageAttributeCategoryApi.md#imageAttributeCategoryDestroy)             | **DELETE** /api/image-attribute-category/{id}/ |
| [**imageAttributeCategoryList**](ImageAttributeCategoryApi.md#imageAttributeCategoryList)                   | **GET** /api/image-attribute-category/         |
| [**imageAttributeCategoryPartialUpdate**](ImageAttributeCategoryApi.md#imageAttributeCategoryPartialUpdate) | **PATCH** /api/image-attribute-category/{id}/  |
| [**imageAttributeCategoryRetrieve**](ImageAttributeCategoryApi.md#imageAttributeCategoryRetrieve)           | **GET** /api/image-attribute-category/{id}/    |
| [**imageAttributeCategoryUpdate**](ImageAttributeCategoryApi.md#imageAttributeCategoryUpdate)               | **PUT** /api/image-attribute-category/{id}/    |

## imageAttributeCategoryCreate

> ImageAttributeCategory imageAttributeCategoryCreate(imageAttributeCategoryRequest)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let imageAttributeCategoryRequest = new Avis.ImageAttributeCategoryRequest(); // ImageAttributeCategoryRequest |
apiInstance.imageAttributeCategoryCreate(
  imageAttributeCategoryRequest,
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

| Name                              | Type                                                                  | Description | Notes |
| --------------------------------- | --------------------------------------------------------------------- | ----------- | ----- |
| **imageAttributeCategoryRequest** | [**ImageAttributeCategoryRequest**](ImageAttributeCategoryRequest.md) |             |

### Return type

[**ImageAttributeCategory**](ImageAttributeCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## imageAttributeCategoryDestroy

> imageAttributeCategoryDestroy(id)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let id = 56; // Number | A unique integer value identifying this image attribute category.
apiInstance.imageAttributeCategoryDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                                       | Notes |
| ------ | ---------- | ----------------------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this image attribute category. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## imageAttributeCategoryList

> PaginatedImageAttributeCategoryList imageAttributeCategoryList(opts)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let opts = {
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.imageAttributeCategoryList(opts, (error, data, response) => {
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

[**PaginatedImageAttributeCategoryList**](PaginatedImageAttributeCategoryList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## imageAttributeCategoryPartialUpdate

> ImageAttributeCategory imageAttributeCategoryPartialUpdate(id, opts)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let id = 56; // Number | A unique integer value identifying this image attribute category.
let opts = {
  patchedImageAttributeCategoryRequest:
    new Avis.PatchedImageAttributeCategoryRequest(), // PatchedImageAttributeCategoryRequest |
};
apiInstance.imageAttributeCategoryPartialUpdate(
  id,
  opts,
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

| Name                                     | Type                                                                                | Description                                                       | Notes      |
| ---------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------- |
| **id**                                   | **Number**                                                                          | A unique integer value identifying this image attribute category. |
| **patchedImageAttributeCategoryRequest** | [**PatchedImageAttributeCategoryRequest**](PatchedImageAttributeCategoryRequest.md) |                                                                   | [optional] |

### Return type

[**ImageAttributeCategory**](ImageAttributeCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## imageAttributeCategoryRetrieve

> ImageAttributeCategory imageAttributeCategoryRetrieve(id, opts)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let id = 56; // Number | A unique integer value identifying this image attribute category.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.imageAttributeCategoryRetrieve(
  id,
  opts,
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

| Name       | Type       | Description                                                       | Notes      |
| ---------- | ---------- | ----------------------------------------------------------------- | ---------- |
| **id**     | **Number** | A unique integer value identifying this image attribute category. |
| **fields** | **String** |                                                                   | [optional] |

### Return type

[**ImageAttributeCategory**](ImageAttributeCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## imageAttributeCategoryUpdate

> ImageAttributeCategory imageAttributeCategoryUpdate(id, imageAttributeCategoryRequest)

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

let apiInstance = new Avis.ImageAttributeCategoryApi();
let id = 56; // Number | A unique integer value identifying this image attribute category.
let imageAttributeCategoryRequest = new Avis.ImageAttributeCategoryRequest(); // ImageAttributeCategoryRequest |
apiInstance.imageAttributeCategoryUpdate(
  id,
  imageAttributeCategoryRequest,
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

| Name                              | Type                                                                  | Description                                                       | Notes |
| --------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ----- |
| **id**                            | **Number**                                                            | A unique integer value identifying this image attribute category. |
| **imageAttributeCategoryRequest** | [**ImageAttributeCategoryRequest**](ImageAttributeCategoryRequest.md) |                                                                   |

### Return type

[**ImageAttributeCategory**](ImageAttributeCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
