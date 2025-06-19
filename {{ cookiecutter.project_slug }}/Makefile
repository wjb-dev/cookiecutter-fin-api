# -------- Generic Makefile (Cookiecutter) --------
PROJECT   := {{ cookiecutter.project_slug }}
IMG       := $(PROJECT):local
PORT      := 8000
KIND_NAME ?= dev
DOCKER_BUILDKIT ?= 1

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

build: ## Build Docker image
	DOCKER_BUILDKIT=$(DOCKER_BUILDKIT) docker build -t $(IMG) .

run: build ## Run container locally
	docker run --rm -p $(PORT):$(PORT) $(IMG)

{% if cookiecutter.language == "python" -%}
lint: ## Python linters
	pip install -q ruff black
	ruff src tests
	black --check src tests

test: ## PyTest
	pip install -q pytest
	pytest -q
{% elif cookiecutter.language == "java" -%}
lint:
	@echo "No lint configured for Java template yet."
test:
	./mvnw test
{% elif cookiecutter.language == "csharp" -%}
lint:
	@echo "No lint configured for C# template yet."
test:
	dotnet test
{% elif cookiecutter.language == "cpp" -%}
lint:
	@echo "No lint configured for C++ template yet."
test:
	ctest --output-on-failure
{% endif %}

kind-load: build ## Load image into kind
	kind load docker-image $(IMG) --name $(KIND_NAME)

skaffold:  ## Live-reload dev loop
	skaffold dev -p dev

clean:     ## Delete local image
	-docker rmi $(IMG)

ci: lint test build

.PHONY: help lint test build run kind-load skaffold clean ci
