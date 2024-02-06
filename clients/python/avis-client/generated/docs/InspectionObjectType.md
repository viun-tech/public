# InspectionObjectType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**instances** | **List[int]** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**name** | **str** |  | [optional]
**display_name** | **str** |  | [optional]
**description** | **str** |  | [optional]

## Example

```python
from avis_client.models.inspection_object_type import InspectionObjectType

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionObjectType from a JSON string
inspection_object_type_instance = InspectionObjectType.from_json(json)
# print the JSON string representation of the object
print InspectionObjectType.to_json()

# convert the object into a dict
inspection_object_type_dict = inspection_object_type_instance.to_dict()
# create an instance of InspectionObjectType from a dict
inspection_object_type_form_dict = inspection_object_type.from_dict(inspection_object_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
