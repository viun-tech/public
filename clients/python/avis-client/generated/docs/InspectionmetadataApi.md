# avis_client.InspectionmetadataApi

All URIs are relative to *https://avis.vu.engineering*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspectionmetadata_create**](InspectionmetadataApi.md#inspectionmetadata_create) | **POST** /api/inspectionmetadata/ | 
[**inspectionmetadata_destroy**](InspectionmetadataApi.md#inspectionmetadata_destroy) | **DELETE** /api/inspectionmetadata/{id}/ | 
[**inspectionmetadata_list**](InspectionmetadataApi.md#inspectionmetadata_list) | **GET** /api/inspectionmetadata/ | 
[**inspectionmetadata_partial_update**](InspectionmetadataApi.md#inspectionmetadata_partial_update) | **PATCH** /api/inspectionmetadata/{id}/ | 
[**inspectionmetadata_retrieve**](InspectionmetadataApi.md#inspectionmetadata_retrieve) | **GET** /api/inspectionmetadata/{id}/ | 
[**inspectionmetadata_update**](InspectionmetadataApi.md#inspectionmetadata_update) | **PUT** /api/inspectionmetadata/{id}/ | 


# **inspectionmetadata_create**
> InspectionMetadata inspectionmetadata_create(inspection_metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.inspection_metadata import InspectionMetadata
from avis_client.models.inspection_metadata_request import InspectionMetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    inspection_metadata_request = avis_client.InspectionMetadataRequest() # InspectionMetadataRequest | 

    try:
        api_response = api_instance.inspectionmetadata_create(inspection_metadata_request)
        print("The response of InspectionmetadataApi->inspectionmetadata_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_metadata_request** | [**InspectionMetadataRequest**](InspectionMetadataRequest.md)|  | 

### Return type

[**InspectionMetadata**](InspectionMetadata.md)

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

# **inspectionmetadata_destroy**
> inspectionmetadata_destroy(id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata.

    try:
        api_instance.inspectionmetadata_destroy(id)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata. | 

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

# **inspectionmetadata_list**
> List[InspectionMetadata] inspectionmetadata_list(fields=fields, id=id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.inspection_metadata import InspectionMetadata
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    fields = 'fields_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.inspectionmetadata_list(fields=fields, id=id)
        print("The response of InspectionmetadataApi->inspectionmetadata_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 

### Return type

[**List[InspectionMetadata]**](InspectionMetadata.md)

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

# **inspectionmetadata_partial_update**
> InspectionMetadata inspectionmetadata_partial_update(id, patched_inspection_metadata_request=patched_inspection_metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.inspection_metadata import InspectionMetadata
from avis_client.models.patched_inspection_metadata_request import PatchedInspectionMetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata.
    patched_inspection_metadata_request = avis_client.PatchedInspectionMetadataRequest() # PatchedInspectionMetadataRequest |  (optional)

    try:
        api_response = api_instance.inspectionmetadata_partial_update(id, patched_inspection_metadata_request=patched_inspection_metadata_request)
        print("The response of InspectionmetadataApi->inspectionmetadata_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata. | 
 **patched_inspection_metadata_request** | [**PatchedInspectionMetadataRequest**](PatchedInspectionMetadataRequest.md)|  | [optional] 

### Return type

[**InspectionMetadata**](InspectionMetadata.md)

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

# **inspectionmetadata_retrieve**
> InspectionMetadata inspectionmetadata_retrieve(id, fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.inspection_metadata import InspectionMetadata
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.inspectionmetadata_retrieve(id, fields=fields)
        print("The response of InspectionmetadataApi->inspectionmetadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata. | 
 **fields** | **str**|  | [optional] 

### Return type

[**InspectionMetadata**](InspectionMetadata.md)

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

# **inspectionmetadata_update**
> InspectionMetadata inspectionmetadata_update(id, inspection_metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.inspection_metadata import InspectionMetadata
from avis_client.models.inspection_metadata_request import InspectionMetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://avis.vu.engineering
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
    host = "https://avis.vu.engineering"
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.InspectionmetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata.
    inspection_metadata_request = avis_client.InspectionMetadataRequest() # InspectionMetadataRequest | 

    try:
        api_response = api_instance.inspectionmetadata_update(id, inspection_metadata_request)
        print("The response of InspectionmetadataApi->inspectionmetadata_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataApi->inspectionmetadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata. | 
 **inspection_metadata_request** | [**InspectionMetadataRequest**](InspectionMetadataRequest.md)|  | 

### Return type

[**InspectionMetadata**](InspectionMetadata.md)

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

