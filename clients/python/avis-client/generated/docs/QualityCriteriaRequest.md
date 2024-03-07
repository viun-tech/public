# QualityCriteriaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**configurations** | **List[int]** |  | [optional] 
**good_quality_classes** | **List[str]** |  | 
**uncertain_quality_classes** | **List[str]** |  | 
**bad_quality_classes** | **List[str]** |  | 

## Example

```python
from avis_client.models.quality_criteria_request import QualityCriteriaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QualityCriteriaRequest from a JSON string
quality_criteria_request_instance = QualityCriteriaRequest.from_json(json)
# print the JSON string representation of the object
print QualityCriteriaRequest.to_json()

# convert the object into a dict
quality_criteria_request_dict = quality_criteria_request_instance.to_dict()
# create an instance of QualityCriteriaRequest from a dict
quality_criteria_request_form_dict = quality_criteria_request.from_dict(quality_criteria_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


