# PatchedQualityCriteriaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**configurations** | **List[int]** |  | [optional] 
**good_quality_classes** | **List[str]** |  | [optional] 
**uncertain_quality_classes** | **List[str]** |  | [optional] 
**bad_quality_classes** | **List[str]** |  | [optional] 

## Example

```python
from avis_client.models.patched_quality_criteria_request import PatchedQualityCriteriaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedQualityCriteriaRequest from a JSON string
patched_quality_criteria_request_instance = PatchedQualityCriteriaRequest.from_json(json)
# print the JSON string representation of the object
print PatchedQualityCriteriaRequest.to_json()

# convert the object into a dict
patched_quality_criteria_request_dict = patched_quality_criteria_request_instance.to_dict()
# create an instance of PatchedQualityCriteriaRequest from a dict
patched_quality_criteria_request_form_dict = patched_quality_criteria_request.from_dict(patched_quality_criteria_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


