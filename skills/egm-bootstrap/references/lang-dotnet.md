<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# .NET Language Pack (C#, F#, Visual Basic)

## Detection

- `*.sln`, `*.slnx`, `*.csproj`, `*.fsproj`, `*.vbproj`,
  `Directory.Build.props`, `Directory.Packages.props`, `global.json`.

## Source Extensions

- `.cs`, `.csx`, `.fs`, `.fsi`, `.vb`, `.razor`, `.cshtml`.
- Markup read as templates (up to 200 lines): `.xaml`, `.axaml`.
- Generated, never source: `*.g.cs`, `*.g.i.cs`, `*.Designer.cs`,
  `*.AssemblyInfo.cs`, `*.AssemblyAttributes.cs`, `.resx`, and
  `Reference.cs` under `Connected Services/` or `Service References/`.

## Ignored Paths

- `bin/`, `obj/`, `.vs/`, `TestResults/`, `artifacts/`, and `packages/`
  next to a `packages.config` or `*.sln`.

## Test Conventions

- Projects whose name ends in `.Tests`, `.UnitTests`, `.IntegrationTests`,
  `.FunctionalTests`, or `.Specs`.
- Projects that use the `MSTest.Sdk` project SDK, set
  `<IsTestProject>true</IsTestProject>`, or reference
  `Microsoft.NET.Test.Sdk`, `xunit`, `xunit.v3`, `NUnit`, `MSTest`,
  `MSTest.TestFramework`, or `TUnit`. The whole project directory is
  test-only.
- Files named `*Tests.cs`, `*Test.cs`, `*Specs.cs`, `*Tests.fs`.

## Public Interface

- C#: `public` types and members. Include `protected` members of public types
  that are not sealed. `internal`, `private`, and `file` members are not
  interface. Record `[assembly: InternalsVisibleTo(...)]` or a csproj
  `<InternalsVisibleTo Include=...>` item as an invariant.
- No modifier: top-level types are `internal` and members are `private`.
  Interface and enum members are public. `protected internal` counts as
  protected; `private protected` is not interface. A member is public only
  if every enclosing type is public.
- Merge `partial` types across files into one entry. List extension methods
  as `[file:StaticClass.Method]`, and members of C# 14 `extension(...)`
  blocks the same way.
- For enums, list every member. Status enums are contract.
- Routes: cite the exact template string from `[Route]`, `[HttpGet]`,
  `[HttpPost]` and similar attributes, minimal API calls (`MapGet`,
  `MapPost`, `MapGroup`), and Blazor `@page` directives.
- Blazor components: `[Parameter]` and `[CascadingParameter]` properties and
  `EventCallback` members.
- gRPC: a service is local only if the `.csproj` has
  `<Protobuf Include=...>` for its `.proto` and a class derives from the
  generated `*Base`.
- F#: top-level `let` and `type` in modules without `private` or `internal`.
  If a `.fsi` signature file exists, it alone defines the interface.
- VB: `Public` and `Protected` declarations. `Friend` (the default) is not
  interface; `Protected Friend` counts as protected.

## Definition Patterns

- C#: `namespace` lines, and lines declaring `class`, `interface`, `struct`,
  `record`, `enum`, or `delegate` (after any attributes and modifiers).
- F#: lines starting with `module`, `type`, or top-level `let`.
- VB: `Class`, `Module`, `Interface`, `Structure`, `Enum`, `Sub`, `Function`.

## Read Order

- Contracts: the directory's `*.csproj` / `*.fsproj` (`TargetFramework`,
  `PackageReference`, `ProjectReference` are dependencies), interface files
  (`I*.cs` that declare an `interface`), `.fsi` files, `.proto` files.
- Configuration: `appsettings*.json`, `Web.config`, and `App.config` keys
  only. Never copy values; they may
  hold secrets.
- Entry points: `Program.cs`, `Startup.cs`, `Global.asax.cs`,
  `MauiProgram.cs`, `App.xaml.cs`, `Worker.cs`, `App.razor`,
  `_Imports.razor`, `Program.fs`.
- EF Core `Migrations/`: read only `*ModelSnapshot.cs` for table and column
  names; skip the timestamped migration files.

## Signals

- Invariants: `ArgumentNullException.ThrowIfNull`, `ArgumentException.ThrowIf*`,
  `ArgumentOutOfRangeException.ThrowIf*`,
  guard clauses that throw, `Debug.Assert`, DataAnnotations (`[Required]`,
  `[Range]`, `[StringLength]`), FluentValidation `RuleFor`, `required` and
  `init` members, `sealed` types, `<Nullable>enable</Nullable>`, and DI
  lifetimes (`AddSingleton`, `AddScoped`, `AddTransient`).
- Side effects: `HttpClient` / `IHttpClientFactory`, `DbContext` and
  `SaveChanges` / `SaveChangesAsync`, `File`, `Directory`, `Stream`,
  `Process.Start`, `Environment.GetEnvironmentVariable`, `IHostedService` /
  `BackgroundService`, message publishing, `IMemoryCache` /
  `IDistributedCache`, and mutable `static` fields.
- Concurrency: `lock`, `SemaphoreSlim`, `Interlocked`, `Channel<T>`.

## Verification

- Non-SDK-style projects (no `Sdk=` attribute on `<Project>`, typical of
  .NET Framework 4.x): `<test-command>` unless the repository has a test
  script.
- Nearest test project that references `D`'s project:
  `dotnet test path/to/X.Tests.csproj`.
- Otherwise the nearest solution file: `dotnet test <solution file>`. Prefer
  `.slnx` over `.sln` when both exist (`.slnx` needs SDK 9.0.200 or later).
- If `global.json` sets `"test": { "runner": "Microsoft.Testing.Platform" }`,
  use `dotnet test --project <csproj>` or `--solution <solution file>`.
- No test project: `dotnet build` on the nearest project file.
- Never invent a `--filter` expression.
