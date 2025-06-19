{% if cookiecutter.language == 'python' -%}
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
{% elif cookiecutter.language == 'java' -%}
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY target/{{ cookiecutter.project_slug }}.jar app.jar
CMD ["java", "-jar", "app.jar"]
{% elif cookiecutter.language == 'csharp' -%}
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine
WORKDIR /app
COPY published/ .
CMD ["dotnet", "{{ cookiecutter.project_name }}.dll"]
{% elif cookiecutter.language == 'cpp' -%}
FROM debian:bookworm-slim
WORKDIR /app
COPY build/{{ cookiecutter.project_slug }} /usr/local/bin/service
CMD ["service"]
{% endif -%}


