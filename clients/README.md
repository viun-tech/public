# Generating the clients

To generate the clients you will need to
install [openapi-generator](https://github.com/OpenAPITools/openapi-generator):
which requires [Java](https://www.java.com/en/download/) to be installed on your system. You can then install the cli
with:

```bash
npm install @openapitools/openapi-generator-cli -g
```

You can then use the helper script to generate all the clients:

```bash
./generate-clients.sh <version>
```

Where `<version>` is the version of the clients to be generated.

You can extract the version from the `api-schema.yml` file with the following command:

```bash
VERSION=$(awk '/info:/{flag=1; next}/^ /{if(flag){print}}/^[^ ]/{flag=0}' ../api-schema.yml | grep 'version:' | awk '{print $2}')
./generate-clients.sh $VERSION
```

Or you can generate them one by one. Please note that the author and license fields will need be updated in the generated
files package.json, setup.py, pyproject.toml, ...:

## Python

```bash
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g python -o python/avis-client/generated --additional-properties=packageName=avis_client,packageVersion=0.1.0
```

## Typescript (using Axios)

```bash
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g typescript-axios -o typescript/avis-client/generated --additional-properties=withInterfaces=true,npmName=@vision-unified-tech/avis-client
```
