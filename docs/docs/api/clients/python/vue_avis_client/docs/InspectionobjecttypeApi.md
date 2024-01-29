# vue_avis_client.InspectionobjecttypeApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspectionobjecttype_create**](InspectionobjecttypeApi.md#inspectionobjecttype_create) | **POST** /api/inspectionobjecttype/ |
[**inspectionobjecttype_destroy**](InspectionobjecttypeApi.md#inspectionobjecttype_destroy) | **DELETE** /api/inspectionobjecttype/{id}/ |
[**inspectionobjecttype_list**](InspectionobjecttypeApi.md#inspectionobjecttype_list) | **GET** /api/inspectionobjecttype/ |
[**inspectionobjecttype_partial_update**](InspectionobjecttypeApi.md#inspectionobjecttype_partial_update) | **PATCH** /api/inspectionobjecttype/{id}/ |
[**inspectionobjecttype_retrieve**](InspectionobjecttypeApi.md#inspectionobjecttype_retrieve) | **GET** /api/inspectionobjecttype/{id}/ |
[**inspectionobjecttype_update**](InspectionobjecttypeApi.md#inspectionobjecttype_update) | **PUT** /api/inspectionobjecttype/{id}/ |


# **inspectionobjecttype_create**
> InspectionObjectType inspectionobjecttype_create(inspection_object_type_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object_type import InspectionObjectType
from vue_avis_client.models.inspection_object_type_request import InspectionObjectTypeRequest
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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    inspection_object_type_request = vue_avis_client.InspectionObjectTypeRequest() # InspectionObjectTypeRequest |

    try:
        api_response = api_instance.inspectionobjecttype_create(inspection_object_type_request)
        print("The response of InspectionobjecttypeApi->inspectionobjecttype_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_object_type_request** | [**InspectionObjectTypeRequest**](InspectionObjectTypeRequest.md)|  |

### Return type

[**InspectionObjectType**](InspectionObjectType.md)

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

# **inspectionobjecttype_destroy**
> inspectionobjecttype_destroy(id)



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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object type.

    try:
        api_instance.inspectionobjecttype_destroy(id)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object type. |

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

# **inspectionobjecttype_list**
> List[InspectionObjectType] inspectionobjecttype_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object_type import InspectionObjectType
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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.inspectionobjecttype_list(id=id)
        print("The response of InspectionobjecttypeApi->inspectionobjecttype_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[InspectionObjectType]**](InspectionObjectType.md)

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

# **inspectionobjecttype_partial_update**
> InspectionObjectType inspectionobjecttype_partial_update(id, patched_inspection_object_type_request=patched_inspection_object_type_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object_type import InspectionObjectType
from vue_avis_client.models.patched_inspection_object_type_request import PatchedInspectionObjectTypeRequest
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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object type.
    patched_inspection_object_type_request = vue_avis_client.PatchedInspectionObjectTypeRequest() # PatchedInspectionObjectTypeRequest |  (optional)

    try:
        api_response = api_instance.inspectionobjecttype_partial_update(id, patched_inspection_object_type_request=patched_inspection_object_type_request)
        print("The response of InspectionobjecttypeApi->inspectionobjecttype_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object type. |
 **patched_inspection_object_type_request** | [**PatchedInspectionObjectTypeRequest**](PatchedInspectionObjectTypeRequest.md)|  | [optional]

### Return type

[**InspectionObjectType**](InspectionObjectType.md)

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

# **inspectionobjecttype_retrieve**
> InspectionObjectType inspectionobjecttype_retrieve(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object_type import InspectionObjectType
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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object type.

    try:
        api_response = api_instance.inspectionobjecttype_retrieve(id)
        print("The response of InspectionobjecttypeApi->inspectionobjecttype_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object type. |

### Return type

[**InspectionObjectType**](InspectionObjectType.md)

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

# **inspectionobjecttype_update**
> InspectionObjectType inspectionobjecttype_update(id, inspection_object_type_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object_type import InspectionObjectType
from vue_avis_client.models.inspection_object_type_request import InspectionObjectTypeRequest
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
    api_instance = vue_avis_client.InspectionobjecttypeApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object type.
    inspection_object_type_request = vue_avis_client.InspectionObjectTypeRequest() # InspectionObjectTypeRequest |

    try:
        api_response = api_instance.inspectionobjecttype_update(id, inspection_object_type_request)
        print("The response of InspectionobjecttypeApi->inspectionobjecttype_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjecttypeApi->inspectionobjecttype_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object type. |
 **inspection_object_type_request** | [**InspectionObjectTypeRequest**](InspectionObjectTypeRequest.md)|  |

### Return type

[**InspectionObjectType**](InspectionObjectType.md)

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
