## Quick start

```bash
cookiecutter gh:wjb-dev/cookiecutter-fin-api
# or
gh repo create --template wjb-dev/cookiecutter-fin-api my-new-api


# From a freshly generated project
kind create cluster --name dev    # or start Colima
skaffold dev -p dev               # should watch, build, and Helm-deploy
curl localhost:8000/healthz       # returns {"status":"ok"}
