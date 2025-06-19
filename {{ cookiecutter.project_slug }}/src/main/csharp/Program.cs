// src/main/csharp/Program.cs
var builder  = WebApplication.CreateBuilder(args);
var app      = builder.Build();

// Inject the project slug so every stack returns the same payload shape
const string Service = "{{ cookiecutter.project_slug }}";

app.MapGet("/healthz", () => Results.Json(new { service = Service, status = "ok" }));

app.Run();
