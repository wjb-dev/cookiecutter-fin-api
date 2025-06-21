package com.example.controller;

import com.example.dto.HealthResponse;
import com.example.service.HealthService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Tag(name = "Ping", description = "Lightweight endpoint consumed by orchestrators (K8s, Nomad, …) to check container liveness/readiness.")
public class HealthController {

    private final HealthService healthService;

    public HealthController(HealthService healthService) {
        this.healthService = healthService;
    }

    @GetMapping("/healthz")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary="Liveness probe",
            description=" Endpoint consumed by orchestrators (K8s, Nomad, …) to verify that the container is **alive and ready**.")
    public HealthResponse health() {
        return healthService.getHealth();
    }
}