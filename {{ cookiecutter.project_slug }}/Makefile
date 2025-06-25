# ---------------------------------------------------------------------------
# Universal Makefile — rendered by Cookiecutter
# Supports: python · java · csharp · cpp
# ---------------------------------------------------------------------------
PROJECT         := {{ cookiecutter.project_slug }}
IMG             := $(PROJECT):local
PORT            := 8000
KIND_NAME       ?= dev
BUILD_DIR       := build
BIN_DIR         := bin
PROTO_DIR       := pkg/proto/v1
PLATFORM        := $(shell uname -m)
PROTO_FILES     := $(wildcard $(PROTO_DIR)/*.proto)
CMAKE_FLAGS     := -DCMAKE_BUILD_TYPE=Release
LANG            := {{ cookiecutter.['__variant'] }}

# ---------- Language-specific commands --------------------------------------

ifeq ($(LANG),python-fastapi)
PRE_BUILD :=
LINT_CMD  := pip install -q ruff black && ruff src tests && black --check src tests
TEST_CMD  := pip install -q pytest && pytest -q
endif

ifeq ($(LANG),java-springboot)
PRE_BUILD := mvn -B package -DskipTests         # requires mvn OR use multi-stage Dockerfile
LINT_CMD  := echo "No Java lint configured"
TEST_CMD  := mvn -q test
endif

ifeq ($(LANG),csharp)
PRE_BUILD := dotnet publish src/main/csharp/DemoApiCSharp.csproj -c Release -o published
LINT_CMD  := echo "No C# lint configured"
TEST_CMD  := dotnet test --nologo
endif

ifneq ($(filter $(LANG),java-springboot python-fastapi csharp),)

.PHONY: help build run kind-load skaffold clean lint test ci


# ---------- Helper ----------------------------------------------------------

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ---------- Build & Run ------------------------------------------------------

build: ## Build Docker image
	$(PRE_BUILD)
	DOCKER_BUILDKIT=1 docker build -t $(IMG) .

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

endif

ifeq ($(LANG),go)

GO_TESTDIR := test

.PHONY: install build test docker-build docker-run clean generate clean-proto clean clean-generate

install:
	@echo "🛠️  Installing Go dependencies…"

ifeq ($(PLATFORM),arm64)
	@if ! command -v go >/dev/null 2>&1; then \
		echo "🍎 Apple Silicon detected, installing Go via Homebrew..."; \
		brew install go; \
	else \
		echo "✅ Go is already installed."; \
	fi
endif

	@for pkg in \
		google.golang.org/protobuf/cmd/protoc-gen-go@latest \
		google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest; do \
		binary=$$(basename $$pkg | cut -d'@' -f1); \
		if ! command -v $$binary >/dev/null 2>&1; then \
			echo "⬇️  Installing $$binary..."; \
			go install $$pkg; \
		else \
			echo "✅ $$binary already installed."; \
		fi; \
	done

generate: install
	@echo "⚙️  Generating Go code from .proto…"
	PATH="$(shell go env GOPATH)/bin:$(PATH)" protoc \
		-I $(PROTO_DIR) \
		--go_out=paths=source_relative:$(PROTO_DIR) \
		--go-grpc_out=paths=source_relative:$(PROTO_DIR) \
		$(PROTO_FILES)
		# 🧹 Ensure go.mod/go.sum reflect any new or removed imports introduced by the generated code
		go mod tidy

test: generate
	@echo "✅ Running Go tests…"
	cd $(GO_TESTDIR) && go test ./...

build:
	@echo "🔨 Building Go Docker image…"
	docker build -f Dockerfile -t $(PROJECT)-go:local .

run: build
	@echo "🚀 Running Go Docker container…"
	docker run --rm -p 50051:50051 $(PROJECT)-go:local

clean-generate:
	@echo "🧹 Cleaning build artifacts…"
	rm -rf $(BIN_DIR)

clean-proto:
	@echo "🧹 Cleaning generated proto files…"
	rm -rf $(PROTO_DIR)/*.pb.go

clean: clean-generate clean-proto

skaffold:
	@echo "🚀 Starting Skaffold in development mode with Go services..."
	skaffold dev -p dev

endif

