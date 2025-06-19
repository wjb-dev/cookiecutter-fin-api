using System.Net;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;

public class HealthEndpointTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    public HealthEndpointTests(WebApplicationFactory<Program> factory) =>
        _client = factory.CreateClient();

    [Fact]
    public async Task Healthz_ReturnsOkWithCorrectBody()
    {
        var resp = await _client.GetAsync("/healthz");
        Assert.Equal(HttpStatusCode.OK, resp.StatusCode);

        var json = await resp.Content.ReadFromJsonAsync<Dictionary<string,string>>();
        Assert.Equal("ok", json!["status"]);
        Assert.Equal("{{ cookiecutter.project_slug }}", json["service"]);
    }
}
