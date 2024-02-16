# InspectionValidationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md) |  | 

## Example

```python
from avis_client.models.inspection_validation_status import InspectionValidationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionValidationStatus from a JSON string
inspection_validation_status_instance = InspectionValidationStatus.from_json(json)
# print the JSON string representation of the object
print InspectionValidationStatus.to_json()

# convert the object into a dict
inspection_validation_status_dict = inspection_validation_status_instance.to_dict()
# create an instance of InspectionValidationStatus from a dict
inspection_validation_status_form_dict = inspection_validation_status.from_dict(inspection_validation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


