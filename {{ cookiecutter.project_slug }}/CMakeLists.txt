cmake_minimum_required(VERSION 3.25)
project(demo_cpp_api LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(FetchContent)

# ---------- gRPC / protobuf ----------
# This grabs the *released* artefacts so we don’t build protoc twice.
FetchContent_Declare(
  grpc
  GIT_REPOSITORY https://github.com/grpc/grpc.git
  GIT_TAG        v1.60.0            # or whatever release you like
)
set(FETCHCONTENT_QUIET FALSE)
FetchContent_MakeAvailable(grpc)    # brings in protobuf too

# Generate C++ sources from .proto files
file(GLOB PROTOS proto/*.proto)
foreach(f ${PROTOS})
  get_filename_component(fname ${f} NAME_WE)
  protobuf_generate(
    LANGUAGE cpp
    OUT_VAR   pb_srcs
    PROTOS    ${f}
  )
  grpc_generate(
    LANGUAGE cpp
    OUT_VAR   grpc_srcs
    PROTOS    ${f}
  )
  list(APPEND GENERATED_SRC ${pb_srcs} ${grpc_srcs})
endforeach()

# ---------- service binary ----------
add_executable(demo-cpp-api
    src/main.cpp
    src/server/EchoServiceImpl.cpp
    ${GENERATED_SRC}
)
target_link_libraries(demo-cpp-api PRIVATE
    gRPC::grpc++       # runtime
    protobuf::libprotobuf
)

# ---------- unit tests ----------
enable_testing()
add_executable(unit-tests
    test/EchoServiceTest.cpp
    ${GENERATED_SRC}         # the same stubs so we can call service locally
)
target_link_libraries(unit-tests PRIVATE
    gRPC::grpc++
    protobuf::libprotobuf
    Catch2::Catch2WithMain           # or gtest if you prefer
)
include(Catch)                       # Catch2 helper
catch_discover_tests(unit-tests)
