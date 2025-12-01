# ADR-004: Choice of Versioned Backup Medium

**Date:** 2025-12-01
**Status:** Proposed

## Context
BackupBot is designed to version, store, and synchronize changes in local directories to remote storage with durability and traceability. This requires a backup medium that can:
- Track incremental changes across many files.
- Efficiently handle large binary files.
- Enable restore workflows for point-in-time states.
- Integrate with remote repositories and support data sovereignty goals.

## Decision
We have decided to use **Git with Git LFS** as the versioned backup medium for all BackupBot data.

- All tracked directories are initialized as Git repositories (with `.git` and `.gitattributes` supporting LFS).
- Files above a configurable size threshold or matching specified extensions are handled by Git LFS.
- Commit and push workflows will batch changes, preserve commit timestamps, and use branch/tag strategies for organization.
- Restore operations will use `git clone`, shallow cloning, and LFS pulls for complete or selective file recovery.

## Rationale
The decision to use Git with Git LFS is based on the following factors:

1.  **Version Control:** Git is optimized for change tracking, branching, and commit history, providing robust versioning capabilities.
2.  **Large File Handling:** Git LFS provides automated detection and transfer of files exceeding specified thresholds, keeping the main repository lightweight.
3.  **Ecosystem Integration:** Git is supported by nearly all remote hosting options (Gitea, GitLab, Codeberg, GitHub), ensuring broad compatibility and avoiding vendor lock-in.
4.  **Operational Resilience:** Git’s distributed model supports local and network outage recovery, allowing for offline work.
5.  **Developer Familiarity:** Most DevOps and engineering teams are well-versed in Git workflows, simplifying onboarding and usage.

## Alternatives Considered
-   **git-annex:** Powerful and flexible, but has a steeper learning curve, more complex remote setup, and an eccentric user experience compared to standard Git.
-   **DVC (Data Version Control):** Excellent for data science pipelines, but introduces heavier dependencies and unnecessary complexity for generic file backup use cases.
-   **Fossil/Pijul:** Niche user bases with less integration for LFS workflows and fewer hosting options.
-   **Custom rsync solution:** Would require building and maintaining a bespoke large-file handling system, reinventing the wheel.

## Consequences
-   **Positive:**
    -   Leverages mature tooling and infrastructure.
    -   Simplifies user onboarding due to familiarity with Git.
    -   Ensures compatibility with a wide range of hosting providers.
-   **Negative:**
    -   Users must install the Git LFS client on their host machines for manual interactions.
    -   LFS storage quotas and bandwidth usage must be monitored, as they are often metered separately by hosting providers.
    -   Users may need to perform maintenance tasks like pruning old LFS objects.

## Related ADRs
- ADR-001: Programming Language Selection (Go)
- ADR-002: Container Runtime & Technology Selection
- ADR-003: Base Image Selection
- ADR-009: Encryption and Credential Management
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01