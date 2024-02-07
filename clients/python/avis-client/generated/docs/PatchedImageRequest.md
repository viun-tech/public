# PatchedImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**case** | **int** |  | [optional]
**uploaded_by** | **int** |  | [optional]
**inspection_results** | **List[int]** |  | [optional]
**format** | [**FormatEnum**](FormatEnum.md) |  | [optional]
**capture_datetime** | **datetime** |  | [optional]
**file** | **bytearray** |  | [optional]
**part_id** | **str** |  | [optional]
**validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md) |  | [optional]

## Example

```python
from avis_client.models.patched_image_request import PatchedImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedImageRequest from a JSON string
patched_image_request_instance = PatchedImageRequest.from_json(json)
# print the JSON string representation of the object
print PatchedImageRequest.to_json()

# convert the object into a dict
patched_image_request_dict = patched_image_request_instance.to_dict()
# create an instance of PatchedImageRequest from a dict
patched_image_request_form_dict = patched_image_request.from_dict(patched_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
