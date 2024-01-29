# vue_avis_client.InspectionobjectApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspectionobject_create**](InspectionobjectApi.md#inspectionobject_create) | **POST** /api/inspectionobject/ |
[**inspectionobject_destroy**](InspectionobjectApi.md#inspectionobject_destroy) | **DELETE** /api/inspectionobject/{id}/ |
[**inspectionobject_list**](InspectionobjectApi.md#inspectionobject_list) | **GET** /api/inspectionobject/ |
[**inspectionobject_partial_update**](InspectionobjectApi.md#inspectionobject_partial_update) | **PATCH** /api/inspectionobject/{id}/ |
[**inspectionobject_retrieve**](InspectionobjectApi.md#inspectionobject_retrieve) | **GET** /api/inspectionobject/{id}/ |
[**inspectionobject_update**](InspectionobjectApi.md#inspectionobject_update) | **PUT** /api/inspectionobject/{id}/ |


# **inspectionobject_create**
> InspectionObject inspectionobject_create(inspection_object_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object import InspectionObject
from vue_avis_client.models.inspection_object_request import InspectionObjectRequest
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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    inspection_object_request = vue_avis_client.InspectionObjectRequest() # InspectionObjectRequest |

    try:
        api_response = api_instance.inspectionobject_create(inspection_object_request)
        print("The response of InspectionobjectApi->inspectionobject_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_object_request** | [**InspectionObjectRequest**](InspectionObjectRequest.md)|  |

### Return type

[**InspectionObject**](InspectionObject.md)

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

# **inspectionobject_destroy**
> inspectionobject_destroy(id)



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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object.

    try:
        api_instance.inspectionobject_destroy(id)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object. |

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

# **inspectionobject_list**
> List[InspectionObject] inspectionobject_list(id=id, identifier=identifier, type=type)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object import InspectionObject
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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)
    identifier = ['identifier_example'] # List[str] | Multiple values may be separated by commas. (optional)
    type = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.inspectionobject_list(id=id, identifier=identifier, type=type)
        print("The response of InspectionobjectApi->inspectionobject_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]
 **identifier** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional]
 **type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[InspectionObject]**](InspectionObject.md)

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

# **inspectionobject_partial_update**
> InspectionObject inspectionobject_partial_update(id, patched_inspection_object_request=patched_inspection_object_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object import InspectionObject
from vue_avis_client.models.patched_inspection_object_request import PatchedInspectionObjectRequest
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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object.
    patched_inspection_object_request = vue_avis_client.PatchedInspectionObjectRequest() # PatchedInspectionObjectRequest |  (optional)

    try:
        api_response = api_instance.inspectionobject_partial_update(id, patched_inspection_object_request=patched_inspection_object_request)
        print("The response of InspectionobjectApi->inspectionobject_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object. |
 **patched_inspection_object_request** | [**PatchedInspectionObjectRequest**](PatchedInspectionObjectRequest.md)|  | [optional]

### Return type

[**InspectionObject**](InspectionObject.md)

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

# **inspectionobject_retrieve**
> InspectionObject inspectionobject_retrieve(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object import InspectionObject
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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object.

    try:
        api_response = api_instance.inspectionobject_retrieve(id)
        print("The response of InspectionobjectApi->inspectionobject_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object. |

### Return type

[**InspectionObject**](InspectionObject.md)

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

# **inspectionobject_update**
> InspectionObject inspectionobject_update(id, inspection_object_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_object import InspectionObject
from vue_avis_client.models.inspection_object_request import InspectionObjectRequest
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
    api_instance = vue_avis_client.InspectionobjectApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection object.
    inspection_object_request = vue_avis_client.InspectionObjectRequest() # InspectionObjectRequest |

    try:
        api_response = api_instance.inspectionobject_update(id, inspection_object_request)
        print("The response of InspectionobjectApi->inspectionobject_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionobjectApi->inspectionobject_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection object. |
 **inspection_object_request** | [**InspectionObjectRequest**](InspectionObjectRequest.md)|  |

### Return type

[**InspectionObject**](InspectionObject.md)

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
