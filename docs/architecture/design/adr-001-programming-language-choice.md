# ADR-001: Programming Language Selection

**Date:** 2025-11-30
**Status:** Proposed

## Context

The git-backup-bot application requires a programming language that is well-suited for file system operations, process management, and interaction with external command-line tools like Git. The language needs a robust ecosystem with libraries for file monitoring, configuration parsing, and potentially cryptographic operations. As the project is open-source and emphasizes data sovereignty, the chosen language should be widely adopted, easy to learn, and not tied to a proprietary ecosystem.

## Decision

We have decided to use **Python 3.11+** as the primary programming language for the BackupBot application.

## Rationale

The decision to use Python is based on the following factors:

1.  **Rich Ecosystem:** Python has an extensive standard library and a vast ecosystem of third-party packages that directly address the project's needs. Key libraries identified in the TSD, well‑supported libraries for file system monitoring, configuration parsing, and potentially cryptographic operations, and libraries for Git integration, file monitoring, YAML/SQLite handling, and  `watchdog` for file monitoring and `PyYAML` for configuration, are mature and well-maintained.
2.  **Maintainability and Readability:** Python's clean syntax and high-level abstractions make it well-suited for rapid development and long-term maintainability. This is particularly important for an open-source project that aims to attract contributions from a diverse community. It's good for rapid prototyping, extensive testing frameworks.
3.  **Excellent Glue Language:** Python is highly effective at orchestrating and interacting with command-line tools. This is a critical requirement for BackupBot, which relies heavily on Git, Git LFS, and potentially `git-crypt` or `gpg`.
4.  **Cross-Platform Support:** Python is widely available on the target platforms (Linux, macOS) and its libraries generally offer good cross-platform compatibility, which keeps future options open. It's also well‑supported in Alpine and other minimal base images.
5.  **Strong Community and Talent Pool:** Python is one of the most popular programming languages in the world, ensuring a large talent pool for future development and a wealth of community-provided resources and support. It also has broad DevOps tooling and documentation.
6.  **Performance considerations:** Python is acceptable for an I/O‑bound tool; Python’s runtime overhead is mitigated by batch operations.



## Alternatives Considered

*   **Go:** Go is a strong candidate, particularly for its performance, static typing, and straightforward concurrency model. However, its ecosystem for file system monitoring is less mature than Python's, and its syntax is generally considered more verbose for scripting-style tasks.
*   **Rust:** Rust offers the highest level of performance and memory safety, which are attractive qualities. However, it has a significantly steeper learning curve than Python, which could be a barrier to entry for potential contributors. The development velocity for a tool like BackupBot would likely be slower in Rust.

## Consequences

*   **Positive:**
    *   Faster initial development and prototyping.
    *   Lower barrier to entry for new contributors.
    *   Leverage mature and reliable libraries for core functionality.
*   **Negative:**
    *   Python's performance will be lower than that of compiled languages like Go or Rust, though this is not expected to be a bottleneck for an I/O-bound application like BackupBot.
    *   Dependency management in Python can be complex, though this will be mitigated by using a clear `requirements.txt` and containerization.
