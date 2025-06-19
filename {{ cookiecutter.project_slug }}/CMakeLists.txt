cmake_minimum_required(VERSION 3.27)
project({{ cookiecutter.project_slug }} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Drogon CONFIG REQUIRED)

add_executable(${PROJECT_NAME}
    src/main.cpp
    src/controllers/HealthController.cc
)

target_link_libraries(${PROJECT_NAME} PRIVATE Drogon::Drogon)

# ─── tests ───────────────────────────────────────────────────────────────
enable_testing()
find_package(Catch2 CONFIG REQUIRED)
add_executable(tests test/HealthControllerTest.cpp)
target_link_libraries(tests PRIVATE Drogon::Drogon Catch2::Catch2WithMain)
add_test(NAME healthz COMMAND tests)
