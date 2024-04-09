# avis_client.MetadataApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_create**](MetadataApi.md#metadata_create) | **POST** /api/metadata/ | 
[**metadata_destroy**](MetadataApi.md#metadata_destroy) | **DELETE** /api/metadata/{id}/ | 
[**metadata_list**](MetadataApi.md#metadata_list) | **GET** /api/metadata/ | 
[**metadata_partial_update**](MetadataApi.md#metadata_partial_update) | **PATCH** /api/metadata/{id}/ | 
[**metadata_retrieve**](MetadataApi.md#metadata_retrieve) | **GET** /api/metadata/{id}/ | 
[**metadata_update**](MetadataApi.md#metadata_update) | **PUT** /api/metadata/{id}/ | 


# **metadata_create**
> Metadata metadata_create(metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata import Metadata
from avis_client.models.metadata_request import MetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    metadata_request = avis_client.MetadataRequest() # MetadataRequest | 

    try:
        api_response = api_instance.metadata_create(metadata_request)
        print("The response of MetadataApi->metadata_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_request** | [**MetadataRequest**](MetadataRequest.md)|  | 

### Return type

[**Metadata**](Metadata.md)

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

# **metadata_destroy**
> metadata_destroy(id)



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

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata.

    try:
        api_instance.metadata_destroy(id)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata. | 

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

# **metadata_list**
> PaginatedMetadataList metadata_list(fields=fields, id=id, ordering=ordering, page=page, page_size=page_size)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.paginated_metadata_list import PaginatedMetadataList
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    fields = 'fields_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.metadata_list(fields=fields, id=id, ordering=ordering, page=page, page_size=page_size)
        print("The response of MetadataApi->metadata_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedMetadataList**](PaginatedMetadataList.md)

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

# **metadata_partial_update**
> Metadata metadata_partial_update(id, patched_metadata_request=patched_metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata import Metadata
from avis_client.models.patched_metadata_request import PatchedMetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata.
    patched_metadata_request = avis_client.PatchedMetadataRequest() # PatchedMetadataRequest |  (optional)

    try:
        api_response = api_instance.metadata_partial_update(id, patched_metadata_request=patched_metadata_request)
        print("The response of MetadataApi->metadata_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata. | 
 **patched_metadata_request** | [**PatchedMetadataRequest**](PatchedMetadataRequest.md)|  | [optional] 

### Return type

[**Metadata**](Metadata.md)

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

# **metadata_retrieve**
> Metadata metadata_retrieve(id, fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata import Metadata
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.metadata_retrieve(id, fields=fields)
        print("The response of MetadataApi->metadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata. | 
 **fields** | **str**|  | [optional] 

### Return type

[**Metadata**](Metadata.md)

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

# **metadata_update**
> Metadata metadata_update(id, metadata_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata import Metadata
from avis_client.models.metadata_request import MetadataRequest
from avis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = avis_client.Configuration(
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
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.MetadataApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata.
    metadata_request = avis_client.MetadataRequest() # MetadataRequest | 

    try:
        api_response = api_instance.metadata_update(id, metadata_request)
        print("The response of MetadataApi->metadata_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->metadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata. | 
 **metadata_request** | [**MetadataRequest**](MetadataRequest.md)|  | 

### Return type

[**Metadata**](Metadata.md)

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

