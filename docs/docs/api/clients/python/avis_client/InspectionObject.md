# InspectionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**type** | **int** |  | [optional]
**cases** | **List[int]** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**identifier** | **str** |  |
**display_name** | **str** |  | [optional]
**description** | **str** |  | [optional]

## Example

```python
from avis_client.models.inspection_object import InspectionObject

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionObject from a JSON string
inspection_object_instance = InspectionObject.from_json(json)
# print the JSON string representation of the object
print InspectionObject.to_json()

# convert the object into a dict
inspection_object_dict = inspection_object_instance.to_dict()
# create an instance of InspectionObject from a dict
inspection_object_form_dict = inspection_object.from_dict(inspection_object_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
