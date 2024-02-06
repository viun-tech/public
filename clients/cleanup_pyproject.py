#!/usr/bin/env python3

import toml
import sys

if not sys.argv[1]:
    print("No argument provided")
    sys.exit(1)

pyproject = toml.load(sys.argv[1])
pyproject["tool"]["poetry"]["authors"] = ["VUEngineering <tech@vu.engineering>"]
pyproject["tool"]["poetry"]["license"] = "Apache License 2.0"
pyproject["tool"]["poetry"][
    "homepage"
] = "https://docs.vu.engineering/api/clients/python/avis_client/"
pyproject["tool"]["poetry"]["repository"] = "https://github.com/vuengineering/public/"
pyproject["tool"]["poetry"]["maintainers"] = [
    "Adriano Pagano <adriano.pagano@vu.engineering>",
    "Lucas Vandroux <lucas.vandroux@vu.engineering>",
]
pyproject["tool"]["poetry"]["keywords"] = ["OpenAPI", "avis", "api client"]
pyproject["tool"]["poetry"]["description"] = "AVIS Python client"
pyproject["tool"]["poetry"]["readme"] = "README.md"

with open(sys.argv[1], "w") as f:
    toml.dump(pyproject, f)
