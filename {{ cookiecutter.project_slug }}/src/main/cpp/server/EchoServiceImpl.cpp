#include "echo.grpc.pb.h"

using grpc::ServerContext;
using grpc::Status;

namespace demo {

class EchoServiceImpl final : public Echo::Service {
  Status Ping(ServerContext*,
              const PingRequest* req,
              PingReply* reply) override {
    reply->set_text("pong: " + req->text());
    return Status::OK;
  }
};

} // namespace demo
