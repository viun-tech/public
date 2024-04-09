# PaginatedTeamList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_team_list import PaginatedTeamList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTeamList from a JSON string
paginated_team_list_instance = PaginatedTeamList.from_json(json)
# print the JSON string representation of the object
print PaginatedTeamList.to_json()

# convert the object into a dict
paginated_team_list_dict = paginated_team_list_instance.to_dict()
# create an instance of PaginatedTeamList from a dict
paginated_team_list_form_dict = paginated_team_list.from_dict(paginated_team_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


