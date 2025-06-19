PROJECT   := {{ cookiecutter.project_slug }}
IMG       := $(PROJECT):local
PORT      := 8000
KIND_NAME ?= dev
DOCKER_BUILDKIT ?= 1        # leverage BuildKit when available

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ---------- Build & Run ------------------------------------------------------

build: ## Build Docker image
	DOCKER_BUILDKIT=$(DOCKER_BUILDKIT) docker build -t $(IMG) .

run: build ## Build & run container locally
	docker run --rm -p $(PORT):$(PORT) $(IMG)

kind-load: build ## Load image into kind (no registry push)
	kind load docker-image $(IMG) --name $(KIND_NAME)

skaffold: ## Live-reload dev loop (kind/Colima)
	skaffold dev -p dev

clean: ## Remove local image
	-docker rmi $(IMG)

# ---------- Quality ----------------------------------------------------------

lint: ## Ruff + Black formatting checks
	pip install -q ruff black
	ruff src tests
	black --check src tests

test: ## Run PyTest suite
	pip install -q pytest
	pytest -q

ci: lint test build ## Lint, test, then build (for CI pipeline)

.PHONY: help build run kind-load skaffold clean lint test ci
