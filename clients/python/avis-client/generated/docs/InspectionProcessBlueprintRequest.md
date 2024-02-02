# InspectionProcessBlueprintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**name** | **str** |  | 
**metadata_schema** | **int** |  | [optional] 
**image_quality_gate** | **int** |  | [optional] 
**ml_model** | **int** |  | [optional] 
**inspection_object_type** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.inspection_process_blueprint_request import InspectionProcessBlueprintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionProcessBlueprintRequest from a JSON string
inspection_process_blueprint_request_instance = InspectionProcessBlueprintRequest.from_json(json)
# print the JSON string representation of the object
print InspectionProcessBlueprintRequest.to_json()

# convert the object into a dict
inspection_process_blueprint_request_dict = inspection_process_blueprint_request_instance.to_dict()
# create an instance of InspectionProcessBlueprintRequest from a dict
inspection_process_blueprint_request_form_dict = inspection_process_blueprint_request.from_dict(inspection_process_blueprint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


