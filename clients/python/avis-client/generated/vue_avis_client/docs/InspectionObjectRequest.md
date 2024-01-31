# InspectionObjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**type** | **int** |  | [optional] 
**cases** | **List[int]** |  | [optional] 
**identifier** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.inspection_object_request import InspectionObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionObjectRequest from a JSON string
inspection_object_request_instance = InspectionObjectRequest.from_json(json)
# print the JSON string representation of the object
print InspectionObjectRequest.to_json()

# convert the object into a dict
inspection_object_request_dict = inspection_object_request_instance.to_dict()
# create an instance of InspectionObjectRequest from a dict
inspection_object_request_form_dict = inspection_object_request.from_dict(inspection_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


