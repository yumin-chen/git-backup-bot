# ADR-001: Programming Language Selection

**Date:** 2025-12-01
**Status:** Accepted

## Context
The git-backup-bot application requires a programming language that is well-suited for file system operations, process management, and interaction with external command-line tools like Git. The language needs a robust ecosystem with libraries for file monitoring, configuration parsing, and potentially cryptographic operations. As the project is open-source and emphasizes data sovereignty, the chosen language should be widely adopted, easy to learn, and not tied to a proprietary ecosystem.

## Decision
We have decided to use **Go (Golang)** as the primary programming language for the BackupBot application.

## Rationale
The decision to use Go is based on the following architectural considerations for a containerized, long-running daemon:

1.  **Workload Fit:** The application workload is I/O bound (filesystem watching + Git CLI) and requires high reliability but not heavy compute. Go is optimized for this pattern, offering excellent concurrency primitives (goroutines/channels) for handling file events and process execution without the complexity of async runtimes.
2.  **Containerization & Deployment:**
    *   **Static Binaries:** Go compiles to a single static binary with no runtime dependencies.
    *   **Minimal Footprint:** Allows for extremely small containers (`FROM scratch` or minimal `alpine`), reducing attack surface and image size.
    *   **Cross-Compilation:** Trivial cross-compilation support simplifies building for mixed infrastructure (AMD64/ARM64).
3.  **File-Watching Ecosystem:** The `fsnotify` library in Go is reliable, widely used, and integrates naturally with Go's concurrency model, making it ideal for a long-running watcher daemon.
4.  **Operational "Glue" Code:** Go excels as a language for operational automation. Executing external commands (Git CLI) is straightforward, and error handling is explicit and predictable, which is preferred for operational tools over the complex borrowing/lifetime constraints of Rust.
5.  **Developer Velocity & Maintainability:** Go's minimal syntax and lack of "magic" ensure that the codebase remains readable and easy to onboard for new contributors. It avoids the steep learning curve and compiler friction associated with Rust, ensuring future maintainability.

## Alternatives Considered

*   **Python:** Previously considered for its rich ecosystem and ease of use. However, it requires a heavier runtime environment in the container, has slower startup times, and lacks the type safety and performance benefits of a compiled language. Dependency management can also be more complex compared to Go's single binary.
*   **Rust:** A strong candidate for high-performance systems. However, for this specific use case (I/O automation daemon), Rust adds unnecessary complexity:
    *   **Steeper Learning Curve:** Borrow checker and lifetime management add friction for simple operational tasks.
    *   **Build Complexity:** Slower build times and more complex cross-compilation compared to Go.
    *   **Async Complexity:** Choosing an async runtime (Tokio vs async-std) adds architectural weight not needed for this problem domain.
    *   **Verdict:** Rust is overkill for a Git backup watcher; Go provides the right balance of performance and simplicity.

## Consequences

*   **Positive:**
    *   **Single Binary:** dramatically simplifies deployment and container construction.
    *   **Performance:** Low memory footprint and instant startup.
    *   **Reliability:** Strong typing and explicit error handling reduce runtime errors.
    *   **Maintainability:** Simple language features make it easy for contributors to understand and modify the code.
*   **Negative:**
    *   **Verbosity:** Error handling in Go can be more verbose than in Python (though more explicit).
    *   **Ecosystem:** While strong, some specific niche libraries might be less mature than Python's vast PyPI repository, though core needs (fsnotify, yaml, git execution) are well covered.

## Related ADRs
- ADR-002: Container Runtime & Technology Selection
- ADR-003: Choice of Versioned Backup Medium

## Date
2025-12-01
