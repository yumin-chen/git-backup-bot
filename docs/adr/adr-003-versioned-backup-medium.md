# ADR-003: Git + Git LFS as Versioned Backup Medium

## Status
Proposed

## Context
BackupBot is designed to version, store, and synchronize changes in local directories to remote storage with durability and traceability. This requires a backup medium that can:

- Track incremental changes across many files.
- Efficiently handle large binary files.
- Enable restore workflows for point-in-time states.
- Integrate with remote repositories and support data sovereignty goals.

### Candidates Considered

- **Git with Git LFS:** Ubiquitous, well-documented, version control and LFS extension for large files.
- **git-annex:** More complex, additional repository setup, eccentric user experience.
- **DVC:** Data science focused, heavier dependencies, less suited for generic file backup.
- **Fossil/Pijul:** Niche user base, less integration with LFS workflows.

### Evaluation Factors

- **Version control:** Git is optimized for change tracking, branching, and commit history.
- **Large file handling:** Git LFS provides automated detection and transfer of files exceeding specified thresholds.
- **Ecosystem integration:** Git is supported by nearly all remote hosting options (Gitea, GitLab, Codeberg, GitHub).
- **Restore functionality:** Native support for checkout, shallow clones, and targeted file restores.
- **Operational resilience:** Git’s distributed model supports local and network outage recovery.
- **User experience:** Most devops and engineering teams are well-versed in Git workflows.

## Decision
**Git with Git LFS** is selected as the versioned backup medium for BackupBot’s core workflows.

- All tracked directories are initialized as Git repositories (with `.git` and `.gitattributes` supporting LFS).
- Files above a configurable size threshold or matching specified extensions are handled by Git LFS.
- Commit and push workflows will batch changes, preserve commit timestamps, and use branch/tag strategies for organization.
- Restore operations will use `git clone`, shallow cloning, and LFS pulls for complete or selective file recovery.

## Consequences

- All backup and restore logic will be built atop Python’s Git and LFS bindings or external CLI, tested for container compatibility.
- Users will benefit from mature documentation, tooling, and hosting provider support.
- LFS quota usage and failure modes will be monitored, with operational alerts for limits and errors.
- Users may need to maintain LFS remote storage and quota, and prune old LFS objects as needed.
- Some advanced Git or LFS features (e.g., git-annex symlink handling) may require future extension.

## Alternatives Considered

- **git-annex:** Powerful, but has more learning curve and more complex remote setup.
- **DVC:** Excellent for pipelines, but too heavy for generic backup cases.
- **Fossil/Pijul:** Less battle-tested for this use case.

## Related ADRs

- ADR-001: Container Runtime Selection (Podman)
- ADR-002: Base Image Selection
- ADR-009: Encryption and Credential Management
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01