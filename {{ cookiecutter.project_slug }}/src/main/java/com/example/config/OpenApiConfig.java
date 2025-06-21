package com.example.config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.info.License;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(
        info = @Info(
                title       = "${spring.application.metadata.name}",
                version     = "${spring.application.metadata.version}",
                description = "${spring.application.metadata.description}",
                contact     = @Contact(name="Your Team", email="support@example.com", url="https://github.com/yourorg"),
                license     = @License(name="MIT", url="https://opensource.org/licenses/MIT")
        )
)
public class OpenApiConfig { }