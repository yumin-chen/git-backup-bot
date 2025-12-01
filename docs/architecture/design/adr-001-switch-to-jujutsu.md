# ADR-001: Switch from Git to Jujutsu for Core VCS Operations

**Date:** 2025-12-01
**Status:** Accepted

## Context

The previous version of BackupBot was built on Git for its core version control operations. While Git is a powerful and widely-used VCS, it presents several challenges for our specific use case of automated, continuous backups:

* **Working Directory Interference:** Direct Git operations can interfere with a user's local Git workflow, leading to potential conflicts, accidental commits, and unexpected behavior.
* **Complexity of State Management:** Managing a clean, linear history of backups in a separate branch while ensuring atomicity and handling potential failures can be complex.
* **Performance:** Git's performance can degrade in repositories with a very large number of files or a high churn rate.
* **LFS Dependency:** The reliance on Git LFS for large file support adds another layer of complexity and a potential point of failure.

## Decision

We have decided to migrate the core VCS engine of BackupBot from Git to [Jujutsu (jj)](https://github.com/martinvonz/jj). Jujutsu is a modern, Git-compatible VCS that offers several advantages for our use case:

* **Conflict-Free Commits:** Jujutsu's design avoids many of the common sources of conflicts in Git, making it better suited for automated operations.
* **Immutable Operation Log:** Every change in Jujutsu is recorded in an immutable operation log, providing a reliable and auditable history of all actions.
* **Git Interoperability:** Jujutsu can read from and write to Git repositories, allowing us to maintain compatibility with existing Git-based remotes and workflows.
* **Built-in File Watcher:** Jujutsu's native file watcher is more efficient and reliable than external solutions like `watchdog`.
* **Simplified Architecture:** The use of a "shadow" Jujutsu repository in a sidecar container completely isolates the backup process from the user's local Git environment.

## Consequences

### Positive

* **Improved Reliability:** The isolated, conflict-free nature of Jujutsu significantly improves the reliability of the backup process.
* **Simplified Architecture:** The two-container architecture with a dedicated `jj-sidecar` simplifies state management and reduces the potential for errors.
* **Enhanced Performance:** Jujutsu's performance characteristics are better suited for our high-frequency, automated commit workload.
* **Reduced Dependencies:** We are no longer reliant on Git LFS, as Jujutsu's native object model handles large files more efficiently.

### Negative

* **New Technology:** Jujutsu is a newer and less well-known technology than Git, which may present a learning curve for some users and contributors.
* **Tooling and Integration:** The ecosystem of tools and integrations for Jujutsu is not as mature as Git's.

## Technical Details

The implementation of this decision is detailed in the updated [Technical Specification Document (TSD)](../../technical/specs/tsd-000-automated-backup-system.md).
