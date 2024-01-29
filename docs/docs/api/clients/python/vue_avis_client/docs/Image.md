# Image


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**case** | **int** |  | [optional]
**uploaded_by** | **int** |  | [optional]
**inspection_results** | **List[int]** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**format** | [**FormatEnum**](FormatEnum.md) |  | [optional]
**capture_datetime** | **datetime** |  |
**file** | **str** |  |
**part_id** | **str** |  | [optional]
**validation_status** | [**ValidationStatusEnum**](ValidationStatusEnum.md) |  | [optional]

## Example

```python
from vue_avis_client.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print Image.to_json()

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_form_dict = image.from_dict(image_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
