{% if cookiecutter.language == 'python' -%}
########################  Python Fast API  #######################
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src /app/src
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

{% elif cookiecutter.language == 'java' -%}
########################  Java Spring Boot  #######################
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

{% elif cookiecutter.language == 'csharp' -%}
########################  C# .NET #######################
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

{% elif cookiecutter.language == 'cpp' -%}
########################  C++ GRPC  #######################
# ---------- build stage ----------
FROM debian:bookworm-slim AS build
WORKDIR /src
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential cmake git pkg-config            \
      libssl-dev libprotobuf-dev protobuf-compiler     \
      libgrpc++-dev libgrpc-dev &&                    \
    rm -rf /var/lib/apt/lists/*
COPY . .
RUN cmake -S . -B build -DBUILD_TESTS=OFF && \
    cmake --build build --config Release -j$(nproc)

# ---------- runtime stage ----------
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libssl3 libprotobuf23 libgrpc++1 &&         \
    rm -rf /var/lib/apt/lists/*

COPY --from=build /src/build/echo-server /usr/local/bin/echo-server
EXPOSE 50051

ENTRYPOINT ["/usr/local/bin/echo-server"]
{% endif -%}


