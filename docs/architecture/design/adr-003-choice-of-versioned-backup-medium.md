# ADR-003: Choice of Versioned Backup Medium

**Date:** 2025-11-30  
**Status:** Proposed

## Context
BackupBot must store backup data in a versioned, reliable, and efficient medium that supports incremental changes, large binary files, and easy synchronization with remote repositories.

## Decision
We have decided to use **Git with Git LFS** as the versioned backup medium for all BackupBot data.

## Rationale
- **Version Control:** Git provides robust change tracking, branching, and history.
- **Large File Support:** Git LFS handles large binaries efficiently, keeping the repository lightweight.
- **Ecosystem Integration:** Works seamlessly with remote hosting services (GitHub, GitLab, Gitea, Codeberg).
- **Operational Resilience:** Distributed nature allows offline work and recovery from network failures.
- **Developer Familiarity:** Most engineers are already comfortable with Git workflows.

## Alternatives Considered
- **git-annex:** Powerful but more complex and less mainstream for typical backup use cases.
- **DVC:** Focused on data science pipelines; adds unnecessary complexity for generic backups.
- **Custom rsync solution:** Would require building and maintaining a bespoke large‑file handling system.

## Consequences
- **Positive:** Leverages mature tooling, simplifies user onboarding, and ensures compatibility with many hosting providers.
- **Negative:** Users must install the Git LFS client and monitor LFS storage quotas.

## Related ADRs
- ADR-001: Container Runtime Selection (Podman)
- ADR-002: Base Image Selection (Alpine Linux)
- ADR-004: Choice of Large File Handling (Git LFS)

## Date
2025-12-01
