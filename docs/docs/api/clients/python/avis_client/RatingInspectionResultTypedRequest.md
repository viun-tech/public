# RatingInspectionResultTypedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | **str** |  |
**confidence** | **decimal.Decimal** |  |
**comment** | **str** |  | [optional]
**rating** | **decimal.Decimal** |  |

## Example

```python
from avis_client.models.rating_inspection_result_typed_request import RatingInspectionResultTypedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatingInspectionResultTypedRequest from a JSON string
rating_inspection_result_typed_request_instance = RatingInspectionResultTypedRequest.from_json(json)
# print the JSON string representation of the object
print RatingInspectionResultTypedRequest.to_json()

# convert the object into a dict
rating_inspection_result_typed_request_dict = rating_inspection_result_typed_request_instance.to_dict()
# create an instance of RatingInspectionResultTypedRequest from a dict
rating_inspection_result_typed_request_form_dict = rating_inspection_result_typed_request.from_dict(rating_inspection_result_typed_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
