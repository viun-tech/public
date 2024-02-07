# ImageQualityGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**blueprints** | **List[int]** |  | [optional]
**good_quality_classes** | **List[str]** |  |
**uncertain_quality_classes** | **List[str]** |  |
**bad_quality_classes** | **List[str]** |  |
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]

## Example

```python
from avis_client.models.image_quality_gate import ImageQualityGate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageQualityGate from a JSON string
image_quality_gate_instance = ImageQualityGate.from_json(json)
# print the JSON string representation of the object
print ImageQualityGate.to_json()

# convert the object into a dict
image_quality_gate_dict = image_quality_gate_instance.to_dict()
# create an instance of ImageQualityGate from a dict
image_quality_gate_form_dict = image_quality_gate.from_dict(image_quality_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
