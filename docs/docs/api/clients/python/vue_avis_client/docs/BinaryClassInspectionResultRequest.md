# BinaryClassInspectionResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional]
**confidence** | **decimal.Decimal** |  |
**comment** | **str** |  | [optional]
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional]

## Example

```python
from vue_avis_client.models.binary_class_inspection_result_request import BinaryClassInspectionResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryClassInspectionResultRequest from a JSON string
binary_class_inspection_result_request_instance = BinaryClassInspectionResultRequest.from_json(json)
# print the JSON string representation of the object
print BinaryClassInspectionResultRequest.to_json()

# convert the object into a dict
binary_class_inspection_result_request_dict = binary_class_inspection_result_request_instance.to_dict()
# create an instance of BinaryClassInspectionResultRequest from a dict
binary_class_inspection_result_request_form_dict = binary_class_inspection_result_request.from_dict(binary_class_inspection_result_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
