#include "server/EchoServiceImpl.cpp"   // <- tiny demo; split headers if you like
#include <grpcpp/server.h>
#include <grpcpp/server_builder.h>

int main() {
  demo::EchoServiceImpl service;
  grpc::ServerBuilder    builder;
  builder.AddListeningPort("0.0.0.0:8000",
                           grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
  std::cout << "gRPC server on :8000\n";
  server->Wait();
}
