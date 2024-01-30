# PatchedRatingInspectionResultTypedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**reported_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**confidence** | **decimal.Decimal** |  | [optional] 
**comment** | **str** |  | [optional] 
**rating** | **decimal.Decimal** |  | [optional] 

## Example

```python
from vue_avis_client.models.patched_rating_inspection_result_typed_request import PatchedRatingInspectionResultTypedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRatingInspectionResultTypedRequest from a JSON string
patched_rating_inspection_result_typed_request_instance = PatchedRatingInspectionResultTypedRequest.from_json(json)
# print the JSON string representation of the object
print PatchedRatingInspectionResultTypedRequest.to_json()

# convert the object into a dict
patched_rating_inspection_result_typed_request_dict = patched_rating_inspection_result_typed_request_instance.to_dict()
# create an instance of PatchedRatingInspectionResultTypedRequest from a dict
patched_rating_inspection_result_typed_request_form_dict = patched_rating_inspection_result_typed_request.from_dict(patched_rating_inspection_result_typed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


