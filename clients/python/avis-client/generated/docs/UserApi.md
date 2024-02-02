# avis_client.UserApi

All URIs are relative to *https://avis.vu.engineering*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_email_list**](UserApi.md#user_email_list) | **GET** /api/user/email/ |
[**user_whoami_retrieve**](UserApi.md#user_whoami_retrieve) | **GET** /api/user/whoami/ |


# **user_email_list**
> List[EmailAddress] user_email_list()



Get all email addresses associated with the current user.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.email_address import EmailAddress
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
    api_instance = avis_client.UserApi(api_client)

    try:
        api_response = api_instance.user_email_list()
        print("The response of UserApi->user_email_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_email_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EmailAddress]**](EmailAddress.md)

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

# **user_whoami_retrieve**
> CustomUser user_whoami_retrieve()



Get the current user's information.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import avis_client
from avis_client.models.custom_user import CustomUser
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
    api_instance = avis_client.UserApi(api_client)

    try:
        api_response = api_instance.user_whoami_retrieve()
        print("The response of UserApi->user_whoami_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_whoami_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomUser**](CustomUser.md)

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
