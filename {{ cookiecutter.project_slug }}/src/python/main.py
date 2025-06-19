from fastapi import FastAPI
app = FastAPI(title="{{ cookiecutter.project_name }}")

@app.get("/healthz")
def health():
    return {
        "service": "{{ cookiecutter.project_slug }}",   # ← rendered at bake-time
        "status":  "ok"
    }
