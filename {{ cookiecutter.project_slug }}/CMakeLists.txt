cmake_minimum_required(VERSION 3.25)
project(echo_service LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ── Dependencies ────────────────────────────────────────────────────────────
find_package(Protobuf    REQUIRED)
find_package(gRPC         CONFIG REQUIRED)
find_package(Threads     REQUIRED)

# ── Proto generation ────────────────────────────────────────────────────────
set(PROTO_DIR ${CMAKE_SOURCE_DIR}/proto)
set(GEN_DIR   ${CMAKE_BINARY_DIR}/generated)
file(MAKE_DIRECTORY ${GEN_DIR})

find_program(PROTOC_EXECUTABLE protoc     REQUIRED)
find_program(GRPC_CPP_PLUGIN    grpc_cpp_plugin REQUIRED)

file(GLOB PROTO_FILES "${PROTO_DIR}/v1/*.proto")
foreach(P ${PROTO_FILES})
  get_filename_component(NAME_WE ${P} NAME_WE)

  set(pb_cc  ${GEN_DIR}/${NAME_WE}.pb.cc)
  set(pb_h   ${GEN_DIR}/${NAME_WE}.pb.h)
  set(grcc   ${GEN_DIR}/${NAME_WE}.grpc.pb.cc)
  set(grch   ${GEN_DIR}/${NAME_WE}.grpc.pb.h)

  add_custom_command(
    OUTPUT ${pb_cc} ${pb_h} ${grcc} ${grch}
    COMMAND ${PROTOC_EXECUTABLE}
            --cpp_out=${GEN_DIR}
            --grpc_out=${GEN_DIR}
            -I ${PROTO_DIR}
            --plugin=protoc-gen-grpc=${GRPC_CPP_PLUGIN}
            ${P}
    DEPENDS ${P}
  )
  list(APPEND PROTO_SRCS ${pb_cc} ${grcc})
  list(APPEND PROTO_HDRS ${pb_h}  ${grch})
endforeach()

# ── Server executable ───────────────────────────────────────────────────────
file(GLOB_RECURSE SRC_SRCS src/main/cpp/*.cpp)
add_executable(echo-server ${SRC_SRCS} ${PROTO_SRCS} ${PROTO_HDRS})
target_include_directories(echo-server PRIVATE ${GEN_DIR} ${PROTO_DIR}/v1)
target_link_libraries(echo-server
  PRIVATE gRPC::grpc++ protobuf::libprotobuf Threads::Threads
)

# ── Tests ───────────────────────────────────────────────────────────────────
option(BUILD_TESTS "Enable unit/integration tests" ON)
if(BUILD_TESTS)
  enable_testing()
  find_package(GTest CONFIG REQUIRED)

  # Unit tests (mock the service implementation)
  add_executable(echo-unit-tests
    test/unit/echo_server_test.cpp
    ${PROTO_SRCS} ${PROTO_HDRS}
  )
  target_include_directories(echo-unit-tests PRIVATE ${GEN_DIR})
  target_link_libraries(echo-unit-tests
    PRIVATE GTest::gtest_main gRPC::grpc++ protobuf::libprotobuf Threads::Threads
  )
  gtest_discover_tests(echo-unit-tests)

  # (Optional) integration tests
  add_executable(echo-int-tests
    test/integration/echo_integration_test.cpp
    ${PROTO_SRCS} ${PROTO_HDRS}
  )
  target_include_directories(echo-int-tests PRIVATE ${GEN_DIR})
  target_link_libraries(echo-int-tests
    PRIVATE GTest::gtest_main gRPC::grpc++ protobuf::libprotobuf Threads::Threads
  )
  gtest_discover_tests(echo-int-tests)
endif()
