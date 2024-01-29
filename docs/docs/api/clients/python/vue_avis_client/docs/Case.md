# Case


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**inspection_object** | **int** |  | [optional]
**opened_by** | **int** |  | [optional]
**closed_by** | **int** |  | [optional]
**images** | **List[int]** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**open_datetime** | **datetime** |  | [readonly]
**close_datetime** | **datetime** |  | [optional]
**blueprint** | **int** |  | [optional]
**metadata** | **int** |  | [optional]

## Example

```python
from vue_avis_client.models.case import Case

# TODO update the JSON string below
json = "{}"
# create an instance of Case from a JSON string
case_instance = Case.from_json(json)
# print the JSON string representation of the object
print Case.to_json()

# convert the object into a dict
case_dict = case_instance.to_dict()
# create an instance of Case from a dict
case_form_dict = case.from_dict(case_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
