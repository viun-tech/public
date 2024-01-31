# PatchedInspectionResultPolymorphicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional] 
**team** | **int** |  | [optional] 
**reported_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**confidence** | **decimal.Decimal** |  | [optional] 
**comment** | **str** |  | [optional] 
**rating** | **decimal.Decimal** |  | [optional] 
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional] 

## Example

```python
from vue_avis_client.models.patched_inspection_result_polymorphic_request import PatchedInspectionResultPolymorphicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionResultPolymorphicRequest from a JSON string
patched_inspection_result_polymorphic_request_instance = PatchedInspectionResultPolymorphicRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionResultPolymorphicRequest.to_json()

# convert the object into a dict
patched_inspection_result_polymorphic_request_dict = patched_inspection_result_polymorphic_request_instance.to_dict()
# create an instance of PatchedInspectionResultPolymorphicRequest from a dict
patched_inspection_result_polymorphic_request_form_dict = patched_inspection_result_polymorphic_request.from_dict(patched_inspection_result_polymorphic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


