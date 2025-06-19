package com.example;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.beans.factory.annotation.Autowired;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
class HealthControllerTest {

    @Autowired
    private MockMvc mvc;

    @Test
    void healthzShouldReturnOk() throws Exception {
        mvc.perform(get("/healthz"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.service").value("{{ cookiecutter.project_slug }}"))  // injected slug
            .andExpect(jsonPath("$.status").value("ok"));
    }
}
