#pragma once
#include "generated/echo.grpc.pb.h"

class EchoServiceImpl final : public echo::v1::EchoService::Service {
public:
  grpc::Status Echo(grpc::ServerContext* ctx,
                    const echo::v1::EchoRequest* req,
                    echo::v1::EchoResponse* resp) override;
};