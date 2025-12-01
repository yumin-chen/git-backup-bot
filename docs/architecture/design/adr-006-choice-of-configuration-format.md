# ADR-005: Choice of Configuration Format

**Date:** 2025-11-30
**Status:** Accepted

## Context

The BackupBot application requires a configuration file to define its behavior, including the directories to monitor, Git remote details, LFS thresholds, and logging settings. The chosen format must be human-readable and easy to edit, support hierarchical data structures, and allow for comments to aid in documentation. It should also be widely supported in the Python ecosystem with mature and reliable parsing libraries.

## Decision

We have decided to use **YAML (YAML Ain't Markup Language)** as the format for the application's configuration file. The primary configuration file will be `config.yaml`.

## Rationale

The decision to use YAML is based on the following advantages:

1.  **Human Readability:** YAML is designed to be easily readable by humans. Its use of indentation to denote structure results in clean, uncluttered configuration files that are easy to understand and modify. This is a significant advantage for a tool that users will need to configure themselves.
2.  **Support for Comments:** YAML has native support for comments, which is crucial for creating well-documented example configuration files. This allows us to explain the purpose of each setting directly within the file.
3.  **Hierarchical Structure:** YAML naturally represents the hierarchical data structures that the application's configuration requires (e.g., nested settings for `git`, `lfs`, and `logging`).
4.  **Mature Python Library:** The `PyYAML` library is the de facto standard for parsing YAML in Python. It is mature, feature-rich, and reliable, meeting the TSD's requirement for a low-risk dependency.
5.  **Wide Adoption in DevOps:** YAML is the most common configuration format in the modern DevOps and cloud-native ecosystem (e.g., Kubernetes, Docker Compose, CI/CD pipelines). Using YAML makes the tool feel familiar to its target audience.

## Alternatives Considered

*   **JSON (JavaScript Object Notation):** JSON is another excellent, widely supported format. However, it has two main drawbacks for this use case: it does not support comments, which makes creating self-documenting configuration files more difficult, and its syntax (requiring quotes around all keys and commas between all elements) is generally considered less human-friendly than YAML's.
*   **TOML (Tom's Obvious, Minimal Language):** TOML is a strong alternative that is also designed for human readability and is the standard for Python's `pyproject.toml` files. It is an excellent format, but YAML's block-style syntax for nested structures can be slightly cleaner for the complex configuration that BackupBot requires. While the choice between YAML and TOML is largely a matter of style, YAML's broader adoption in the general DevOps space makes it a slightly more conventional choice.
*   **INI Files:** The classic INI format is simple for flat key-value pairs but becomes cumbersome for representing the nested, hierarchical data that BackupBot's configuration needs.

## Consequences

*   **Positive:**
    *   The configuration file will be easy for users to read, understand, and edit.
    *   The use of comments will improve the clarity of the example configuration.
    *   The format is familiar to the target audience of developers and system administrators.
*   **Negative:**
    *   YAML parsing can be less performant than JSON parsing, but this is completely irrelevant for a configuration file that is read only on application startup.
    *   The YAML spec is complex, and indentation errors can be a common source of user frustration. This will be mitigated by providing a clear and well-structured example file.
