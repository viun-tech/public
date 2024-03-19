# avis_client.MetadataSchemaApi

All URIs are relative to *https://avis.vu.engineering*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_schema_create**](MetadataSchemaApi.md#metadata_schema_create) | **POST** /api/metadata-schema/ | 
[**metadata_schema_destroy**](MetadataSchemaApi.md#metadata_schema_destroy) | **DELETE** /api/metadata-schema/{id}/ | 
[**metadata_schema_list**](MetadataSchemaApi.md#metadata_schema_list) | **GET** /api/metadata-schema/ | 
[**metadata_schema_partial_update**](MetadataSchemaApi.md#metadata_schema_partial_update) | **PATCH** /api/metadata-schema/{id}/ | 
[**metadata_schema_retrieve**](MetadataSchemaApi.md#metadata_schema_retrieve) | **GET** /api/metadata-schema/{id}/ | 
[**metadata_schema_update**](MetadataSchemaApi.md#metadata_schema_update) | **PUT** /api/metadata-schema/{id}/ | 


# **metadata_schema_create**
> MetadataSchema metadata_schema_create(metadata_schema_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata_schema import MetadataSchema
from avis_client.models.metadata_schema_request import MetadataSchemaRequest
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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    metadata_schema_request = avis_client.MetadataSchemaRequest() # MetadataSchemaRequest | 

    try:
        api_response = api_instance.metadata_schema_create(metadata_schema_request)
        print("The response of MetadataSchemaApi->metadata_schema_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_schema_request** | [**MetadataSchemaRequest**](MetadataSchemaRequest.md)|  | 

### Return type

[**MetadataSchema**](MetadataSchema.md)

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

# **metadata_schema_destroy**
> metadata_schema_destroy(id)



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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata schema.

    try:
        api_instance.metadata_schema_destroy(id)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata schema. | 

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

# **metadata_schema_list**
> List[MetadataSchema] metadata_schema_list(fields=fields, id=id)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata_schema import MetadataSchema
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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    fields = 'fields_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.metadata_schema_list(fields=fields, id=id)
        print("The response of MetadataSchemaApi->metadata_schema_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 

### Return type

[**List[MetadataSchema]**](MetadataSchema.md)

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

# **metadata_schema_partial_update**
> MetadataSchema metadata_schema_partial_update(id, patched_metadata_schema_request=patched_metadata_schema_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata_schema import MetadataSchema
from avis_client.models.patched_metadata_schema_request import PatchedMetadataSchemaRequest
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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata schema.
    patched_metadata_schema_request = avis_client.PatchedMetadataSchemaRequest() # PatchedMetadataSchemaRequest |  (optional)

    try:
        api_response = api_instance.metadata_schema_partial_update(id, patched_metadata_schema_request=patched_metadata_schema_request)
        print("The response of MetadataSchemaApi->metadata_schema_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata schema. | 
 **patched_metadata_schema_request** | [**PatchedMetadataSchemaRequest**](PatchedMetadataSchemaRequest.md)|  | [optional] 

### Return type

[**MetadataSchema**](MetadataSchema.md)

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

# **metadata_schema_retrieve**
> MetadataSchema metadata_schema_retrieve(id, fields=fields)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata_schema import MetadataSchema
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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata schema.
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = api_instance.metadata_schema_retrieve(id, fields=fields)
        print("The response of MetadataSchemaApi->metadata_schema_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata schema. | 
 **fields** | **str**|  | [optional] 

### Return type

[**MetadataSchema**](MetadataSchema.md)

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

# **metadata_schema_update**
> MetadataSchema metadata_schema_update(id, metadata_schema_request)



A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.metadata_schema import MetadataSchema
from avis_client.models.metadata_schema_request import MetadataSchemaRequest
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
    api_instance = avis_client.MetadataSchemaApi(api_client)
    id = 56 # int | A unique integer value identifying this metadata schema.
    metadata_schema_request = avis_client.MetadataSchemaRequest() # MetadataSchemaRequest | 

    try:
        api_response = api_instance.metadata_schema_update(id, metadata_schema_request)
        print("The response of MetadataSchemaApi->metadata_schema_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemaApi->metadata_schema_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this metadata schema. | 
 **metadata_schema_request** | [**MetadataSchemaRequest**](MetadataSchemaRequest.md)|  | 

### Return type

[**MetadataSchema**](MetadataSchema.md)

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

