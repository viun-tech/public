# UserAPIKeyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [readonly]
**created** | **datetime** |  | [readonly]
**name** | **str** | A free-form name for the API key. Need not be unique. 50 characters max. | [readonly]
**expiry_date** | **datetime** | Once API key expires, clients cannot use it anymore. | [readonly]
**revoked** | **bool** |  | [readonly]
**message** | **str** |  | [readonly]

## Example

```python
from avis_client.models.user_api_key_create import UserAPIKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserAPIKeyCreate from a JSON string
user_api_key_create_instance = UserAPIKeyCreate.from_json(json)
# print the JSON string representation of the object
print UserAPIKeyCreate.to_json()

# convert the object into a dict
user_api_key_create_dict = user_api_key_create_instance.to_dict()
# create an instance of UserAPIKeyCreate from a dict
user_api_key_create_form_dict = user_api_key_create.from_dict(user_api_key_create_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
