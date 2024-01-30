# Generating the clients

To generate the clients you will need to
install [openapi-generator](https://github.com/OpenAPITools/openapi-generator):
which requires [Java](https://www.java.com/en/download/) to be installed on your system. You can then install the cli
with:

```commandline
npm install @openapitools/openapi-generator-cli -g
```

Then pick the API version you'd like to generate the client for:

```commandline
API_VERSION=v1
```

## Python

```commandline
openapi-generator-cli generate --global-property apiTests=false,modelTests=false -i "$API_VERSION/api-schema.yml" -g python -o "$API_VERSION/python/vue-avis-client/generated" --additional-properties=packageName=vue_avis_client,generateSourceCodeOnly=true
```

## Typescript (using Axios)

```commandline
openapi-generator-cli generate -i "$API_VERSION/api-schema.yml" -g typescript-axios -o "$API_VERSION/typescript/vue-avis-axios-client/generated" --additional-properties=withInterfaces=true,npmName=vue-avis-axios-client
```