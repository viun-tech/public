#!/usr/bin/env bash

# fail on error
set -e

# if a version number is not passed as an argument, fail
if [ -z "$1" ]; then
    echo "Please provide a version number as an argument"
    exit 1
fi

# Function to update files
update_files() {
    local file=$1
    echo "Updating $file"
    case "$file" in
      *.json)
            # Update package.json
            sed -i 's/"author": "[^"]*"/"author": "tech@vu.engineering"/g' "$file"
            sed -i 's/"license": "[^"]*"/"license": "Apache-2.0"/g' "$file"
            ;;
        *.toml)
            # Update pyproject.toml
            ./cleanup_pyproject.py "$file"
            ;;
        *.py)
            # Remove setup.py, we only use pyproject.toml
            rm -f "$file"
            ;;
        *.cfg)
            # Remove setup.cfg, we only use pyproject.toml
            rm -f "$file"
            ;;
    esac
}

# clean up previous generated files
rm -rf python/avis-client/generated
rm -rf typescript/avis-client/generated
rm -rf javascript/avis-client/generated

# generate python client
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g python -o python/avis-client/generated --additional-properties=packageName=avis_client,packageVersion="$1"
# generate typescript client
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g typescript-axios -o typescript/avis-client/generated --additional-properties=withInterfaces=true,npmName=@viun/avis-client
# generate javascript client
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g javascript -o javascript/avis-client-js/generated --additional-properties=npmName=@viun/avis-client-js

# Clean up author and license fields
export -f update_files
find . -type d \( -name node_modules -o -name .venv \) -prune -o -type f \( -name "package.json" -o -name "setup.py" -o -name "setup.cfg" -o -name "pyproject.toml" \) -exec bash -c 'update_files "$0"' {} \;

# Add Apache-2.0 license to the generated files
cp ../LICENSE python/avis-client/generated/LICENSE
cp ../LICENSE typescript/avis-client/generated/LICENSE
cp ../LICENSE javascript/avis-client/generated/LICENSE

echo "Done."
