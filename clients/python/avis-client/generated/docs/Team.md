# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**name** | **str** |  |
**slug** | **str** |  |
**customer** | **int** |  | [optional]
**subscription** | **int** |  | [optional]
**members** | **List[int]** |  | [readonly]

## Example

```python
from avis_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
