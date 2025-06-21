#include <grpcpp/grpcpp.h>
#include "echo_server.h"

int main(int argc, char** argv) {
  std::string server_addr("0.0.0.0:50051");
  EchoServiceImpl service;

  grpc::ServerBuilder builder;
  builder.AddListeningPort(server_addr, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);

  auto server = builder.BuildAndStart();
  std::cout << "🚀 gRPC server listening on " << server_addr << std::endl;
  server->Wait();
  return 0;
}
