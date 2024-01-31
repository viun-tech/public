# RatingInspectionResultTyped


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
**rating** | **decimal.Decimal** |  | 

## Example

```python
from vue_avis_client.models.rating_inspection_result_typed import RatingInspectionResultTyped

# TODO update the JSON string below
json = "{}"
# create an instance of RatingInspectionResultTyped from a JSON string
rating_inspection_result_typed_instance = RatingInspectionResultTyped.from_json(json)
# print the JSON string representation of the object
print RatingInspectionResultTyped.to_json()

# convert the object into a dict
rating_inspection_result_typed_dict = rating_inspection_result_typed_instance.to_dict()
# create an instance of RatingInspectionResultTyped from a dict
rating_inspection_result_typed_form_dict = rating_inspection_result_typed.from_dict(rating_inspection_result_typed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


