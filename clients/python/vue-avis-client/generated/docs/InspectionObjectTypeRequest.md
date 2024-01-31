# InspectionObjectTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**instances** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.inspection_object_type_request import InspectionObjectTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionObjectTypeRequest from a JSON string
inspection_object_type_request_instance = InspectionObjectTypeRequest.from_json(json)
# print the JSON string representation of the object
print InspectionObjectTypeRequest.to_json()

# convert the object into a dict
inspection_object_type_request_dict = inspection_object_type_request_instance.to_dict()
# create an instance of InspectionObjectTypeRequest from a dict
inspection_object_type_request_form_dict = inspection_object_type_request.from_dict(inspection_object_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


