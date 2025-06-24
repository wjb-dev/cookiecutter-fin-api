# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

{% if cookiecutter.variant == "go-grpc-protoc" %}
## gRPC Server Validation Commands

Use `grpcurl` to validate the running gRPC server.

---

### 🔎 List Available Services

```bash
grpcurl -plaintext localhost:50051 list
```

---

### ❤️ Health Checks

#### Check All Services

```bash
grpcurl -plaintext -d '{}' \
localhost:50051 grpc.health.v1.Health/Check
```

#### Check EchoService Health

```bash
grpcurl -plaintext -d '{"service":"v1.EchoService"}' \
localhost:50051 grpc.health.v1.Health/Check
```

#### Check PingService Health

```bash
grpcurl -plaintext -d '{"service":"v1.PingService"}' \
localhost:50051 grpc.health.v1.Health/Check
```

---

### 📘 Describe Services

#### EchoService

```bash
grpcurl -plaintext localhost:50051 describe v1.EchoService
```

#### PingService

```bash
grpcurl -plaintext localhost:50051 describe v1.PingService
```

---

### 🧪 Test RPCs

#### Test EchoService

```bash
grpcurl -plaintext -d '{"message":"Hello Echo"}' \
localhost:50051 v1.EchoService/Echo
```

#### Test PingService

```bash
grpcurl -plaintext -d '{}' \
localhost:50051 v1.PingService/Ping
```
{% elif cookiecutter.variant == "python-fastapi" %}
## 🚀 FastAPI Quick-start

```bash
uvicorn {{ cookiecutter.project_slug }}.main:app --reload
```

Visit docs at: <http://127.0.0.1:8000/docs>

{% elif cookiecutter.variant == "java-springboot" %}
## ☕ Spring Boot Quick-start

```bash
./mvnw spring-boot:run
```

Visit actuator at: `http://localhost:8080/actuator/health`

{% elif cookiecutter.variant == "csharp" %}
## 🔧 .NET API Quick-start

```bash
dotnet run --project src/{{ cookiecutter.project_slug }}
```

Swagger UI: `http://localhost:5000/swagger`

{% endif %}
