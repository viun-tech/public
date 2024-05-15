# ViunAvisClientJs.ProductCategoryApi

All URIs are relative to _http://localhost:8000_

| Method                                                                                 | HTTP request                           | Description |
| -------------------------------------------------------------------------------------- | -------------------------------------- | ----------- |
| [**productCategoryCreate**](ProductCategoryApi.md#productCategoryCreate)               | **POST** /api/product-category/        |
| [**productCategoryDestroy**](ProductCategoryApi.md#productCategoryDestroy)             | **DELETE** /api/product-category/{id}/ |
| [**productCategoryList**](ProductCategoryApi.md#productCategoryList)                   | **GET** /api/product-category/         |
| [**productCategoryPartialUpdate**](ProductCategoryApi.md#productCategoryPartialUpdate) | **PATCH** /api/product-category/{id}/  |
| [**productCategoryRetrieve**](ProductCategoryApi.md#productCategoryRetrieve)           | **GET** /api/product-category/{id}/    |
| [**productCategoryUpdate**](ProductCategoryApi.md#productCategoryUpdate)               | **PUT** /api/product-category/{id}/    |

## productCategoryCreate

> ProductCategory productCategoryCreate(productCategoryRequest)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let productCategoryRequest = new ViunAvisClientJs.ProductCategoryRequest(); // ProductCategoryRequest |
apiInstance.productCategoryCreate(
  productCategoryRequest,
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
| **productCategoryRequest** | [**ProductCategoryRequest**](ProductCategoryRequest.md) |             |

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## productCategoryDestroy

> productCategoryDestroy(id)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let id = 56; // Number | A unique integer value identifying this product category.
apiInstance.productCategoryDestroy(id, (error, data, response) => {
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
| **id** | **Number** | A unique integer value identifying this product category. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## productCategoryList

> PaginatedProductCategoryList productCategoryList(opts)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let opts = {
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.productCategoryList(opts, (error, data, response) => {
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

[**PaginatedProductCategoryList**](PaginatedProductCategoryList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## productCategoryPartialUpdate

> ProductCategory productCategoryPartialUpdate(id, opts)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let id = 56; // Number | A unique integer value identifying this product category.
let opts = {
  patchedProductCategoryRequest:
    new ViunAvisClientJs.PatchedProductCategoryRequest(), // PatchedProductCategoryRequest |
};
apiInstance.productCategoryPartialUpdate(id, opts, (error, data, response) => {
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
| **id**                            | **Number**                                                            | A unique integer value identifying this product category. |
| **patchedProductCategoryRequest** | [**PatchedProductCategoryRequest**](PatchedProductCategoryRequest.md) |                                                           | [optional] |

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## productCategoryRetrieve

> ProductCategory productCategoryRetrieve(id, opts)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let id = 56; // Number | A unique integer value identifying this product category.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.productCategoryRetrieve(id, opts, (error, data, response) => {
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
| **id**     | **Number** | A unique integer value identifying this product category. |
| **fields** | **String** |                                                           | [optional] |

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## productCategoryUpdate

> ProductCategory productCategoryUpdate(id, productCategoryRequest)

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

let apiInstance = new ViunAvisClientJs.ProductCategoryApi();
let id = 56; // Number | A unique integer value identifying this product category.
let productCategoryRequest = new ViunAvisClientJs.ProductCategoryRequest(); // ProductCategoryRequest |
apiInstance.productCategoryUpdate(
  id,
  productCategoryRequest,
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
| **id**                     | **Number**                                              | A unique integer value identifying this product category. |
| **productCategoryRequest** | [**ProductCategoryRequest**](ProductCategoryRequest.md) |                                                           |

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
