from cookiecutter.config import get_user_config

LANG_MAP = {
    "Python - FastAPI":  ("python-fastapi", "py"),
    "Java - SpringBoot": ("java-springboot", "java"),
    "Go - gRPC - Protoc":("go-grpc-protoc", "go"),
    "csharp":            ("csharp", "cs"),
}

choice = "csharp"
print("HELLO THERE!!!!")
print(choice) # <- ask() or argparse, etc.
slug, abbrev = LANG_MAP[choice]

print(get_user_config().values())
# cookiecutter(
#     "gh:wjb-dev/cookiecutter-fin-api",
#     no_input=False,
#     extra_context={
#         "variant":    slug,
#         "language_abbrev":  abbrev,
#     },
# )
