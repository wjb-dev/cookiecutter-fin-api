cmake_minimum_required(VERSION 3.25)
project(demo_cpp_api LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(FetchContent)

# ───────────── gRPC / protobuf deps ─────────────
FetchContent_Declare(
    grpc
    GIT_REPOSITORY https://github.com/grpc/grpc.git
    GIT_TAG        v1.60.0            # pin → reproducible
)
FetchContent_MakeAvailable(grpc)       # also pulls protobuf

# ───────────── code-gen from proto ─────────────
file(GLOB PROTO_FILES "${CMAKE_SOURCE_DIR}/proto/*.proto")

protobuf_generate(
    LANGUAGE cpp
    OUT_VAR  PB_SRCS
    PROTOS   ${PROTO_FILES}
)

grpc_generate(
    LANGUAGE cpp
    OUT_VAR  GRPC_SRCS
    PROTOS   ${PROTO_FILES}
)

set(GENERATED ${PB_SRCS} ${GRPC_SRCS})

# ───────────── service binary ─────────────
add_executable(demo-cpp-api
    src/main/cpp/main.cpp
    src/main/cpp/server/EchoServiceImpl.cpp
    ${GENERATED}
)
target_include_directories(demo-cpp-api PRIVATE
    ${CMAKE_CURRENT_BINARY_DIR}        # generated *.pb.h
)
target_link_libraries(demo-cpp-api PRIVATE
    gRPC::grpc++ protobuf::libprotobuf
)

# ───────────── unit tests ─────────────
enable_testing()
FetchContent_Declare(
    catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.6.0
)
FetchContent_MakeAvailable(catch2)

add_executable(unit-tests
    test/cpp/EchoServiceTest.cpp
    src/main/cpp/server/EchoServiceImpl.cpp
    ${GENERATED}
)
target_include_directories(unit-tests PRIVATE
    ${CMAKE_CURRENT_BINARY_DIR}
)
target_link_libraries(unit-tests PRIVATE
    gRPC::grpc++ protobuf::libprotobuf Catch2::Catch2WithMain
)
include(Catch)
catch_discover_tests(unit-tests)
