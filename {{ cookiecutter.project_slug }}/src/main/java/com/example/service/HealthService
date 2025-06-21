package com.example.service;

import com.example.dto.HealthResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class HealthService {
    @Value("${spring.application.metadata.name}")
    private String appName;
    @Value("${spring.application.metadata.version}")
    private String appVersion;

    public HealthResponse getHealth() {
        return new HealthResponse(appName, "ok", appVersion);
    }
}
