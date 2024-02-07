# avis_client.TeamApi

All URIs are relative to *https://avis.vu.engineering*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_create**](TeamApi.md#team_create) | **POST** /api/team/ |
[**team_destroy**](TeamApi.md#team_destroy) | **DELETE** /api/team/{id}/ |
[**team_list**](TeamApi.md#team_list) | **GET** /api/team/ |
[**team_retrieve**](TeamApi.md#team_retrieve) | **GET** /api/team/{id}/ |
[**team_update**](TeamApi.md#team_update) | **PUT** /api/team/{id}/ |


# **team_create**
> Team team_create(team_request)



A base read-only viewset that enables optimized queryset fetching and tracing.  This is a combination of the following mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset making it read-only.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.team import Team
from avis_client.models.team_request import TeamRequest
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
    api_instance = avis_client.TeamApi(api_client)
    team_request = avis_client.TeamRequest() # TeamRequest |

    try:
        api_response = api_instance.team_create(team_request)
        print("The response of TeamApi->team_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_request** | [**TeamRequest**](TeamRequest.md)|  |

### Return type

[**Team**](Team.md)

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

# **team_destroy**
> team_destroy(id)



A base read-only viewset that enables optimized queryset fetching and tracing.  This is a combination of the following mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset making it read-only.

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
    api_instance = avis_client.TeamApi(api_client)
    id = 56 # int | A unique integer value identifying this team.

    try:
        api_instance.team_destroy(id)
    except Exception as e:
        print("Exception when calling TeamApi->team_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. |

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

# **team_list**
> List[Team] team_list()



A base read-only viewset that enables optimized queryset fetching and tracing.  This is a combination of the following mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset making it read-only.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.team import Team
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
    api_instance = avis_client.TeamApi(api_client)

    try:
        api_response = api_instance.team_list()
        print("The response of TeamApi->team_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Team]**](Team.md)

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

# **team_retrieve**
> Team team_retrieve(id)



A base read-only viewset that enables optimized queryset fetching and tracing.  This is a combination of the following mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset making it read-only.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.team import Team
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
    api_instance = avis_client.TeamApi(api_client)
    id = 56 # int | A unique integer value identifying this team.

    try:
        api_response = api_instance.team_retrieve(id)
        print("The response of TeamApi->team_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. |

### Return type

[**Team**](Team.md)

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

# **team_update**
> Team team_update(id, team_request)



A base read-only viewset that enables optimized queryset fetching and tracing.  This is a combination of the following mixins: * OptimizedQuerySetMixin (from drf_jsonmask): allows the client to specify which fields to return by exposing a `fields` query parameter. If this parameter is not specified, all fields are returned. If it is specified, only the specified fields are returned and the other fields are not fetched from the database. * TracedModelViewSetMixin (from vue_instrumentation): adds tracing to the viewset's methods. * ListModelMixin, RetrieveModelMixin  (from django-rest-framework): adds a list and retrieve method to the viewset making it read-only.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.team import Team
from avis_client.models.team_request import TeamRequest
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
    api_instance = avis_client.TeamApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    team_request = avis_client.TeamRequest() # TeamRequest |

    try:
        api_response = api_instance.team_update(id, team_request)
        print("The response of TeamApi->team_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. |
 **team_request** | [**TeamRequest**](TeamRequest.md)|  |

### Return type

[**Team**](Team.md)

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
