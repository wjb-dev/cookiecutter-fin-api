package com.example.controller;

import com.example.dto.HealthResponse;
import com.example.service.HealthService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;


@WebMvcTest(HealthController.class)
class HealthControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private HealthService healthService;

    @Test
    void healthzReturns200AndCorrectBody() throws Exception {
        // Arrange
        var response = new HealthResponse(
                "Service Name",
                "ok",
                "0.0.0"
        );
        when(healthService.getHealth()).thenReturn(response);

        // Act & Assert
        mockMvc.perform(get("/healthz"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.service").value("Service Name"))
                .andExpect(jsonPath("$.status").value("ok"))
                .andExpect(jsonPath("$.version").value("0.0.0"));
    }
}
