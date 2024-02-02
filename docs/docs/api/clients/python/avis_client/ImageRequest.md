# ImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**case** | **int** |  | [optional]
**uploaded_by** | **int** |  | [optional]
**inspection_results** | **List[int]** |  | [optional]
**format** | [**FormatEnum**](FormatEnum.md) |  | [optional]
**capture_datetime** | **datetime** |  |
**file** | **bytearray** |  |
**part_id** | **str** |  | [optional]
**validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md) |  | [optional]

## Example

```python
from avis_client.models.image_request import ImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageRequest from a JSON string
image_request_instance = ImageRequest.from_json(json)
# print the JSON string representation of the object
print ImageRequest.to_json()

# convert the object into a dict
image_request_dict = image_request_instance.to_dict()
# create an instance of ImageRequest from a dict
image_request_form_dict = image_request.from_dict(image_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
