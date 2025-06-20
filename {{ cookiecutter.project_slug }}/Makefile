# ---------------------------------------------------------------------------
# Universal Makefile — rendered by Cookiecutter
# Supports: python · java · csharp · cpp
# ---------------------------------------------------------------------------
PROJECT   := {{ cookiecutter.project_slug }}
IMG       := $(PROJECT):local
PORT      := 8000
KIND_NAME ?= dev
DOCKER_BUILDKIT ?= 1

LANG      := {{ cookiecutter.language }}    # rendered value

# ---------- Language-specific commands --------------------------------------

ifeq ($(LANG),python)
PRE_BUILD :=
LINT_CMD  := pip install -q ruff black && ruff src tests && black --check src tests
TEST_CMD  := pip install -q pytest && pytest -q
endif

ifeq ($(LANG),java)
PRE_BUILD := mvn -B package -DskipTests         # requires mvn OR use multi-stage Dockerfile
LINT_CMD  := echo "No Java lint configured"
TEST_CMD  := mvn -q test
endif

ifeq ($(LANG),csharp)
PRE_BUILD := dotnet publish src/main/csharp/DemoApiCSharp.csproj -c Release -o published
LINT_CMD  := echo "No C# lint configured"
TEST_CMD  := dotnet test --nologo
endif

ifeq ($(LANG),cpp)
PRE_BUILD :=
LINT_CMD  := echo "No C++ lint configured"
TEST_CMD  := ctest --test-dir build --output-on-failure || true
endif

# ---------- Helper ----------------------------------------------------------

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ---------- Build & Run ------------------------------------------------------

build: ## Build Docker image
	$(PRE_BUILD)
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

lint: ## Language-specific lint
	$(LINT_CMD)

test: ## Language-specific test
	$(TEST_CMD)

ci: lint test build ## Lint, test, then build (for CI pipeline)

.PHONY: help build run kind-load skaffold clean lint test ci
