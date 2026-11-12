<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# JVM Language Pack (Java, Kotlin, Scala, Groovy)

## Detection

- `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle`,
  `settings.gradle.kts`, `build.sbt`.

## Source Extensions

- `.java`, `.kt`, `.kts` (except `*.gradle.kts`), `.scala`, `.sc`,
  `.groovy`.

## Ignored Paths

- `target/`, `build/`, `out/`, `.gradle/`, `.idea/`, `.bsp/`.

## Test Conventions

- Source sets `src/test/` and `src/integrationTest/`.
- Files `*Test.java`, `*Tests.java`, `*IT.java`, `*Test.kt`, `*Spec.scala`,
  `*Spec.groovy`.

## Public Interface

- Java: `public` types and members, and `protected` members of public types
  that are not `final`. If `module-info.java` exists, only `exports`
  packages are interface.
- Interface members and enum constants are implicitly public. No modifier
  means package-private, which is not interface.
- Kotlin: declarations are public unless marked `private`, `protected`, or
  `internal`. `internal` is module-only and not interface. `protected`
  members of `open` classes count as protected.
- Scala: members without `private` or `protected` modifiers.
- Routes: cite the exact path from Spring `@RequestMapping`, `@GetMapping`,
  `@PostMapping` and similar, JAX-RS `@Path`, and Ktor `routing { get("/x") }`.

## Definition Patterns

- Lines declaring `class`, `interface`, `enum`, `record`, `@interface`,
  `object`, `trait`, `fun`, or `def`, after annotations and modifiers.

## Read Order

- Contracts: interfaces, JPA entities (`@Entity`, `@Table(name = ...)`),
  OpenAPI specs, and the module's build file dependencies.
- Entry points: classes with `main`, `@SpringBootApplication` classes, and
  `Application.kt`.

## Signals

- Invariants: `Objects.requireNonNull`, `require` / `check` (Kotlin),
  Bean Validation (`@NotNull`, `@Valid`, `@Size`), `final` fields, and
  `synchronized` / `ReentrantLock`.
- Side effects: `@Transactional`, JDBC / JPA repositories, HTTP clients
  (`RestTemplate`, `WebClient`, `HttpClient`), `java.nio.file`, messaging
  (`@KafkaListener`, `JmsTemplate`), `System.getenv`, and `@Scheduled`.

## Verification

- Maven: `mvn -pl <module> -am test`, with `<module>` as the path relative
  to the root `pom.xml` (use `./mvnw` when the wrapper exists). Single
  module: `mvn test`.
- Gradle: `./gradlew :a:b:test`, using the project path from `include` in
  `settings.gradle*` (`gradle` without a wrapper). Kotlin Multiplatform:
  `:<module>:allTests`. Single project: `./gradlew test`.
- sbt: `sbt <project>/test` (`<project>` is the sbt project id).
- Prefix `cd <project_dir> &&` when the build root is not the repository
  root.
