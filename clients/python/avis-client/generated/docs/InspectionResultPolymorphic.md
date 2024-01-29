# InspectionResultPolymorphic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**confidence** | **decimal.Decimal** |  | 
**comment** | **str** |  | [optional] 
**rating** | **decimal.Decimal** |  | 
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional] 

## Example

```python
from avis_client.models.inspection_result_polymorphic import InspectionResultPolymorphic

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionResultPolymorphic from a JSON string
inspection_result_polymorphic_instance = InspectionResultPolymorphic.from_json(json)
# print the JSON string representation of the object
print InspectionResultPolymorphic.to_json()

# convert the object into a dict
inspection_result_polymorphic_dict = inspection_result_polymorphic_instance.to_dict()
# create an instance of InspectionResultPolymorphic from a dict
inspection_result_polymorphic_form_dict = inspection_result_polymorphic.from_dict(inspection_result_polymorphic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


