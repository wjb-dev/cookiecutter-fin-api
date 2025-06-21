package com.example.dto;

import io.swagger.v3.oas.annotations.media.Schema;

@Schema(name = "HealthResponse", description = "Service liveness payload")
public record HealthResponse(
        @Schema(description="The name of the service", example="{{ cookiecutter.project_slug }}") String service,
        @Schema(description="Status",           example="ok")             String status,
        @Schema(description="Version",          example="0.1.0")          String version
) {}