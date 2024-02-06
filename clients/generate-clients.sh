#!/bin/bash

# fail on error
set -e

new_author="VUEngineering"
new_license="Apache 2.0"
new_author_email="tech@vu.engineering"

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
            sed -i 's/"author": "[^"]*"/"author": "'"$new_author"'"/g' "$file"
            sed -i 's/"license": "[^"]*"/"license": "'"$new_license"'"/g' "$file"
            ;;
        *.py)
            # Update setup.py
            sed -i 's/author="[^"]*"/author="'"$new_author"'"/g' "$file"
            sed -i 's/license="[^"]*"/license="'"$new_license"'"/g' "$file"
            sed -i 's/author_email="[^"]*"/author_email="'"$new_author_email"'"/g' "$file"
            ;;
        *.toml)
            # Update pyproject.toml
            sed -i 's/authors = \["[^"]*"\]/authors = ["'"$new_author_email"'"]/g' "$file"
            sed -i 's/license = "[^"]*"/license = "'"$new_license"'"/g' "$file"
            ;;
    esac
}

# generate python client
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g python -o python/avis-client/generated --additional-properties=packageName=avis_client,packageVersion="$1"
# generate typescript client
openapi-generator-cli generate --git-repo-id public --git-user-id vuengineering -i ../api-schema.yml -g typescript-axios -o typescript/avis-client/generated --additional-properties=withInterfaces=true,npmName=@vision-unified-tech/avis-client

# Clean up author and license fields
export -f update_files
export new_author
export new_license
export new_author_email
find . -type f \( -name "package.json" -o -name "setup.py" -o -name "pyproject.toml" \) -exec bash -c 'update_files "$0"' {} \;

echo "Done."
