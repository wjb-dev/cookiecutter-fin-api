#include "echo_server.h"

grpc::Status EchoServiceImpl::Echo(
    grpc::ServerContext*, const echo::v1::EchoRequest* req,
    echo::v1::EchoResponse* resp) {
  resp->set_message("Echo: " + req->message());
  return grpc::Status::OK;
}