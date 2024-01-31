# ImageQualityGateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**quality** | [**QualityEnum**](QualityEnum.md) |  | 
**quality_gate** | **int** |  | 

## Example

```python
from avis_client.models.image_quality_gate_result import ImageQualityGateResult

# TODO update the JSON string below
json = "{}"
# create an instance of ImageQualityGateResult from a JSON string
image_quality_gate_result_instance = ImageQualityGateResult.from_json(json)
# print the JSON string representation of the object
print ImageQualityGateResult.to_json()

# convert the object into a dict
image_quality_gate_result_dict = image_quality_gate_result_instance.to_dict()
# create an instance of ImageQualityGateResult from a dict
image_quality_gate_result_form_dict = image_quality_gate_result.from_dict(image_quality_gate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


