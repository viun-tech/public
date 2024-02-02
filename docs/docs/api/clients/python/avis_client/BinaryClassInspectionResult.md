# BinaryClassInspectionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**confidence** | **decimal.Decimal** |  |
**comment** | **str** |  | [optional]
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional]

## Example

```python
from avis_client.models.binary_class_inspection_result import BinaryClassInspectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryClassInspectionResult from a JSON string
binary_class_inspection_result_instance = BinaryClassInspectionResult.from_json(json)
# print the JSON string representation of the object
print BinaryClassInspectionResult.to_json()

# convert the object into a dict
binary_class_inspection_result_dict = binary_class_inspection_result_instance.to_dict()
# create an instance of BinaryClassInspectionResult from a dict
binary_class_inspection_result_form_dict = binary_class_inspection_result.from_dict(binary_class_inspection_result_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
