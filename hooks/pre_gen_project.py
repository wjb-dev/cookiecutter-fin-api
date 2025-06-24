import re

from cookiecutter.main import cookiecutter


def normalize(text: str) -> str:
    """Return lower-case string with *all* whitespace removed."""
    return re.sub(r"\s+", "", text).lower()

# 2) Slug version (lowercase, no spaces)
slug = normalize(cookiecutter["language"])
cookiecutter["variant"] = slug

ABBREV_MAP = {
    "python-fastapi": "python",
    "java-springboot": "java",
    "csharp": "cs",
    "go-grpc-protoc": "go",
}

cookiecutter["language_abbrev"] = ABBREV_MAP.get(slug, slug[:2])

