{% if cookiecutter._variant == 'python-fastAPI' -%}
#########################################################
#                    Python FastAPI                     #
#########################################################

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src /app/src
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

{% elif cookiecutter._variant == 'java-springboot' -%}
#########################################################
#                    Java Springboot                    #
#########################################################

# ──────────────────── Stage 1: Builder ────────────────────────────────────────
FROM maven:3.9-eclipse-temurin-21 AS builder
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn -B package -DskipTests

# ──────────────────── Stage 2: Runtime ────────────────────────────────────────
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /build/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]

{% elif cookiecutter._variant == 'csharp' -%}
#########################################################
#                       C# .NET                         #
#########################################################
# ──────────────────── Stage 1: Builder ────────────────────────────────────────
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS builder
WORKDIR /build
COPY src/main/csharp ./src
RUN dotnet publish src/DemoApiCSharp.csproj -c Release -o out

# ──────────────────── Stage 2: Runtime ────────────────────────────────────────
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=builder /build/out .
ENV ASPNETCORE_URLS=http://0.0.0.0:8000
ENTRYPOINT ["dotnet", "DemoApiCSharp.dll"]

{% elif cookiecutter._variant == 'go-grpc-protc' -%}
#########################################################
#              GoLang gRPC-ProtoBuf Protoc              #
#########################################################

# ──────────────────── Stage 1: Builder ────────────────────────────────────────
FROM golang:1.24.4-alpine AS builder
RUN apk add --no-cache git protobuf protoc
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
ENV PATH="${PATH}:$(go env GOPATH)/bin"
WORKDIR /app
COPY . .
COPY go.mod go.sum ./
RUN go get gopkg.in/yaml.v3@v3.0.1
RUN go mod download
RUN protoc \
-I pkg/proto/v1 \
--go_out=paths=source_relative:pkg/proto/v1 \
--go-grpc_out=paths=source_relative:pkg/proto/v1 \
pkg/proto/v1/service.proto
RUN go mod tidy
RUN CGO_ENABLED=0 go build -o /app/{{ cookiecutter.project_slug }} cmd/{{ cookiecutter.project_slug }}/main.go

# ──────────────────── Stage 2: Runtime ────────────────────────────────────────
FROM alpine:latest
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY --from=builder /app/{{ cookiecutter.project_slug }} .
COPY --from=builder /app/configs /app/configs
EXPOSE 50051
ENTRYPOINT ["./{{ cookiecutter.project_slug }}"]


