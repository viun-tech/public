# Avis.MlApi

All URIs are relative to _http://localhost:8000_

| Method                                                            | HTTP request                        | Description |
| ----------------------------------------------------------------- | ----------------------------------- | ----------- |
| [**mlModelCreate**](MlApi.md#mlModelCreate)                       | **POST** /api/ml/model/             |
| [**mlModelDestroy**](MlApi.md#mlModelDestroy)                     | **DELETE** /api/ml/model/{id}/      |
| [**mlModelInference**](MlApi.md#mlModelInference)                 | **POST** /api/ml/model/{id}/infer/  |
| [**mlModelList**](MlApi.md#mlModelList)                           | **GET** /api/ml/model/              |
| [**mlModelPartialUpdate**](MlApi.md#mlModelPartialUpdate)         | **PATCH** /api/ml/model/{id}/       |
| [**mlModelRetrieve**](MlApi.md#mlModelRetrieve)                   | **GET** /api/ml/model/{id}/         |
| [**mlModelTypeCreate**](MlApi.md#mlModelTypeCreate)               | **POST** /api/ml/model-type/        |
| [**mlModelTypeDestroy**](MlApi.md#mlModelTypeDestroy)             | **DELETE** /api/ml/model-type/{id}/ |
| [**mlModelTypeList**](MlApi.md#mlModelTypeList)                   | **GET** /api/ml/model-type/         |
| [**mlModelTypePartialUpdate**](MlApi.md#mlModelTypePartialUpdate) | **PATCH** /api/ml/model-type/{id}/  |
| [**mlModelTypeRetrieve**](MlApi.md#mlModelTypeRetrieve)           | **GET** /api/ml/model-type/{id}/    |
| [**mlModelTypeUpdate**](MlApi.md#mlModelTypeUpdate)               | **PUT** /api/ml/model-type/{id}/    |
| [**mlModelUpdate**](MlApi.md#mlModelUpdate)                       | **PUT** /api/ml/model/{id}/         |

## mlModelCreate

> MLModel mlModelCreate(mLModelRequest)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let mLModelRequest = new Avis.MLModelRequest(); // MLModelRequest |
apiInstance.mlModelCreate(mLModelRequest, (error, data, response) => {
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
| **mLModelRequest** | [**MLModelRequest**](MLModelRequest.md) |             |

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelDestroy

> mlModelDestroy(id)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model.
apiInstance.mlModelDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                       | Notes |
| ------ | ---------- | ------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this ml model. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## mlModelInference

> MLModel mlModelInference(id, azureMLInferenceRequest)

Infer a result from the model. This is a passthrough to the model&#39;s inference endpoint running somewhere else. The request body is passed through to the model.

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model.
let azureMLInferenceRequest = new Avis.AzureMLInferenceRequest(); // AzureMLInferenceRequest |
apiInstance.mlModelInference(
  id,
  azureMLInferenceRequest,
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

| Name                        | Type                                                      | Description                                       | Notes |
| --------------------------- | --------------------------------------------------------- | ------------------------------------------------- | ----- |
| **id**                      | **Number**                                                | A unique integer value identifying this ml model. |
| **azureMLInferenceRequest** | [**AzureMLInferenceRequest**](AzureMLInferenceRequest.md) |                                                   |

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelList

> PaginatedMLModelList mlModelList(opts)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let opts = {
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.mlModelList(opts, (error, data, response) => {
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

[**PaginatedMLModelList**](PaginatedMLModelList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## mlModelPartialUpdate

> MLModel mlModelPartialUpdate(id, opts)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model.
let opts = {
  patchedMLModelRequest: new Avis.PatchedMLModelRequest(), // PatchedMLModelRequest |
};
apiInstance.mlModelPartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                      | Type                                                  | Description                                       | Notes      |
| ------------------------- | ----------------------------------------------------- | ------------------------------------------------- | ---------- |
| **id**                    | **Number**                                            | A unique integer value identifying this ml model. |
| **patchedMLModelRequest** | [**PatchedMLModelRequest**](PatchedMLModelRequest.md) |                                                   | [optional] |

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelRetrieve

> MLModel mlModelRetrieve(id)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model.
apiInstance.mlModelRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                       | Notes |
| ------ | ---------- | ------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this ml model. |

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## mlModelTypeCreate

> MLModelType mlModelTypeCreate(opts)

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

let apiInstance = new Avis.MlApi();
let opts = {
  mLModelTypeRequest: new Avis.MLModelTypeRequest(), // MLModelTypeRequest |
};
apiInstance.mlModelTypeCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                   | Type                                            | Description | Notes      |
| ---------------------- | ----------------------------------------------- | ----------- | ---------- |
| **mLModelTypeRequest** | [**MLModelTypeRequest**](MLModelTypeRequest.md) |             | [optional] |

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelTypeDestroy

> mlModelTypeDestroy(id)

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model type.
apiInstance.mlModelTypeDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                            | Notes |
| ------ | ---------- | ------------------------------------------------------ | ----- |
| **id** | **Number** | A unique integer value identifying this ml model type. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## mlModelTypeList

> PaginatedMLModelTypeList mlModelTypeList(opts)

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

let apiInstance = new Avis.MlApi();
let opts = {
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.mlModelTypeList(opts, (error, data, response) => {
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

[**PaginatedMLModelTypeList**](PaginatedMLModelTypeList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## mlModelTypePartialUpdate

> MLModelType mlModelTypePartialUpdate(id, opts)

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model type.
let opts = {
  patchedMLModelTypeRequest: new Avis.PatchedMLModelTypeRequest(), // PatchedMLModelTypeRequest |
};
apiInstance.mlModelTypePartialUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                          | Type                                                          | Description                                            | Notes      |
| ----------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ | ---------- |
| **id**                        | **Number**                                                    | A unique integer value identifying this ml model type. |
| **patchedMLModelTypeRequest** | [**PatchedMLModelTypeRequest**](PatchedMLModelTypeRequest.md) |                                                        | [optional] |

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelTypeRetrieve

> MLModelType mlModelTypeRetrieve(id)

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model type.
apiInstance.mlModelTypeRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                            | Notes |
| ------ | ---------- | ------------------------------------------------------ | ----- |
| **id** | **Number** | A unique integer value identifying this ml model type. |

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## mlModelTypeUpdate

> MLModelType mlModelTypeUpdate(id, opts)

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model type.
let opts = {
  mLModelTypeRequest: new Avis.MLModelTypeRequest(), // MLModelTypeRequest |
};
apiInstance.mlModelTypeUpdate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name                   | Type                                            | Description                                            | Notes      |
| ---------------------- | ----------------------------------------------- | ------------------------------------------------------ | ---------- |
| **id**                 | **Number**                                      | A unique integer value identifying this ml model type. |
| **mLModelTypeRequest** | [**MLModelTypeRequest**](MLModelTypeRequest.md) |                                                        | [optional] |

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## mlModelUpdate

> MLModel mlModelUpdate(id, mLModelRequest)

A viewset for ML models. It filters results based on the permissions granted to all the user&#39;s team(s). A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

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

let apiInstance = new Avis.MlApi();
let id = 56; // Number | A unique integer value identifying this ml model.
let mLModelRequest = new Avis.MLModelRequest(); // MLModelRequest |
apiInstance.mlModelUpdate(id, mLModelRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name               | Type                                    | Description                                       | Notes |
| ------------------ | --------------------------------------- | ------------------------------------------------- | ----- |
| **id**             | **Number**                              | A unique integer value identifying this ml model. |
| **mLModelRequest** | [**MLModelRequest**](MLModelRequest.md) |                                                   |

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
