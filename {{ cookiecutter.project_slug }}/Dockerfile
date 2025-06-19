########################  Python Fast API  #######################
{% if cookiecutter.language == 'python' -%}
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/python ./python
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "python.main:app", "--host", "0.0.0.0", "--port", "8000"]

########################  Java Spring Boot  #######################
{% elif cookiecutter.language == 'java' -%}
# ---------- build stage ----------
FROM maven:3.9-eclipse-temurin-21 AS builder
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn -B package -DskipTests

# ---------- runtime stage ----------
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /build/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]

########################  C# .NET #######################
{% elif cookiecutter.language == 'csharp' -%}
# ---------- build stage ----------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS builder
WORKDIR /build
COPY src/main/csharp ./src
RUN dotnet publish src/DemoApiCSharp.csproj -c Release -o out

# ---------- runtime stage ----------
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=builder /build/out .
ENV ASPNETCORE_URLS=http://0.0.0.0:8000
ENTRYPOINT ["dotnet", "DemoApiCSharp.dll"]

########################  C++ GRPC  #######################
{% elif cookiecutter.language == 'cpp' -%}
# ---------- build stage ----------
FROM debian:bookworm-slim AS build
WORKDIR /src
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential cmake git ca-certificates \
        libssl-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . .
RUN cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build --target demo-cpp-api -j1   # safer for cross-arch

# ---------- runtime stage ----------
FROM debian:bookworm-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends libssl3 zlib1g && \
    rm -rf /var/lib/apt/lists/*
COPY --from=build /src/build/demo-cpp-api /usr/local/bin/service
EXPOSE 8000
CMD ["service"]
{% endif -%}


