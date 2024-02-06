# MembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  |

## Example

```python
from avis_client.models.membership_request import MembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipRequest from a JSON string
membership_request_instance = MembershipRequest.from_json(json)
# print the JSON string representation of the object
print MembershipRequest.to_json()

# convert the object into a dict
membership_request_dict = membership_request_instance.to_dict()
# create an instance of MembershipRequest from a dict
membership_request_form_dict = membership_request.from_dict(membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
