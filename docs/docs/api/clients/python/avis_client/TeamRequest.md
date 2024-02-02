# TeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**slug** | **str** |  |
**customer** | **int** |  | [optional]
**subscription** | **int** |  | [optional]

## Example

```python
from avis_client.models.team_request import TeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRequest from a JSON string
team_request_instance = TeamRequest.from_json(json)
# print the JSON string representation of the object
print TeamRequest.to_json()

# convert the object into a dict
team_request_dict = team_request_instance.to_dict()
# create an instance of TeamRequest from a dict
team_request_form_dict = team_request.from_dict(team_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
