# Avis.ProductApi

All URIs are relative to _http://localhost:8000_

| Method                                                         | HTTP request                  | Description |
| -------------------------------------------------------------- | ----------------------------- | ----------- |
| [**productCreate**](ProductApi.md#productCreate)               | **POST** /api/product/        |
| [**productDestroy**](ProductApi.md#productDestroy)             | **DELETE** /api/product/{id}/ |
| [**productList**](ProductApi.md#productList)                   | **GET** /api/product/         |
| [**productPartialUpdate**](ProductApi.md#productPartialUpdate) | **PATCH** /api/product/{id}/  |
| [**productRetrieve**](ProductApi.md#productRetrieve)           | **GET** /api/product/{id}/    |
| [**productUpdate**](ProductApi.md#productUpdate)               | **PUT** /api/product/{id}/    |

## productCreate

> Product productCreate(productRequest)

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

let apiInstance = new Avis.ProductApi();
let productRequest = new Avis.ProductRequest(); // ProductRequest |
apiInstance.productCreate(productRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name               | Type                                    | Description | Notes |
| ------------------ | --------------------------------------- | ----------- | ----- |
| **productRequest** | [**ProductRequest**](ProductRequest.md) |             |

### Return type

[**Product**](Product.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## productDestroy

> productDestroy(id)

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

let apiInstance = new Avis.ProductApi();
let id = 56; // Number | A unique integer value identifying this product.
apiInstance.productDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                      | Notes |
| ------ | ---------- | ------------------------------------------------ | ----- |
| **id** | **Number** | A unique integer value identifying this product. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## productList

> PaginatedProductList productList(opts)

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

let apiInstance = new Avis.ProductApi();
let opts = {
  category: [null], // [Number] | Multiple values may be separated by commas.
  fields: "fields_example", // String |
  id: [null], // [Number] | Multiple values may be separated by commas.
  identifier: ["null"], // [String] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.productList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name           | Type                      | Description                                    | Notes      |
| -------------- | ------------------------- | ---------------------------------------------- | ---------- |
| **category**   | [**[Number]**](Number.md) | Multiple values may be separated by commas.    | [optional] |
| **fields**     | **String**                |                                                | [optional] |
| **id**         | [**[Number]**](Number.md) | Multiple values may be separated by commas.    | [optional] |
| **identifier** | [**[String]**](String.md) | Multiple values may be separated by commas.    | [optional] |
| **ordering**   | **String**                | Which field to use when ordering the results.  | [optional] |
| **page**       | **Number**                | A page number within the paginated result set. | [optional] |
| **pageSize**   | **Number**                | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedProductList**](PaginatedProductList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## productPartialUpdate

> Product productPartialUpdate(id, opts)

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

let apiInstance = new Avis.ProductApi();
let id = 56; // Number | A unique integer value identifying this product.
let opts = {
  patchedProductRequest: new Avis.PatchedProductRequest(), // PatchedProductRequest |
};
apiInstance.productPartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                      | Type                                                  | Description                                      | Notes      |
| ------------------------- | ----------------------------------------------------- | ------------------------------------------------ | ---------- |
| **id**                    | **Number**                                            | A unique integer value identifying this product. |
| **patchedProductRequest** | [**PatchedProductRequest**](PatchedProductRequest.md) |                                                  | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## productRetrieve

> Product productRetrieve(id, opts)

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

let apiInstance = new Avis.ProductApi();
let id = 56; // Number | A unique integer value identifying this product.
let opts = {
  fields: "fields_example", // String |
};
apiInstance.productRetrieve(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name       | Type       | Description                                      | Notes      |
| ---------- | ---------- | ------------------------------------------------ | ---------- |
| **id**     | **Number** | A unique integer value identifying this product. |
| **fields** | **String** |                                                  | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## productUpdate

> Product productUpdate(id, productRequest)

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

let apiInstance = new Avis.ProductApi();
let id = 56; // Number | A unique integer value identifying this product.
let productRequest = new Avis.ProductRequest(); // ProductRequest |
apiInstance.productUpdate(id, productRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name               | Type                                    | Description                                      | Notes |
| ------------------ | --------------------------------------- | ------------------------------------------------ | ----- |
| **id**             | **Number**                              | A unique integer value identifying this product. |
| **productRequest** | [**ProductRequest**](ProductRequest.md) |                                                  |

### Return type

[**Product**](Product.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
