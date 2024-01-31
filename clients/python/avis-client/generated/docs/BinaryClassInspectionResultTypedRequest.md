# BinaryClassInspectionResultTypedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**type** | **str** |  | 
**confidence** | **decimal.Decimal** |  | 
**comment** | **str** |  | [optional] 
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional] 

## Example

```python
from avis_client.models.binary_class_inspection_result_typed_request import BinaryClassInspectionResultTypedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryClassInspectionResultTypedRequest from a JSON string
binary_class_inspection_result_typed_request_instance = BinaryClassInspectionResultTypedRequest.from_json(json)
# print the JSON string representation of the object
print BinaryClassInspectionResultTypedRequest.to_json()

# convert the object into a dict
binary_class_inspection_result_typed_request_dict = binary_class_inspection_result_typed_request_instance.to_dict()
# create an instance of BinaryClassInspectionResultTypedRequest from a dict
binary_class_inspection_result_typed_request_form_dict = binary_class_inspection_result_typed_request.from_dict(binary_class_inspection_result_typed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


