# InspectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  |
**inspection_status** | [**InspectionStatusEnum**](InspectionStatusEnum.md) |  |

## Example

```python
from avis_client.models.inspection_status import InspectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionStatus from a JSON string
inspection_status_instance = InspectionStatus.from_json(json)
# print the JSON string representation of the object
print InspectionStatus.to_json()

# convert the object into a dict
inspection_status_dict = inspection_status_instance.to_dict()
# create an instance of InspectionStatus from a dict
inspection_status_form_dict = inspection_status.from_dict(inspection_status_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
