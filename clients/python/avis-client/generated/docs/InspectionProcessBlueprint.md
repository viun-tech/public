# InspectionProcessBlueprint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**name** | **str** |  |
**metadata_schema** | **int** |  | [optional]
**image_quality_gate** | **int** |  | [optional]
**ml_model** | **int** |  | [optional]
**inspection_object_type** | **int** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**description** | **str** |  | [optional]

## Example

```python
from avis_client.models.inspection_process_blueprint import InspectionProcessBlueprint

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionProcessBlueprint from a JSON string
inspection_process_blueprint_instance = InspectionProcessBlueprint.from_json(json)
# print the JSON string representation of the object
print InspectionProcessBlueprint.to_json()

# convert the object into a dict
inspection_process_blueprint_dict = inspection_process_blueprint_instance.to_dict()
# create an instance of InspectionProcessBlueprint from a dict
inspection_process_blueprint_form_dict = inspection_process_blueprint.from_dict(inspection_process_blueprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
