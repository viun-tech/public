# vue_avis_client.MembershipApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_list**](MembershipApi.md#membership_list) | **GET** /api/membership/ |


# **membership_list**
> List[Membership] membership_list()



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import vue_avis_client
from vue_avis_client.models.membership import Membership
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
    api_instance = vue_avis_client.MembershipApi(api_client)

    try:
        api_response = api_instance.membership_list()
        print("The response of MembershipApi->membership_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Membership]**](Membership.md)

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
