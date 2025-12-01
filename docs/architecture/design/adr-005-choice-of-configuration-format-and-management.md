# ADR-005: Choice of Configuration Format and Management Library

**Date:** 2025-11-30  
**Status:** Accepted

## Context
BackupBot requires a human‑editable configuration file to define directories to monitor, Git remote details, LFS thresholds, retry policies, and encryption options. The configuration system must be versioned, easy to read/write, support hierarchical structures, allow comments, and integrate cleanly with the Python codebase.

## Decision
We have decided to use **YAML** as the configuration format and **PyYAML** as the library for parsing, validation, and schema handling. The primary configuration file will be `config.yaml`.

## Rationale
- **Human Readability & Comments:** YAML supports comments and a clean indentation‑based syntax, making configuration files approachable for users.
- **Hierarchical Structure:** Naturally represents nested settings (e.g., `git`, `lfs`, `logging`).
- **Mature Python Library:** PyYAML is the de‑facto standard, well‑maintained, and integrates with Python’s `sqlite3` and other modules.
- **DevOps Familiarity:** YAML is ubiquitous in Kubernetes, Docker Compose, CI/CD pipelines, aligning with the target audience’s expectations.
- **Schema Validation:** We can define a YAML schema (e.g., using `jsonschema` or custom validation) to ensure configuration correctness before runtime.

## Alternatives Considered
- **JSON:** No native comment support; more verbose for nested structures.
- **TOML:** Good readability but less widespread in DevOps tooling; fewer validation libraries.
- **INI:** Too flat for the required hierarchical configuration.

## Consequences
- **Positive:** Easy for users to edit and understand; leverages existing tooling and libraries.
- **Negative:** YAML’s indentation sensitivity can cause user errors; mitigated by providing example files and validation.

## Related ADRs
- ADR‑004: Python 3.11+ as Implementation Language (provides the runtime for PyYAML).
- ADR‑001: Container Runtime Selection (Podman).
- ADR‑002: Base Image Selection (Alpine Linux).

## Date
2025-12-01
