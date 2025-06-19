#include <drogon/HttpController.h>
#include <drogon/HttpResponse.h>

using namespace drogon;

class HealthController : public HttpController<HealthController> {
public:
    METHOD_LIST_BEGIN
        ADD_METHOD_TO(HealthController::healthz, "/healthz", Get);
    METHOD_LIST_END

    void healthz(const HttpRequestPtr&, Callback &&cb) {
        Json::Value body;
        body["service"] = app().getCustomConfig()["service_name"].asString();
        body["status"]  = "ok";
        cb(HttpResponse::newHttpJsonResponse(body));
    }
};
