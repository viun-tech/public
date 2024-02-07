# Membership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**user** | [**CustomUser**](CustomUser.md) |  | [readonly]
**role** | **str** |  |
**team** | **int** |  | [readonly]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]

## Example

```python
from avis_client.models.membership import Membership

# TODO update the JSON string below
json = "{}"
# create an instance of Membership from a JSON string
membership_instance = Membership.from_json(json)
# print the JSON string representation of the object
print Membership.to_json()

# convert the object into a dict
membership_dict = membership_instance.to_dict()
# create an instance of Membership from a dict
membership_form_dict = membership.from_dict(membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
