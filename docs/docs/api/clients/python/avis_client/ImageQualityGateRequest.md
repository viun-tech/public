# ImageQualityGateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**blueprints** | **List[int]** |  | [optional]
**good_quality_classes** | **List[str]** |  |
**uncertain_quality_classes** | **List[str]** |  |
**bad_quality_classes** | **List[str]** |  |

## Example

```python
from avis_client.models.image_quality_gate_request import ImageQualityGateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageQualityGateRequest from a JSON string
image_quality_gate_request_instance = ImageQualityGateRequest.from_json(json)
# print the JSON string representation of the object
print ImageQualityGateRequest.to_json()

# convert the object into a dict
image_quality_gate_request_dict = image_quality_gate_request_instance.to_dict()
# create an instance of ImageQualityGateRequest from a dict
image_quality_gate_request_form_dict = image_quality_gate_request.from_dict(image_quality_gate_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
