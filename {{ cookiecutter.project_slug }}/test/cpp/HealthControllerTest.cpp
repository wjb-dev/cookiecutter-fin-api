#include <drogon/drogon_test.h>

DROGON_TEST(Healthz) {
    auto cli = HttpClient::newHttpClient("http://127.0.0.1:{{ cookiecutter.port | default(8000) }}");
    auto req = HttpRequest::newHttpRequest();
    req->setPath("/healthz");

    co_await cli->sendRequest(req) >> [C](ReqResult r, const HttpResponsePtr& resp) {
        REQUIRE(r == ReqResult::Ok);
        Json::Value j; Json::Reader().parse(resp->body(), j);
        CHECK(j["status"].asString() == "ok");
        CHECK(j["service"].asString() == "{{ cookiecutter.project_slug }}");
    };
}
