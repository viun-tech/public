# QualityCriteriaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**quality** | [**QualityEnum**](QualityEnum.md) |  | 
**quality_criteria** | **int** |  | 

## Example

```python
from avis_client.models.quality_criteria_result import QualityCriteriaResult

# TODO update the JSON string below
json = "{}"
# create an instance of QualityCriteriaResult from a JSON string
quality_criteria_result_instance = QualityCriteriaResult.from_json(json)
# print the JSON string representation of the object
print QualityCriteriaResult.to_json()

# convert the object into a dict
quality_criteria_result_dict = quality_criteria_result_instance.to_dict()
# create an instance of QualityCriteriaResult from a dict
quality_criteria_result_form_dict = quality_criteria_result.from_dict(quality_criteria_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


