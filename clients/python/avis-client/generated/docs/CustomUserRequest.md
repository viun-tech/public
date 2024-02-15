# CustomUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from avis_client.models.custom_user_request import CustomUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomUserRequest from a JSON string
custom_user_request_instance = CustomUserRequest.from_json(json)
# print the JSON string representation of the object
print CustomUserRequest.to_json()

# convert the object into a dict
custom_user_request_dict = custom_user_request_instance.to_dict()
# create an instance of CustomUserRequest from a dict
custom_user_request_form_dict = custom_user_request.from_dict(custom_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


