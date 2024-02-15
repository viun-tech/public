# avis_client.ApiKeysApi

All URIs are relative to *https://avis.vu.engineering*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keys_create**](ApiKeysApi.md#keys_create) | **POST** /api/keys/ | 
[**keys_revoke_create**](ApiKeysApi.md#keys_revoke_create) | **POST** /api/keys/revoke/ | 


# **keys_create**
> UserAPIKeyCreate keys_create(user_api_key_create_request=user_api_key_create_request)



Create a new API key for the current user.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.user_api_key_create import UserAPIKeyCreate
from avis_client.models.user_api_key_create_request import UserAPIKeyCreateRequest
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
    api_instance = avis_client.ApiKeysApi(api_client)
    user_api_key_create_request = avis_client.UserAPIKeyCreateRequest() # UserAPIKeyCreateRequest |  (optional)

    try:
        api_response = api_instance.keys_create(user_api_key_create_request=user_api_key_create_request)
        print("The response of ApiKeysApi->keys_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->keys_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_api_key_create_request** | [**UserAPIKeyCreateRequest**](UserAPIKeyCreateRequest.md)|  | [optional] 

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

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

# **keys_revoke_create**
> UserAPIKeyCreate keys_revoke_create(user_api_key_create_request=user_api_key_create_request)



Revoke an API key for the current user. We use the name of the API Key to revoke it, not the ID or actual key to prevent information leakage.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.user_api_key_create import UserAPIKeyCreate
from avis_client.models.user_api_key_create_request import UserAPIKeyCreateRequest
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
    api_instance = avis_client.ApiKeysApi(api_client)
    user_api_key_create_request = avis_client.UserAPIKeyCreateRequest() # UserAPIKeyCreateRequest |  (optional)

    try:
        api_response = api_instance.keys_revoke_create(user_api_key_create_request=user_api_key_create_request)
        print("The response of ApiKeysApi->keys_revoke_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->keys_revoke_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_api_key_create_request** | [**UserAPIKeyCreateRequest**](UserAPIKeyCreateRequest.md)|  | [optional] 

### Return type

[**UserAPIKeyCreate**](UserAPIKeyCreate.md)

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

