# BinaryClassInspectionResultTyped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | **str** |  |
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**confidence** | **decimal.Decimal** |  |
**comment** | **str** |  | [optional]
**binary_class** | [**BinaryClassEnum**](BinaryClassEnum.md) |  | [optional]

## Example

```python
from avis_client.models.binary_class_inspection_result_typed import BinaryClassInspectionResultTyped

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryClassInspectionResultTyped from a JSON string
binary_class_inspection_result_typed_instance = BinaryClassInspectionResultTyped.from_json(json)
# print the JSON string representation of the object
print BinaryClassInspectionResultTyped.to_json()

# convert the object into a dict
binary_class_inspection_result_typed_dict = binary_class_inspection_result_typed_instance.to_dict()
# create an instance of BinaryClassInspectionResultTyped from a dict
binary_class_inspection_result_typed_form_dict = binary_class_inspection_result_typed.from_dict(binary_class_inspection_result_typed_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
