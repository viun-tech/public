# InspectionResultPolymorphicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**confidence** | **decimal.Decimal** |  | 
**comment** | **str** |  | [optional] 
**rating** | **decimal.Decimal** |  | 
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional] 

## Example

```python
from avis_client.models.inspection_result_polymorphic_request import InspectionResultPolymorphicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionResultPolymorphicRequest from a JSON string
inspection_result_polymorphic_request_instance = InspectionResultPolymorphicRequest.from_json(json)
# print the JSON string representation of the object
print InspectionResultPolymorphicRequest.to_json()

# convert the object into a dict
inspection_result_polymorphic_request_dict = inspection_result_polymorphic_request_instance.to_dict()
# create an instance of InspectionResultPolymorphicRequest from a dict
inspection_result_polymorphic_request_form_dict = inspection_result_polymorphic_request.from_dict(inspection_result_polymorphic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


