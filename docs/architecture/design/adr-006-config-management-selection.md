# ADR-006: Configuration Management Library Selection

## Status
Proposed

## Context
BackupBot requires a human-editable, versioned configuration for directories, debounce settings, LFS thresholds, retry policies, and encryption options. This configuration must be easily readable and writable, support schema validation, and fit smoothly into the Python ecosystem.

### Candidates Considered

- **PyYAML:** Well-supported Python library for reading/writing YAML, supports complex structures, active maintenance.
- **TOML:** Increasingly popular for configs, but less natively supported in older Python codebases.
- **JSON:** Standard but less readable/writable for complex hierarchical configs.

### Evaluation Factors

- **Human readability:** YAML excels for complex, nested structures and is familiar to most devops engineers.
- **Features:** PyYAML supports custom validation, schema evolution, and hot-reloading.
- **Python integration:** PyYAML is a mature library, easy to install and pin, and works in Alpine containers.
- **Community adoption:** YAML is the default for many container and CI/CD workflows, documentation, and configuration files.

## Decision
**PyYAML with a YAML schema** is selected for BackupBot configuration management.

- All runtime and deploy-time configuration will use YAML files validated and loaded via PyYAML.
- Versioning and hot-reloading mechanisms will be built on PyYAML’s parsing and event hooks.
- Schema validation will be enforced before run, errors logged and surfaced to the operator.

## Consequences

- All config documentation and samples will be YAML-based.
- Team must maintain YAML schemas and validation logic.
- PyYAML vulnerabilities and breaking changes will be tracked with security updates.
- Advanced features (e.g., JSONSchema for YAML, migration helpers) may be considered later.

## Alternatives Considered

- **TOML:** Simpler structure, good for small configs, but less adopted outside Python packaging.
- **JSON:** Universal, but difficult to manually edit for nested and optional fields.

## Related ADRs

- ADR-004: Python 3.11+ as Implementation Language
- ADR-001: Container Runtime Selection
- ADR-002: Base Image Selection

## Date
2025-12-01