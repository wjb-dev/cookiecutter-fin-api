import os
import shutil
from pathlib import Path

project_dir = Path.cwd()
language = "{{ cookiecutter.language }}"

def rm(path: Path):
    if path.is_dir():
        shutil.rmtree(path, ignore_errors=True)
    else:
        path.unlink(missing_ok=True)

# maps language ➜ list of (relative) paths to KEEP.
keep = {
    "python": {
        "requirements.txt", "src/python/__init__.py", "src/python/main.py", "test/python/test_main.py"
    },
    "java": {
        "pom.xml", "src/main", "test/java"
    },
    "csharp": {
        "Program.csproj", "src/main/csharp"
    },
    "cpp": {
        "CMakeLists.txt", "src/main/cpp"
    },
}

# remove every language-specific file not in keep[language]
all_specific = {
    "python": [ "requirements.txt", "src/python/__init__.py", "src/python/main.py", "test/python/test_main.py"],
    "java": ["pom.xml", "src/main", "test/java"],
    "csharp": ["Program.csproj", "src/main/csharp"],
    "cpp": ["CMakeLists.txt", "src/main/cpp"],
}

for lang, paths in all_specific.items():
    if lang == language:
        continue
    for rel in paths:
        rm(project_dir / rel)

print(f"Template clean-up complete → kept only {language} assets.")
