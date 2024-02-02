# vue_avis_client.InspectionmetadataschemaApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspectionmetadataschema_create**](InspectionmetadataschemaApi.md#inspectionmetadataschema_create) | **POST** /api/inspectionmetadataschema/ |
[**inspectionmetadataschema_destroy**](InspectionmetadataschemaApi.md#inspectionmetadataschema_destroy) | **DELETE** /api/inspectionmetadataschema/{id}/ |
[**inspectionmetadataschema_list**](InspectionmetadataschemaApi.md#inspectionmetadataschema_list) | **GET** /api/inspectionmetadataschema/ |
[**inspectionmetadataschema_partial_update**](InspectionmetadataschemaApi.md#inspectionmetadataschema_partial_update) | **PATCH** /api/inspectionmetadataschema/{id}/ |
[**inspectionmetadataschema_retrieve**](InspectionmetadataschemaApi.md#inspectionmetadataschema_retrieve) | **GET** /api/inspectionmetadataschema/{id}/ |
[**inspectionmetadataschema_update**](InspectionmetadataschemaApi.md#inspectionmetadataschema_update) | **PUT** /api/inspectionmetadataschema/{id}/ |


# **inspectionmetadataschema_create**
> InspectionMetadataSchema inspectionmetadataschema_create(inspection_metadata_schema_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema
from vue_avis_client.models.inspection_metadata_schema_request import InspectionMetadataSchemaRequest
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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    inspection_metadata_schema_request = vue_avis_client.InspectionMetadataSchemaRequest() # InspectionMetadataSchemaRequest |

    try:
        api_response = api_instance.inspectionmetadataschema_create(inspection_metadata_schema_request)
        print("The response of InspectionmetadataschemaApi->inspectionmetadataschema_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_metadata_schema_request** | [**InspectionMetadataSchemaRequest**](InspectionMetadataSchemaRequest.md)|  |

### Return type

[**InspectionMetadataSchema**](InspectionMetadataSchema.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **inspectionmetadataschema_destroy**
> inspectionmetadataschema_destroy(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata schema.

    try:
        api_instance.inspectionmetadataschema_destroy(id)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata schema. |

### Return type

void (empty response body)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **inspectionmetadataschema_list**
> List[InspectionMetadataSchema] inspectionmetadataschema_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema
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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.inspectionmetadataschema_list(id=id)
        print("The response of InspectionmetadataschemaApi->inspectionmetadataschema_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[InspectionMetadataSchema]**](InspectionMetadataSchema.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **inspectionmetadataschema_partial_update**
> InspectionMetadataSchema inspectionmetadataschema_partial_update(id, patched_inspection_metadata_schema_request=patched_inspection_metadata_schema_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema
from vue_avis_client.models.patched_inspection_metadata_schema_request import PatchedInspectionMetadataSchemaRequest
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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata schema.
    patched_inspection_metadata_schema_request = vue_avis_client.PatchedInspectionMetadataSchemaRequest() # PatchedInspectionMetadataSchemaRequest |  (optional)

    try:
        api_response = api_instance.inspectionmetadataschema_partial_update(id, patched_inspection_metadata_schema_request=patched_inspection_metadata_schema_request)
        print("The response of InspectionmetadataschemaApi->inspectionmetadataschema_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata schema. |
 **patched_inspection_metadata_schema_request** | [**PatchedInspectionMetadataSchemaRequest**](PatchedInspectionMetadataSchemaRequest.md)|  | [optional]

### Return type

[**InspectionMetadataSchema**](InspectionMetadataSchema.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **inspectionmetadataschema_retrieve**
> InspectionMetadataSchema inspectionmetadataschema_retrieve(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema
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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata schema.

    try:
        api_response = api_instance.inspectionmetadataschema_retrieve(id)
        print("The response of InspectionmetadataschemaApi->inspectionmetadataschema_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata schema. |

### Return type

[**InspectionMetadataSchema**](InspectionMetadataSchema.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **inspectionmetadataschema_update**
> InspectionMetadataSchema inspectionmetadataschema_update(id, inspection_metadata_schema_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema
from vue_avis_client.models.inspection_metadata_schema_request import InspectionMetadataSchemaRequest
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
    api_instance = vue_avis_client.InspectionmetadataschemaApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection metadata schema.
    inspection_metadata_schema_request = vue_avis_client.InspectionMetadataSchemaRequest() # InspectionMetadataSchemaRequest |

    try:
        api_response = api_instance.inspectionmetadataschema_update(id, inspection_metadata_schema_request)
        print("The response of InspectionmetadataschemaApi->inspectionmetadataschema_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionmetadataschemaApi->inspectionmetadataschema_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection metadata schema. |
 **inspection_metadata_schema_request** | [**InspectionMetadataSchemaRequest**](InspectionMetadataSchemaRequest.md)|  |

### Return type

[**InspectionMetadataSchema**](InspectionMetadataSchema.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)
