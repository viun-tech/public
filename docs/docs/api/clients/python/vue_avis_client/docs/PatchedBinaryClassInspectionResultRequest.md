# PatchedBinaryClassInspectionResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional]
**confidence** | **decimal.Decimal** |  | [optional]
**comment** | **str** |  | [optional]
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional]

## Example

```python
from vue_avis_client.models.patched_binary_class_inspection_result_request import PatchedBinaryClassInspectionResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBinaryClassInspectionResultRequest from a JSON string
patched_binary_class_inspection_result_request_instance = PatchedBinaryClassInspectionResultRequest.from_json(json)
# print the JSON string representation of the object
print PatchedBinaryClassInspectionResultRequest.to_json()

# convert the object into a dict
patched_binary_class_inspection_result_request_dict = patched_binary_class_inspection_result_request_instance.to_dict()
# create an instance of PatchedBinaryClassInspectionResultRequest from a dict
patched_binary_class_inspection_result_request_form_dict = patched_binary_class_inspection_result_request.from_dict(patched_binary_class_inspection_result_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
