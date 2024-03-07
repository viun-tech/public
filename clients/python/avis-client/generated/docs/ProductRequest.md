# ProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**category** | **int** |  | [optional] 
**inspections** | **List[int]** |  | [optional] 
**identifier** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.product_request import ProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRequest from a JSON string
product_request_instance = ProductRequest.from_json(json)
# print the JSON string representation of the object
print ProductRequest.to_json()

# convert the object into a dict
product_request_dict = product_request_instance.to_dict()
# create an instance of ProductRequest from a dict
product_request_form_dict = product_request.from_dict(product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


