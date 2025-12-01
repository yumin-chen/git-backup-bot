# ADR-006: Configuration Format Selection

## Status
Proposed

## Context
BackupBot requires a user-facing configuration file to define its behavior, including watched directories, Git settings, and logging levels. The format must be human-readable, support comments, handle hierarchical data, and have robust support in the Python ecosystem.

### Candidates Considered

- **YAML:** Human-friendly, supports comments, widely used in DevOps.
- **JSON:** Strict syntax, no comments, but universally supported.
- **TOML:** Well-defined, good readability, popular in the Python ecosystem.
- **INI:** Simple, but struggles with nested or complex data structures.

### Evaluation Factors

- **Human Readability:** YAML's indentation-based syntax is clean and easy for users to read and edit.
- **Comments:** YAML's native support for comments is critical for creating a self-documenting example configuration file.
- **Data Structure Support:** The format must elegantly support nested sections for `git`, `lfs`, etc.
- **Ecosystem:** A mature, low-risk parsing library must be available for Python. `PyYAML` is the standard for this.
- **Familiarity:** YAML is the dominant configuration format in the cloud-native and DevOps space (e.g., Kubernetes, Docker Compose), making it a familiar choice for the target audience.

## Decision
**YAML** is selected as the configuration format for BackupBot. All user-facing configuration will be defined in a `config.yaml` file.

- The application will use the `PyYAML` library to parse the configuration.
- A heavily commented `config.yaml.example` file will be provided to guide users.

## Consequences

- The configuration will be easy for users to manage and understand.
- Indentation errors can be a common source of user error, which will be mitigated by providing a clear example and robust error handling during parsing.
- Parsing performance is secondary to readability for a file that is only read on startup.

## Alternatives Considered

- **JSON:** Rejected primarily due to its lack of support for comments.
- **TOML:** A very strong candidate, but YAML's wider adoption in the general DevOps ecosystem makes it a slightly more conventional choice for this type of application.

## Related ADRs

- ADR-004: Language Selection (Python)

## Date
2025-12-01
