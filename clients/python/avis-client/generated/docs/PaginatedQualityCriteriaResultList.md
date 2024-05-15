# PaginatedQualityCriteriaResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QualityCriteriaResult]**](QualityCriteriaResult.md) |  | 

## Example

```python
from avis_client.models.paginated_quality_criteria_result_list import PaginatedQualityCriteriaResultList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQualityCriteriaResultList from a JSON string
paginated_quality_criteria_result_list_instance = PaginatedQualityCriteriaResultList.from_json(json)
# print the JSON string representation of the object
print PaginatedQualityCriteriaResultList.to_json()

# convert the object into a dict
paginated_quality_criteria_result_list_dict = paginated_quality_criteria_result_list_instance.to_dict()
# create an instance of PaginatedQualityCriteriaResultList from a dict
paginated_quality_criteria_result_list_form_dict = paginated_quality_criteria_result_list.from_dict(paginated_quality_criteria_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


