# RatingInspectionResult


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
**rating** | **decimal.Decimal** |  |

## Example

```python
from vue_avis_client.models.rating_inspection_result import RatingInspectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of RatingInspectionResult from a JSON string
rating_inspection_result_instance = RatingInspectionResult.from_json(json)
# print the JSON string representation of the object
print RatingInspectionResult.to_json()

# convert the object into a dict
rating_inspection_result_dict = rating_inspection_result_instance.to_dict()
# create an instance of RatingInspectionResult from a dict
rating_inspection_result_form_dict = rating_inspection_result.from_dict(rating_inspection_result_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
