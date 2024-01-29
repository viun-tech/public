# vue_avis_client.InspectionprocessblueprintApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspectionprocessblueprint_create**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_create) | **POST** /api/inspectionprocessblueprint/ |
[**inspectionprocessblueprint_destroy**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_destroy) | **DELETE** /api/inspectionprocessblueprint/{id}/ |
[**inspectionprocessblueprint_list**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_list) | **GET** /api/inspectionprocessblueprint/ |
[**inspectionprocessblueprint_partial_update**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_partial_update) | **PATCH** /api/inspectionprocessblueprint/{id}/ |
[**inspectionprocessblueprint_retrieve**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_retrieve) | **GET** /api/inspectionprocessblueprint/{id}/ |
[**inspectionprocessblueprint_update**](InspectionprocessblueprintApi.md#inspectionprocessblueprint_update) | **PUT** /api/inspectionprocessblueprint/{id}/ |


# **inspectionprocessblueprint_create**
> InspectionProcessBlueprint inspectionprocessblueprint_create(inspection_process_blueprint_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint
from vue_avis_client.models.inspection_process_blueprint_request import InspectionProcessBlueprintRequest
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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    inspection_process_blueprint_request = vue_avis_client.InspectionProcessBlueprintRequest() # InspectionProcessBlueprintRequest |

    try:
        api_response = api_instance.inspectionprocessblueprint_create(inspection_process_blueprint_request)
        print("The response of InspectionprocessblueprintApi->inspectionprocessblueprint_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_process_blueprint_request** | [**InspectionProcessBlueprintRequest**](InspectionProcessBlueprintRequest.md)|  |

### Return type

[**InspectionProcessBlueprint**](InspectionProcessBlueprint.md)

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

# **inspectionprocessblueprint_destroy**
> inspectionprocessblueprint_destroy(id)



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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection process blueprint.

    try:
        api_instance.inspectionprocessblueprint_destroy(id)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection process blueprint. |

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

# **inspectionprocessblueprint_list**
> List[InspectionProcessBlueprint] inspectionprocessblueprint_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint
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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.inspectionprocessblueprint_list(id=id)
        print("The response of InspectionprocessblueprintApi->inspectionprocessblueprint_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[InspectionProcessBlueprint]**](InspectionProcessBlueprint.md)

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

# **inspectionprocessblueprint_partial_update**
> InspectionProcessBlueprint inspectionprocessblueprint_partial_update(id, patched_inspection_process_blueprint_request=patched_inspection_process_blueprint_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint
from vue_avis_client.models.patched_inspection_process_blueprint_request import PatchedInspectionProcessBlueprintRequest
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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection process blueprint.
    patched_inspection_process_blueprint_request = vue_avis_client.PatchedInspectionProcessBlueprintRequest() # PatchedInspectionProcessBlueprintRequest |  (optional)

    try:
        api_response = api_instance.inspectionprocessblueprint_partial_update(id, patched_inspection_process_blueprint_request=patched_inspection_process_blueprint_request)
        print("The response of InspectionprocessblueprintApi->inspectionprocessblueprint_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection process blueprint. |
 **patched_inspection_process_blueprint_request** | [**PatchedInspectionProcessBlueprintRequest**](PatchedInspectionProcessBlueprintRequest.md)|  | [optional]

### Return type

[**InspectionProcessBlueprint**](InspectionProcessBlueprint.md)

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

# **inspectionprocessblueprint_retrieve**
> InspectionProcessBlueprint inspectionprocessblueprint_retrieve(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint
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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection process blueprint.

    try:
        api_response = api_instance.inspectionprocessblueprint_retrieve(id)
        print("The response of InspectionprocessblueprintApi->inspectionprocessblueprint_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection process blueprint. |

### Return type

[**InspectionProcessBlueprint**](InspectionProcessBlueprint.md)

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

# **inspectionprocessblueprint_update**
> InspectionProcessBlueprint inspectionprocessblueprint_update(id, inspection_process_blueprint_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint
from vue_avis_client.models.inspection_process_blueprint_request import InspectionProcessBlueprintRequest
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
    api_instance = vue_avis_client.InspectionprocessblueprintApi(api_client)
    id = 56 # int | A unique integer value identifying this inspection process blueprint.
    inspection_process_blueprint_request = vue_avis_client.InspectionProcessBlueprintRequest() # InspectionProcessBlueprintRequest |

    try:
        api_response = api_instance.inspectionprocessblueprint_update(id, inspection_process_blueprint_request)
        print("The response of InspectionprocessblueprintApi->inspectionprocessblueprint_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionprocessblueprintApi->inspectionprocessblueprint_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inspection process blueprint. |
 **inspection_process_blueprint_request** | [**InspectionProcessBlueprintRequest**](InspectionProcessBlueprintRequest.md)|  |

### Return type

[**InspectionProcessBlueprint**](InspectionProcessBlueprint.md)

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
