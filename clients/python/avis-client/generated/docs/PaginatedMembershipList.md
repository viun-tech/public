# PaginatedMembershipList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]
**results** | [**List[Membership]**](Membership.md) |  |

## Example

```python
from avis_client.models.paginated_membership_list import PaginatedMembershipList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMembershipList from a JSON string
paginated_membership_list_instance = PaginatedMembershipList.from_json(json)
# print the JSON string representation of the object
print PaginatedMembershipList.to_json()

# convert the object into a dict
paginated_membership_list_dict = paginated_membership_list_instance.to_dict()
# create an instance of PaginatedMembershipList from a dict
paginated_membership_list_form_dict = paginated_membership_list.from_dict(paginated_membership_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
