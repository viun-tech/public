# CaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**inspection_object** | **int** |  | [optional]
**opened_by** | **int** |  | [optional]
**closed_by** | **int** |  | [optional]
**images** | **List[int]** |  | [optional]
**close_datetime** | **datetime** |  | [optional]
**blueprint** | **int** |  | [optional]
**metadata** | **int** |  | [optional]

## Example

```python
from avis_client.models.case_request import CaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseRequest from a JSON string
case_request_instance = CaseRequest.from_json(json)
# print the JSON string representation of the object
print CaseRequest.to_json()

# convert the object into a dict
case_request_dict = case_request_instance.to_dict()
# create an instance of CaseRequest from a dict
case_request_form_dict = case_request.from_dict(case_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
