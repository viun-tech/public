# avis_client.MembershipApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_create**](MembershipApi.md#membership_create) | **POST** /api/membership/ |
[**membership_destroy**](MembershipApi.md#membership_destroy) | **DELETE** /api/membership/{id}/ |
[**membership_list**](MembershipApi.md#membership_list) | **GET** /api/membership/ |
[**membership_retrieve**](MembershipApi.md#membership_retrieve) | **GET** /api/membership/{id}/ |
[**membership_update**](MembershipApi.md#membership_update) | **PUT** /api/membership/{id}/ |


# **membership_create**
> Membership membership_create(membership_request)



A mixin that allows reading entities (listing and retrieving by id).

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.membership import Membership
from avis_client.models.membership_request import MembershipRequest
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
    api_instance = avis_client.MembershipApi(api_client)
    membership_request = avis_client.MembershipRequest() # MembershipRequest |

    try:
        api_response = api_instance.membership_create(membership_request)
        print("The response of MembershipApi->membership_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_request** | [**MembershipRequest**](MembershipRequest.md)|  |

### Return type

[**Membership**](Membership.md)

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

# **membership_destroy**
> membership_destroy(id)



A mixin that allows reading entities (listing and retrieving by id).

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
    api_instance = avis_client.MembershipApi(api_client)
    id = 56 # int | A unique integer value identifying this membership.

    try:
        api_instance.membership_destroy(id)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this membership. |

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

# **membership_list**
> PaginatedMembershipList membership_list(page=page, page_size=page_size)



A mixin that allows reading entities (listing and retrieving by id).

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.paginated_membership_list import PaginatedMembershipList
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
    api_instance = avis_client.MembershipApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.membership_list(page=page, page_size=page_size)
        print("The response of MembershipApi->membership_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**PaginatedMembershipList**](PaginatedMembershipList.md)

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

# **membership_retrieve**
> Membership membership_retrieve(id)



A mixin that allows reading entities (listing and retrieving by id).

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.membership import Membership
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
    api_instance = avis_client.MembershipApi(api_client)
    id = 56 # int | A unique integer value identifying this membership.

    try:
        api_response = api_instance.membership_retrieve(id)
        print("The response of MembershipApi->membership_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this membership. |

### Return type

[**Membership**](Membership.md)

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

# **membership_update**
> Membership membership_update(id, membership_request)



A mixin that allows reading entities (listing and retrieving by id).

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.membership import Membership
from avis_client.models.membership_request import MembershipRequest
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
    api_instance = avis_client.MembershipApi(api_client)
    id = 56 # int | A unique integer value identifying this membership.
    membership_request = avis_client.MembershipRequest() # MembershipRequest |

    try:
        api_response = api_instance.membership_update(id, membership_request)
        print("The response of MembershipApi->membership_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this membership. |
 **membership_request** | [**MembershipRequest**](MembershipRequest.md)|  |

### Return type

[**Membership**](Membership.md)

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
