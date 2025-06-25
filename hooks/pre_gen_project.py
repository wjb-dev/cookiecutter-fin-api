from cookiecutter.main import cookiecutter

LANG_MAP = {
    "Python - FastAPI":  ("python-fastapi", "py"),
    "Java - SpringBoot": ("java-springboot", "java"),
    "Go - gRPC - Protoc":("go-grpc-protoc", "go"),
    "csharp":            ("csharp", "cs"),
}

choice = "{{ cookiecutter.language }}"                     # <- ask() or argparse, etc.
slug, abbrev = LANG_MAP[choice]

cookiecutter(
    '{ cookiecutter.project_slug }}',
    no_input=True,
    extra_context={
        "variant":    slug,
        "language_abbrev":  abbrev,
    },
)
