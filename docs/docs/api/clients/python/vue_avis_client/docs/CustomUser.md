# CustomUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**first_name** | **str** |  | [optional]
**last_name** | **str** |  | [optional]
**email** | **str** |  | [optional]

## Example

```python
from vue_avis_client.models.custom_user import CustomUser

# TODO update the JSON string below
json = "{}"
# create an instance of CustomUser from a JSON string
custom_user_instance = CustomUser.from_json(json)
# print the JSON string representation of the object
print CustomUser.to_json()

# convert the object into a dict
custom_user_dict = custom_user_instance.to_dict()
# create an instance of CustomUser from a dict
custom_user_form_dict = custom_user.from_dict(custom_user_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
