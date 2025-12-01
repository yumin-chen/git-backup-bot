# ADR-006: Configuration Format and Management Library Selection

**Date:** 2025-12-01
**Status:** Proposed

## Context
The `git-backup-bot` application requires a human-editable configuration file to define its behavior, including directories to monitor, Git remote details, LFS thresholds, retry policies, and encryption options. The configuration system must be versioned, easy to read and write for humans, support hierarchical structures, allow comments for documentation, and integrate cleanly with the Python codebase. It must also support schema validation to ensure correctness before runtime.

## Decision
We have decided to use **YAML (YAML Ain't Markup Language)** as the configuration format and **PyYAML** as the library for parsing, validation, and schema handling. The primary configuration file will be `config.yaml`.

## Rationale
1.  **Human Readability & Comments:** YAML is designed to be easily readable by humans. Its clean, indentation-based syntax and native support for comments make it approachable for users and allow for self-documenting configuration files.
2.  **Hierarchical Structure:** YAML naturally represents the nested, hierarchical data structures required by the application (e.g., nested settings for `git`, `lfs`, `logging`).
3.  **Mature Python Library:** `PyYAML` is the de-facto standard library for YAML in Python. It is mature, well-maintained, feature-rich, and integrates well with other Python modules, meeting the requirement for a low-risk dependency.
4.  **DevOps Familiarity:** YAML is the standard configuration format in the modern DevOps and cloud-native ecosystem (e.g., Kubernetes, Docker Compose, CI/CD pipelines), making the tool feel familiar to its target audience.
5.  **Schema Validation:** We can define a YAML schema (e.g., using `jsonschema` or custom validation logic) to enforce configuration correctness, ensuring errors are caught and surfaced to the operator before runtime.

## Alternatives Considered
*   **JSON:** A standard format, but lacks native comment support and is more verbose for nested structures (requiring quotes and braces), making it less human-friendly for manual editing.
*   **TOML:** A strong alternative with good readability, but it is less widely adopted in the general DevOps space compared to YAML, and its support for deeply nested structures can be less clean than YAML's block style.
*   **INI:** Too flat and simple for the required hierarchical configuration structure.

## Consequences
*   **Positive:**
    *   The configuration file will be easy for users to read, understand, and edit.
    *   Leverages existing tooling, libraries, and user familiarity.
    *   Enables robust validation through schemas.
*   **Negative:**
    *   YAML's indentation sensitivity can be a source of user errors. This will be mitigated by providing clear, well-structured example files and robust validation error messages.
    *   The team must maintain YAML schemas and validation logic.
    *   PyYAML vulnerabilities must be tracked and patched.

## Related ADRs
*   ADR-004: Python 3.11+ as Implementation Language (provides the runtime for PyYAML).
*   ADR-001: Container Runtime Selection.
*   ADR-002: Base Image Selection.
