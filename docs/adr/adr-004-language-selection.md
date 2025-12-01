# ADR-004: Python 3.11+ as Implementation Language

## Status
Proposed

## Context
BackupBot’s requirements include cross-platform support, advanced file system monitoring, Git/LFS integration, and reliability in both container and host environments. The main candidates for the implementation language were Python, Go, and Rust.

### Evaluation Factors

- **Ecosystem:** Python has robust libraries for Git integration (`GitPython`), file monitoring (`watchdog`), YAML and SQLite handling (`PyYAML`, `sqlite3`).
- **Maintainability:** Python’s syntax and standard library enable rapid prototyping, easier onboarding, and extensive testing frameworks.
- **Container compatibility:** Python is well-supported in Alpine and other minimal container base images.
- **Community support:** Python’s ecosystem covers logging, encryption, metrics/monitoring, and more, minimizing the need for custom implementations.
- **Performance:** While Go and Rust offer higher performance for compute-heavy tasks, BackupBot’s workload is not CPU-bound, except for file change detection and batch operations.
- **Extensibility:** Python enables flexible plugin architectures and fast iteration for future features (multi-remote, restore workflows).

## Decision
**Python 3.11+** is selected as the primary implementation language for all core BackupBot components.

- All central workflows (file monitoring, config parsing, Git operations, queue management) will be written in Python.
- Required dependencies will specify compatibility with Python 3.11+.
- Container images will use Alpine Linux’s Python packages, verified for stability and security.
- Plugin and extension mechanisms will target Python interfaces and package standards.

## Consequences

- The team must maintain Python best practices, follow security updates, and pin dependency versions for repeatability.
- Python’s runtime overhead will be mitigated with batch operations and optimizations for I/O.
- Developers can leverage a wide range of third-party packages for encryption, observability, and resilience.
- Advanced users may request future command-line utilities or integrations in other languages, which can be considered via clear interfaces.

## Alternatives Considered

- **Go:** Faster, robust concurrency, easier cross-compilation, but fewer batteries-included file monitoring and YAML support.
- **Rust:** High performance and security, but slower for prototyping and fewer established ecosystem packages for “glue” work.

## Related ADRs

- ADR-001: Container Runtime Selection (Podman)
- ADR-002: Base Image Selection (Alpine Linux)
- ADR-003: Git + Git LFS as Versioned Backup Medium

## Date
2025-12-01
