# vue_avis_client.ImageApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_create**](ImageApi.md#image_create) | **POST** /api/image/ |
[**image_destroy**](ImageApi.md#image_destroy) | **DELETE** /api/image/{id}/ |
[**image_inspection_status_list**](ImageApi.md#image_inspection_status_list) | **GET** /api/image/inspection_status/ |
[**image_list**](ImageApi.md#image_list) | **GET** /api/image/ |
[**image_partial_update**](ImageApi.md#image_partial_update) | **PATCH** /api/image/{id}/ |
[**image_quality_list**](ImageApi.md#image_quality_list) | **GET** /api/image/quality/ |
[**image_retrieve**](ImageApi.md#image_retrieve) | **GET** /api/image/{id}/ |
[**image_update**](ImageApi.md#image_update) | **PUT** /api/image/{id}/ |


# **image_create**
> Image image_create(team, capture_datetime, file, case=case, uploaded_by=uploaded_by, inspection_results=inspection_results, format=format, part_id=part_id, validation_status=validation_status)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.format_enum import FormatEnum
from vue_avis_client.models.image import Image
from vue_avis_client.models.validation_status_enum import ValidationStatusEnum
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
    api_instance = vue_avis_client.ImageApi(api_client)
    team = 56 # int |
    capture_datetime = '2013-10-20T19:20:30+01:00' # datetime |
    file = None # bytearray |
    case = 56 # int |  (optional)
    uploaded_by = 56 # int |  (optional)
    inspection_results = [56] # List[int] |  (optional)
    format = vue_avis_client.FormatEnum() # FormatEnum |  (optional)
    part_id = 'part_id_example' # str |  (optional)
    validation_status = vue_avis_client.ValidationStatusEnum() # ValidationStatusEnum |  (optional)

    try:
        api_response = api_instance.image_create(team, capture_datetime, file, case=case, uploaded_by=uploaded_by, inspection_results=inspection_results, format=format, part_id=part_id, validation_status=validation_status)
        print("The response of ImageApi->image_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **int**|  |
 **capture_datetime** | **datetime**|  |
 **file** | **bytearray**|  |
 **case** | **int**|  | [optional]
 **uploaded_by** | **int**|  | [optional]
 **inspection_results** | [**List[int]**](int.md)|  | [optional]
 **format** | [**FormatEnum**](FormatEnum.md)|  | [optional]
 **part_id** | **str**|  | [optional]
 **validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md)|  | [optional]

### Return type

[**Image**](Image.md)

### Authorization

[cookieAuth](..#cookieAuth), [ApiKeyAuth](..#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to Model list]](..#documentation-for-models) [[Back to README]](..)

# **image_destroy**
> image_destroy(id)



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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = 56 # int | A unique integer value identifying this image.

    try:
        api_instance.image_destroy(id)
    except Exception as e:
        print("Exception when calling ImageApi->image_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image. |

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

# **image_inspection_status_list**
> List[InspectionStatus] image_inspection_status_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.inspection_status import InspectionStatus
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.image_inspection_status_list(id=id)
        print("The response of ImageApi->image_inspection_status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_inspection_status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[InspectionStatus]**](InspectionStatus.md)

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

# **image_list**
> List[Image] image_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.image import Image
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.image_list(id=id)
        print("The response of ImageApi->image_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[Image]**](Image.md)

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

# **image_partial_update**
> Image image_partial_update(id, patched_image_request=patched_image_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.image import Image
from vue_avis_client.models.patched_image_request import PatchedImageRequest
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = 56 # int | A unique integer value identifying this image.
    patched_image_request = vue_avis_client.PatchedImageRequest() # PatchedImageRequest |  (optional)

    try:
        api_response = api_instance.image_partial_update(id, patched_image_request=patched_image_request)
        print("The response of ImageApi->image_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image. |
 **patched_image_request** | [**PatchedImageRequest**](PatchedImageRequest.md)|  | [optional]

### Return type

[**Image**](Image.md)

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

# **image_quality_list**
> List[ImageQualityGateResult] image_quality_list(id=id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.image_quality_gate_result import ImageQualityGateResult
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.image_quality_list(id=id)
        print("The response of ImageApi->image_quality_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_quality_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional]

### Return type

[**List[ImageQualityGateResult]**](ImageQualityGateResult.md)

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

# **image_retrieve**
> Image image_retrieve(id)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.image import Image
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = 56 # int | A unique integer value identifying this image.

    try:
        api_response = api_instance.image_retrieve(id)
        print("The response of ImageApi->image_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image. |

### Return type

[**Image**](Image.md)

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

# **image_update**
> Image image_update(id, image_request)



A viewset that filters results based on the user's team memberships.  Not to be used directly, but as a base class for other viewsets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.image import Image
from vue_avis_client.models.image_request import ImageRequest
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
    api_instance = vue_avis_client.ImageApi(api_client)
    id = 56 # int | A unique integer value identifying this image.
    image_request = vue_avis_client.ImageRequest() # ImageRequest |

    try:
        api_response = api_instance.image_update(id, image_request)
        print("The response of ImageApi->image_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image. |
 **image_request** | [**ImageRequest**](ImageRequest.md)|  |

### Return type

[**Image**](Image.md)

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
