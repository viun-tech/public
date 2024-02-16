# InspectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**product** | **int** |  | [optional] 
**opened_by** | **int** |  | [optional] 
**closed_by** | **int** |  | [optional] 
**images** | **List[int]** |  | [optional] 
**close_datetime** | **datetime** |  | [optional] 
**blueprint** | **int** |  | [optional] 
**metadata** | **int** |  | [optional] 

## Example

```python
from avis_client.models.inspection_request import InspectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionRequest from a JSON string
inspection_request_instance = InspectionRequest.from_json(json)
# print the JSON string representation of the object
print InspectionRequest.to_json()

# convert the object into a dict
inspection_request_dict = inspection_request_instance.to_dict()
# create an instance of InspectionRequest from a dict
inspection_request_form_dict = inspection_request.from_dict(inspection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


