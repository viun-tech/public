# AzureMLInferenceRequest

Serializer for Azure ML inference requests. This corresponds to the schema of the request body that Azure ML expects. See https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models?view=azureml-api-2&tabs=azureml#input-structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_data** | **object** |  | 
**params** | **object** |  | [optional] 

## Example

```python
from avis_client.models.azure_ml_inference_request import AzureMLInferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMLInferenceRequest from a JSON string
azure_ml_inference_request_instance = AzureMLInferenceRequest.from_json(json)
# print the JSON string representation of the object
print AzureMLInferenceRequest.to_json()

# convert the object into a dict
azure_ml_inference_request_dict = azure_ml_inference_request_instance.to_dict()
# create an instance of AzureMLInferenceRequest from a dict
azure_ml_inference_request_form_dict = azure_ml_inference_request.from_dict(azure_ml_inference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


