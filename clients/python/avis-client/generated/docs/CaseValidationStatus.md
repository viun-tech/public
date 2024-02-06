# CaseValidationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  |
**validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md) |  |

## Example

```python
from avis_client.models.case_validation_status import CaseValidationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CaseValidationStatus from a JSON string
case_validation_status_instance = CaseValidationStatus.from_json(json)
# print the JSON string representation of the object
print CaseValidationStatus.to_json()

# convert the object into a dict
case_validation_status_dict = case_validation_status_instance.to_dict()
# create an instance of CaseValidationStatus from a dict
case_validation_status_form_dict = case_validation_status.from_dict(case_validation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
