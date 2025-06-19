#include <drogon/drogon.h>

int main() {
    drogon::app()
        .loadConfigFile("config/drogon_config.json")
        .setLogLevel(trantor::Logger::kInfo)
        .run();
}
