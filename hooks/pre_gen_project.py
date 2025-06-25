# hooks/pre_gen_project.py
import re
import sys

# ── Jinja block executes before Python runs ────────────────────
{% set slug = cookiecutter.language|lower|replace(' ', '') %}
{% set abbrev_map = {
        'python-fastapi': 'python',
        'java-springboot': 'java',
        'go-grpc-protoc':  'go',
        'csharp':          'cs'
} %}
{% set _ = cookiecutter.update({
        'language_slug': slug,
        'language_abbrev': abbrev_map.get(slug, slug[:2])
}) %}
# ── end Jinja block ─────────────────────────────────────────────

# The rest is ordinary Python; you can still validate or abort
LANG_RE = r'^[a-z\-]+$'
if not re.match(LANG_RE, '{{ cookiecutter.language_slug }}'):
    print("ERROR: invalid language slug")
    sys.exit(1)
