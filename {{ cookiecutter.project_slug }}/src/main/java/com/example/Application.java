package com.example;

import java.net.InetAddress;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.ApplicationListener;
import lombok.extern.slf4j.Slf4j;

@SpringBootApplication
@Slf4j
public class Application implements ApplicationListener<ApplicationReadyEvent> {

    @Value("${server.port:8080}")
    private int port;

    @Value("${springdoc.swagger-ui.path:/swagger-ui/index.html}")
    private String swaggerPath;

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Override
    public void onApplicationEvent(ApplicationReadyEvent event) {
        try {
            String host = InetAddress.getLocalHost().getHostAddress();
            log.info("✅  Swagger UI available at: http://{}:{}{}", host, port, swaggerPath);
            log.info("✅  Swagger UI available at: http://localhost:{}{}", port, swaggerPath);
        } catch (Exception e) {
            log.warn("Could not determine host address for Swagger URL", e);
            log.info("✅  Swagger UI available at: http://localhost:{}{}", port, swaggerPath);
        }
    }
}
