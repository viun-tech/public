# QualityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**configurations** | **List[int]** |  | [optional] 
**good_quality_classes** | **List[str]** |  | 
**uncertain_quality_classes** | **List[str]** |  | 
**bad_quality_classes** | **List[str]** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from avis_client.models.quality_criteria import QualityCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of QualityCriteria from a JSON string
quality_criteria_instance = QualityCriteria.from_json(json)
# print the JSON string representation of the object
print QualityCriteria.to_json()

# convert the object into a dict
quality_criteria_dict = quality_criteria_instance.to_dict()
# create an instance of QualityCriteria from a dict
quality_criteria_form_dict = quality_criteria.from_dict(quality_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


