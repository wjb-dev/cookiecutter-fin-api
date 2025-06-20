import os, shutil, textwrap
from pathlib import Path

project_dir = Path.cwd()
language = "{{ cookiecutter.language }}"

LANGUAGE_ASSETS = {
    "python": {"requirements.txt", "src/python", "test/python"},
    "java":   {"pom.xml", "src/main/resources", "src/main/java", "test/java"},
    "csharp":  {"src/main/csharp", "test/csharp"},
    "cpp": {"proto", "CMakeLists.txt", "src/main/cpp", "test/cpp"}
    # …
}

def rm(p: Path):
    if p.is_dir():
        shutil.rmtree(p, ignore_errors=True)
    else:
        p.unlink(missing_ok=True)

# ---------------------------------------------------------------------------
# helper: pretty-print a tree *relative to* project_dir
# ---------------------------------------------------------------------------
def snapshot(label: str):
    print(f"\n─── {label} ─────────────────────────────────────────────")
    for root, dirs, files in os.walk(project_dir):
        rel_root = Path(root).relative_to(project_dir)
        indent   = "│   " * len(rel_root.parts)
        head     = "└── " if indent else ""
        print(f"{indent}{head}{rel_root.name if rel_root.name else '.'}")
        for f in sorted(files):
            print(f"{indent}    {f}")
    print("──────────────────────────────────────────────────────────\n")

# ---------------------------------------------------------------------------
# 1️⃣ BEFORE
snapshot("tree BEFORE clean-up")

# 2️⃣ DELETE language assets that we do *not* want
for lang, assets in LANGUAGE_ASSETS.items():
    if lang == language:
        continue
    for rel in assets:
        path = project_dir / rel
        if path.exists():
            rm(path)
            print(f"🧹  removed {path.relative_to(project_dir)}")

# 3️⃣ AFTER
snapshot("tree AFTER clean-up")

print(f"Template clean-up complete — kept only “{language}” assets.")
