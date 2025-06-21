package com.example.service;

import com.example.dto.HealthResponse;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(
        classes = HealthService.class,
        properties = {
                "spring.application.metadata.name=service-name",
                "spring.application.metadata.version=0.0.0"
        })

class HealthServiceTest {

    @Autowired
    private HealthService healthService;

    @Test
    void getHealthReturnsCorrectPayload() {
        HealthResponse resp = healthService.getHealth();

        assertThat(resp.service()).isEqualTo("service-name");
        assertThat(resp.status()).isEqualTo("ok");
        assertThat(resp.version()).isEqualTo("0.0.0");
    }
}
