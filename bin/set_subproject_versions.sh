#!/usr/bin/env bash

# --------------------------------------------------------------------------------------------------
# Script: set_subproject_versions.sh
#
# Description:
# Set the version of all subprojects to the same version as a parent project.
# This script gets passed the path to the VERSION file of the parent project. It will then resolve
# any nested python or javascript subprojects managed by poetry or yarn respectively and set their
# versions to the same version as the parent project.
#
# Usage:
# ./set_subproject_versions.sh [VERSION_FILE]
# VERSION_FILE: The file containing the version number of the parent project. The subproject resolution will be done
#               relative to this file. Defaults to VERSION.
#
# --------------------------------------------------------------------------------------------------

# Fail on any error and undefined variable (also in pipes)
set -euo pipefail

version_file=${1:-VERSION}

# Check if the VERSION file exists
if [ ! -f "$version_file" ]; then
  echo "VERSION file $version_file does not exist" >&2
  exit 1
fi

# Working directory is the one containing the version file
working_directory="$(dirname "$version_file")"

# Get the existing version string from the file
existing_version=$(cat "$version_file")

printf "Setting all subprojects version from parent '%s'\n" "$working_directory"

# Function to update version for poetry projects
update_poetry_version() {
    local pyproject_file=$1
    local project_dir
    project_dir=$(dirname "$pyproject_file")

    # Navigate to the directory containing the pyproject.toml
    cd "$project_dir" || return

    printf "[POETRY]: Bumping %s to %s\n" "$project_dir" "$existing_version"

    if ! poetry version "$existing_version" &> /dev/null; then
        printf "[POETRY]: Poetry version failed for project in directory: %s\n" "$project_dir"
        return 1
    fi
}

# Function to update version for yarn projects
update_yarn_version(){
    local package_json=$1
    local project_dir
    project_dir=$(dirname "$package_json")

    # Navigate to the directory containing the package.json
    cd "$project_dir" || return

    printf "[YARN]: Bumping %s to %s\n" "$project_dir" "$existing_version"

    if ! YARN_VERSION_GIT_TAG='' yarn version --no-git-tag-version --new-version "$existing_version" &> /dev/null; then
        printf "[YARN]: Yarn version failed for project in directory: %s\n" "$project_dir"
        return 1
    fi
}

# Exporting variables so subprocesses can access them
export working_directory
export existing_version
export -f update_poetry_version
export -f update_yarn_version

# Fix to make this work on both Linux and macOS: https://github.com/memkind/memkind/issues/33#issuecomment-1800080708
git ls-files --exclude-standard "$working_directory" | { grep 'pyproject.toml$' || test $? = 1; } | xargs -I {} -P "$(nproc 2>/dev/null || sysctl -n hw.logicalcpu)" bash -c 'update_poetry_version "$@"' _ {}
git ls-files --exclude-standard "$working_directory" | { grep 'package.json$' || test $? = 1; } | xargs -I {} -P "$(nproc 2>/dev/null || sysctl -n hw.logicalcpu)" bash -c 'update_yarn_version "$@"' _ {}
