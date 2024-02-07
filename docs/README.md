# VUE's public documentation

## Pre-requisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Install

```bash
poetry install
```

All commands below assume you have activated the virtual environment with

```bash
poetry shell
```

## Serve locally

To serve the documentation locally (with live reload) run:

```bash
mkdocs serve
```

This will serve the documentation at http://localhost:8888.

Alternatively, you can use `mike` to see the final output of the documentation build with the different versions of the
documentation:

```bash
mike serve -a localhost:8888
```

Please note that you will not benefit from live reload when using `mike serve`. So when working on the documentation, it
is recommended to use `mkdocs serve`.

## Deploy

### Automatic (CICD)

Please refer to the GitHub Action workflow in `.github/workflows/documentation.yml` for the latest deployment
configuration.

### Manual

```bash
mike deploy --push --update-aliases <version> latest
```

where `<version>` is the version of the doc you want to deploy.

This will build and deploy the documentation to the `gh-pages` branch of the repository. The documentation will be
available at https://vuengineering.github.io/vue-monorepo and
https://docs.vu.engineering.
