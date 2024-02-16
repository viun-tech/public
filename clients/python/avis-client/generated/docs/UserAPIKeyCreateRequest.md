# UserAPIKeyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A free-form name for the API key. Need not be unique. 50 characters max. | [optional] 

## Example

```python
from avis_client.models.user_api_key_create_request import UserAPIKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAPIKeyCreateRequest from a JSON string
user_api_key_create_request_instance = UserAPIKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print UserAPIKeyCreateRequest.to_json()

# convert the object into a dict
user_api_key_create_request_dict = user_api_key_create_request_instance.to_dict()
# create an instance of UserAPIKeyCreateRequest from a dict
user_api_key_create_request_form_dict = user_api_key_create_request.from_dict(user_api_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


