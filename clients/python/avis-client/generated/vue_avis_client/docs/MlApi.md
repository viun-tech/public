# vue_avis_client.MlApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ml_inspectionresult_create**](MlApi.md#ml_inspectionresult_create) | **POST** /api/ml/inspectionresult/ | 
[**ml_inspectionresult_destroy**](MlApi.md#ml_inspectionresult_destroy) | **DELETE** /api/ml/inspectionresult/{id}/ | 
[**ml_inspectionresult_list**](MlApi.md#ml_inspectionresult_list) | **GET** /api/ml/inspectionresult/ | 
[**ml_inspectionresult_partial_update**](MlApi.md#ml_inspectionresult_partial_update) | **PATCH** /api/ml/inspectionresult/{id}/ | 
[**ml_inspectionresult_retrieve**](MlApi.md#ml_inspectionresult_retrieve) | **GET** /api/ml/inspectionresult/{id}/ | 
[**ml_inspectionresult_update**](MlApi.md#ml_inspectionresult_update) | **PUT** /api/ml/inspectionresult/{id}/ | 
[**ml_model_create**](MlApi.md#ml_model_create) | **POST** /api/ml/model/ | 
[**ml_model_destroy**](MlApi.md#ml_model_destroy) | **DELETE** /api/ml/model/{id}/ | 
[**ml_model_inference**](MlApi.md#ml_model_inference) | **POST** /api/ml/model/{id}/inference/ | 
[**ml_model_list**](MlApi.md#ml_model_list) | **GET** /api/ml/model/ | 
[**ml_model_partial_update**](MlApi.md#ml_model_partial_update) | **PATCH** /api/ml/model/{id}/ | 
[**ml_model_retrieve**](MlApi.md#ml_model_retrieve) | **GET** /api/ml/model/{id}/ | 
[**ml_model_update**](MlApi.md#ml_model_update) | **PUT** /api/ml/model/{id}/ | 
[**ml_modeltype_create**](MlApi.md#ml_modeltype_create) | **POST** /api/ml/modeltype/ | 
[**ml_modeltype_destroy**](MlApi.md#ml_modeltype_destroy) | **DELETE** /api/ml/modeltype/{id}/ | 
[**ml_modeltype_list**](MlApi.md#ml_modeltype_list) | **GET** /api/ml/modeltype/ | 
[**ml_modeltype_partial_update**](MlApi.md#ml_modeltype_partial_update) | **PATCH** /api/ml/modeltype/{id}/ | 
[**ml_modeltype_retrieve**](MlApi.md#ml_modeltype_retrieve) | **GET** /api/ml/modeltype/{id}/ | 
[**ml_modeltype_update**](MlApi.md#ml_modeltype_update) | **PUT** /api/ml/modeltype/{id}/ | 


# **ml_inspectionresult_create**
> ClassificationResult ml_inspectionresult_create(classification_result_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.classification_result import ClassificationResult
from vue_avis_client.models.classification_result_request import ClassificationResultRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    classification_result_request = vue_avis_client.ClassificationResultRequest() # ClassificationResultRequest | 

    try:
        api_response = api_instance.ml_inspectionresult_create(classification_result_request)
        print("The response of MlApi->ml_inspectionresult_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_result_request** | [**ClassificationResultRequest**](ClassificationResultRequest.md)|  | 

### Return type

[**ClassificationResult**](ClassificationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_inspectionresult_destroy**
> ml_inspectionresult_destroy(id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this classification result.

    try:
        api_instance.ml_inspectionresult_destroy(id)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this classification result. | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_inspectionresult_list**
> List[ClassificationResult] ml_inspectionresult_list(fields=fields, id=id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.classification_result import ClassificationResult
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    fields = 'fields_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.ml_inspectionresult_list(fields=fields, id=id)
        print("The response of MlApi->ml_inspectionresult_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 

### Return type

[**List[ClassificationResult]**](ClassificationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_inspectionresult_partial_update**
> ClassificationResult ml_inspectionresult_partial_update(id, patched_classification_result_request=patched_classification_result_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.classification_result import ClassificationResult
from vue_avis_client.models.patched_classification_result_request import PatchedClassificationResultRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this classification result.
    patched_classification_result_request = vue_avis_client.PatchedClassificationResultRequest() # PatchedClassificationResultRequest |  (optional)

    try:
        api_response = api_instance.ml_inspectionresult_partial_update(id, patched_classification_result_request=patched_classification_result_request)
        print("The response of MlApi->ml_inspectionresult_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this classification result. | 
 **patched_classification_result_request** | [**PatchedClassificationResultRequest**](PatchedClassificationResultRequest.md)|  | [optional] 

### Return type

[**ClassificationResult**](ClassificationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_inspectionresult_retrieve**
> ClassificationResult ml_inspectionresult_retrieve(id, fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.classification_result import ClassificationResult
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this classification result.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.ml_inspectionresult_retrieve(id, fields=fields)
        print("The response of MlApi->ml_inspectionresult_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this classification result. | 
 **fields** | **str**|  | [optional] 

### Return type

[**ClassificationResult**](ClassificationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_inspectionresult_update**
> ClassificationResult ml_inspectionresult_update(id, classification_result_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.classification_result import ClassificationResult
from vue_avis_client.models.classification_result_request import ClassificationResultRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this classification result.
    classification_result_request = vue_avis_client.ClassificationResultRequest() # ClassificationResultRequest | 

    try:
        api_response = api_instance.ml_inspectionresult_update(id, classification_result_request)
        print("The response of MlApi->ml_inspectionresult_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_inspectionresult_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this classification result. | 
 **classification_result_request** | [**ClassificationResultRequest**](ClassificationResultRequest.md)|  | 

### Return type

[**ClassificationResult**](ClassificationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_create**
> MLModel ml_model_create(ml_model_request)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.models.ml_model_request import MLModelRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    ml_model_request = vue_avis_client.MLModelRequest() # MLModelRequest | 

    try:
        api_response = api_instance.ml_model_create(ml_model_request)
        print("The response of MlApi->ml_model_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ml_model_request** | [**MLModelRequest**](MLModelRequest.md)|  | 

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_destroy**
> ml_model_destroy(id)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model.

    try:
        api_instance.ml_model_destroy(id)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model. | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_inference**
> MLModel ml_model_inference(id, azure_ml_inference_request)



Infer a result from the model. This is a passthrough to the model's inference endpoint running somewhere else. The request body is passed through to the model.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.azure_ml_inference_request import AzureMLInferenceRequest
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model.
    azure_ml_inference_request = vue_avis_client.AzureMLInferenceRequest() # AzureMLInferenceRequest | 

    try:
        api_response = api_instance.ml_model_inference(id, azure_ml_inference_request)
        print("The response of MlApi->ml_model_inference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_inference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model. | 
 **azure_ml_inference_request** | [**AzureMLInferenceRequest**](AzureMLInferenceRequest.md)|  | 

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_list**
> List[MLModel] ml_model_list(fields=fields)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.ml_model_list(fields=fields)
        print("The response of MlApi->ml_model_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**List[MLModel]**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_partial_update**
> MLModel ml_model_partial_update(id, patched_ml_model_request=patched_ml_model_request)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.models.patched_ml_model_request import PatchedMLModelRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model.
    patched_ml_model_request = vue_avis_client.PatchedMLModelRequest() # PatchedMLModelRequest |  (optional)

    try:
        api_response = api_instance.ml_model_partial_update(id, patched_ml_model_request=patched_ml_model_request)
        print("The response of MlApi->ml_model_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model. | 
 **patched_ml_model_request** | [**PatchedMLModelRequest**](PatchedMLModelRequest.md)|  | [optional] 

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_retrieve**
> MLModel ml_model_retrieve(id, fields=fields)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.ml_model_retrieve(id, fields=fields)
        print("The response of MlApi->ml_model_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model. | 
 **fields** | **str**|  | [optional] 

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_model_update**
> MLModel ml_model_update(id, ml_model_request)



A viewset for ML models. It filters results based on the permissions granted to all the user's team(s).  A user will only be able to interact with an ML models if at least one of the teams they are a member of has access to it.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model import MLModel
from vue_avis_client.models.ml_model_request import MLModelRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model.
    ml_model_request = vue_avis_client.MLModelRequest() # MLModelRequest | 

    try:
        api_response = api_instance.ml_model_update(id, ml_model_request)
        print("The response of MlApi->ml_model_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_model_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model. | 
 **ml_model_request** | [**MLModelRequest**](MLModelRequest.md)|  | 

### Return type

[**MLModel**](MLModel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_create**
> MLModelType ml_modeltype_create(ml_model_type_request=ml_model_type_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model_type import MLModelType
from vue_avis_client.models.ml_model_type_request import MLModelTypeRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    ml_model_type_request = vue_avis_client.MLModelTypeRequest() # MLModelTypeRequest |  (optional)

    try:
        api_response = api_instance.ml_modeltype_create(ml_model_type_request=ml_model_type_request)
        print("The response of MlApi->ml_modeltype_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ml_model_type_request** | [**MLModelTypeRequest**](MLModelTypeRequest.md)|  | [optional] 

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_destroy**
> ml_modeltype_destroy(id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model type.

    try:
        api_instance.ml_modeltype_destroy(id)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model type. | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_list**
> List[MLModelType] ml_modeltype_list(fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model_type import MLModelType
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.ml_modeltype_list(fields=fields)
        print("The response of MlApi->ml_modeltype_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**List[MLModelType]**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_partial_update**
> MLModelType ml_modeltype_partial_update(id, patched_ml_model_type_request=patched_ml_model_type_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model_type import MLModelType
from vue_avis_client.models.patched_ml_model_type_request import PatchedMLModelTypeRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model type.
    patched_ml_model_type_request = vue_avis_client.PatchedMLModelTypeRequest() # PatchedMLModelTypeRequest |  (optional)

    try:
        api_response = api_instance.ml_modeltype_partial_update(id, patched_ml_model_type_request=patched_ml_model_type_request)
        print("The response of MlApi->ml_modeltype_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model type. | 
 **patched_ml_model_type_request** | [**PatchedMLModelTypeRequest**](PatchedMLModelTypeRequest.md)|  | [optional] 

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_retrieve**
> MLModelType ml_modeltype_retrieve(id, fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model_type import MLModelType
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model type.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.ml_modeltype_retrieve(id, fields=fields)
        print("The response of MlApi->ml_modeltype_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model type. | 
 **fields** | **str**|  | [optional] 

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ml_modeltype_update**
> MLModelType ml_modeltype_update(id, ml_model_type_request=ml_model_type_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.ml_model_type import MLModelType
from vue_avis_client.models.ml_model_type_request import MLModelTypeRequest
from vue_avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = vue_avis_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with vue_avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vue_avis_client.MlApi(api_client)
    id = 56 # int | A unique integer value identifying this ml model type.
    ml_model_type_request = vue_avis_client.MLModelTypeRequest() # MLModelTypeRequest |  (optional)

    try:
        api_response = api_instance.ml_modeltype_update(id, ml_model_type_request=ml_model_type_request)
        print("The response of MlApi->ml_modeltype_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlApi->ml_modeltype_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ml model type. | 
 **ml_model_type_request** | [**MLModelTypeRequest**](MLModelTypeRequest.md)|  | [optional] 

### Return type

[**MLModelType**](MLModelType.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

