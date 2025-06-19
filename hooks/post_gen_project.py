# #!/usr/bin/env python3
# """
# Cookiecutter post-generation hook

# Remove source-tree pieces that belong to *other* languages so the rendered
# project is lean.  Currently supports only Python and Java.
# """
# import shutil
# from pathlib import Path

# # root of the newly generated project
# project_dir = Path(__file__).resolve().parent.parent

# # the choice the user made during cookiecutter prompts
# language = "{{ cookiecutter.language }}".lower()

# LANGUAGE_ASSETS = {
#     "python": {
#         Path("requirements.txt"),
#         Path("src/python"),
#         Path("tests/python"),          # rename “test”→“tests” if you like
#     },
#     "java": {
#         Path("pom.xml"),
#         Path("src/main"),
#         Path("test/java"),
#     },
# }

# def rm(path: Path) -> None:
#     """Delete file or directory; ignore if it doesn’t exist."""
#     try:
#         if path.is_dir():
#             shutil.rmtree(path, ignore_errors=True)
#         else:
#             path.unlink(missing_ok=True)  # Py ≥ 3.8
#     except PermissionError:
#         # best-effort – don’t fail the whole generation
#         print(f"⚠️  Could not remove {path}")

# # sanity-check in case someone typed a new language in prompts
# if language not in LANGUAGE_ASSETS:
#     raise SystemExit(
#         f"Unknown language '{language}'. "
#         f"Supported: {', '.join(LANGUAGE_ASSETS)}"
#     )

# # remove assets that belong to *other* languages
# for lang, assets in LANGUAGE_ASSETS.items():
#     if lang == language:
#         continue
#     for rel in assets:
#         path = project_dir / rel 
#         rm(path)
#         print(f"🧹  Removed file — {path}")


# print(f"🧹  Template clean-up complete — kept only {language!r} assets.")


# post_gen_project.py  –  Cookiecutter post-generate hook
import os, shutil, textwrap
from pathlib import Path

project_dir = Path.cwd()
language = "{{ cookiecutter.language }}"

LANGUAGE_ASSETS = {
    "python": {"requirements.txt", "src/python", "tests/python"},
    "java":   {"pom.xml", "src/main", "test/java"},
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
