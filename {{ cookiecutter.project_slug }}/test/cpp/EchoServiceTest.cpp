#include <catch2/catch_test_macros.hpp>
#include "echo.grpc.pb.h"
#include "server/EchoServiceImpl.cpp"

TEST_CASE("Echo::Ping returns pong") {
  demo::EchoServiceImpl svc;
  grpc::ServerContext   ctx;
  demo::PingRequest     req;
  demo::PingReply       rep;
  req.set_text("hello");

  grpc::Status s = svc.Ping(&ctx, &req, &rep);

  REQUIRE(s.ok());
  CHECK(rep.text() == "pong: hello");
}
