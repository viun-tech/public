# PaginatedImageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]
**results** | [**List[Image]**](Image.md) |  |

## Example

```python
from avis_client.models.paginated_image_list import PaginatedImageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedImageList from a JSON string
paginated_image_list_instance = PaginatedImageList.from_json(json)
# print the JSON string representation of the object
print PaginatedImageList.to_json()

# convert the object into a dict
paginated_image_list_dict = paginated_image_list_instance.to_dict()
# create an instance of PaginatedImageList from a dict
paginated_image_list_form_dict = paginated_image_list.from_dict(paginated_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
