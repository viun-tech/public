# VUE's public documentation

## Install

```bash
poetry install
```

All commands below assume you have activated the virtual environment with

```bash
poetry shell
```


## Serve locally

```bash
mkdocs serve
```

This will serve the documentation at http://localhost:8888

## Build

```bash
mkdocs build
```

## Deploy

### Automatic (CICD)

Please refer to the GitHub Action workflow in `.github/workflows/documentation.yml` for the latest deployment configuration.

### Manual

```bash
mkdocs gh-deploy --force
```

This will build and deploy the documentation to the `gh-pages` branch of the repository. The documentation will be available at https://vuengineering.github.io/vue-monorepo and
https://docs.vu.engineering.
