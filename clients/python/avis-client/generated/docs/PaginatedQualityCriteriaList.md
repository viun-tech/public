# PaginatedQualityCriteriaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QualityCriteria]**](QualityCriteria.md) |  | 

## Example

```python
from avis_client.models.paginated_quality_criteria_list import PaginatedQualityCriteriaList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQualityCriteriaList from a JSON string
paginated_quality_criteria_list_instance = PaginatedQualityCriteriaList.from_json(json)
# print the JSON string representation of the object
print PaginatedQualityCriteriaList.to_json()

# convert the object into a dict
paginated_quality_criteria_list_dict = paginated_quality_criteria_list_instance.to_dict()
# create an instance of PaginatedQualityCriteriaList from a dict
paginated_quality_criteria_list_form_dict = paginated_quality_criteria_list.from_dict(paginated_quality_criteria_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


