# avis_client.ApiKeysApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_create**](ApiKeysApi.md#api_key_create) | **POST** /api/api-keys/ |
[**api_key_revoke**](ApiKeysApi.md#api_key_revoke) | **POST** /api/api-keys/{id}/revoke/ |


# **api_key_create**
> UserAPIKeyCreate api_key_create(credentials_request)



Create a new API key for the current user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.credentials_request import CredentialsRequest
from avis_client.models.user_api_key_create import UserAPIKeyCreate
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.ApiKeysApi(api_client)
    credentials_request = avis_client.CredentialsRequest() # CredentialsRequest |

    try:
        api_response = api_instance.api_key_create(credentials_request)
        print("The response of ApiKeysApi->api_key_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_key_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  |

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_revoke**
> UserAPIKeyCreate api_key_revoke(id, credentials_request)



Revoke an API key for the current user. We use the name of the API Key to revoke it, not the ID or actual key to prevent information leakage.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.credentials_request import CredentialsRequest
from avis_client.models.user_api_key_create import UserAPIKeyCreate
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with avis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avis_client.ApiKeysApi(api_client)
    id = 'id_example' # str | A unique value identifying this API key.
    credentials_request = avis_client.CredentialsRequest() # CredentialsRequest |

    try:
        api_response = api_instance.api_key_revoke(id, credentials_request)
        print("The response of ApiKeysApi->api_key_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_key_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this API key. |
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  |

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
