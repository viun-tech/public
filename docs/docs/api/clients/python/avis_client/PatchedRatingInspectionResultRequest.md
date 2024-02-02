# PatchedRatingInspectionResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**reported_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional]
**confidence** | **decimal.Decimal** |  | [optional]
**comment** | **str** |  | [optional]
**rating** | **decimal.Decimal** |  | [optional]

## Example

```python
from avis_client.models.patched_rating_inspection_result_request import PatchedRatingInspectionResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRatingInspectionResultRequest from a JSON string
patched_rating_inspection_result_request_instance = PatchedRatingInspectionResultRequest.from_json(json)
# print the JSON string representation of the object
print PatchedRatingInspectionResultRequest.to_json()

# convert the object into a dict
patched_rating_inspection_result_request_dict = patched_rating_inspection_result_request_instance.to_dict()
# create an instance of PatchedRatingInspectionResultRequest from a dict
patched_rating_inspection_result_request_form_dict = patched_rating_inspection_result_request.from_dict(patched_rating_inspection_result_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
