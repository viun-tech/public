# Inspection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**product** | **int** |  | [optional] 
**opened_by** | **int** |  | [optional] 
**closed_by** | **int** |  | [optional] 
**images** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**open_datetime** | **datetime** |  | [readonly] 
**close_datetime** | **datetime** |  | [optional] 
**blueprint** | **int** |  | [optional] 
**metadata** | **int** |  | [optional] 

## Example

```python
from avis_client.models.inspection import Inspection

# TODO update the JSON string below
json = "{}"
# create an instance of Inspection from a JSON string
inspection_instance = Inspection.from_json(json)
# print the JSON string representation of the object
print Inspection.to_json()

# convert the object into a dict
inspection_dict = inspection_instance.to_dict()
# create an instance of Inspection from a dict
inspection_form_dict = inspection.from_dict(inspection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


