# RatingInspectionResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional]
**confidence** | **decimal.Decimal** |  |
**comment** | **str** |  | [optional]
**rating** | **decimal.Decimal** |  |

## Example

```python
from avis_client.models.rating_inspection_result_request import RatingInspectionResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatingInspectionResultRequest from a JSON string
rating_inspection_result_request_instance = RatingInspectionResultRequest.from_json(json)
# print the JSON string representation of the object
print RatingInspectionResultRequest.to_json()

# convert the object into a dict
rating_inspection_result_request_dict = rating_inspection_result_request_instance.to_dict()
# create an instance of RatingInspectionResultRequest from a dict
rating_inspection_result_request_form_dict = rating_inspection_result_request.from_dict(rating_inspection_result_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
