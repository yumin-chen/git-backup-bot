# ADR-004: Choice of Large File Handling

**Date:** 2025-11-30
**Status:** Accepted

## Context

The BackupBot application is designed to back up the contents of local directories, which may contain large binary files such as images, videos, archives, or other assets. Storing large files directly in a Git repository is inefficient, bloats the repository size, and significantly degrades the performance of Git operations like cloning and pulling. A specialized solution is required to handle these large files efficiently while keeping the core Git repository small and fast.

## Decision

We have decided to use **Git LFS (Large File Storage)** as the standard mechanism for handling files that exceed a configurable size threshold. The BackupBot will be responsible for automatically tracking, uploading, and managing files with Git LFS.

## Rationale

The decision to adopt Git LFS is based on the following primary reasons:

1.  **Industry Standard and Wide Support:** Git LFS is the de facto industry standard for managing large files in Git. It is supported by virtually all major Git hosting providers, including GitHub, GitLab, Gitea, and Codeberg, which are the recommended remote targets in the TSD. This ensures broad compatibility and a seamless user experience.
2.  **Transparent Integration with Git:** Git LFS integrates cleanly with the standard Git workflow. Once a file type is tracked, developers and users can use their normal `git add`, `git commit`, and `git push` commands. Git LFS works in the background to replace large file contents with small text pointers, which is exactly the behavior required for BackupBot's automated commits.
3.  **Keeps Repository Size Small:** By storing only pointers in the Git repository and the actual file contents in a separate object store, Git LFS keeps the repository history small and fast. This is critical for the long-term performance and maintainability of the backup archives.
4.  **Existing Tooling:** Git LFS is a mature, open-source tool with a stable command-line interface. BackupBot can reliably call the `git lfs` command to perform its operations, rather than having to implement a complex file-chunking and uploading protocol from scratch.

## Alternatives Considered

*   **git-annex:** `git-annex` is a powerful and flexible alternative to Git LFS. It offers more complex and customizable workflows, allowing files to be stored in many different types of locations (e.g., S3, rsync.net, local drives). However, its setup and usage are significantly more complex than Git LFS. For the primary use case of BackupBot—backing up to a central Git remote—the simplicity and widespread provider support of Git LFS are more advantageous.
*   **DVC (Data Version Control):** DVC is another excellent tool for versioning large files and datasets, often used in machine learning workflows. It is more focused on versioning data pipelines and artifacts than on general-purpose file backups. Integrating it would require a separate workflow alongside Git, whereas Git LFS is a direct extension of the core Git workflow.
*   **Custom Solution (e.g., rsync + Git):** We could have designed a hybrid system where Git tracks metadata and a separate tool like `rsync` or a custom script uploads large files to an object store (like S3). This would give us complete control but would require reinventing the wheel. It would be a significant engineering effort to build a robust and reliable solution that matches the maturity of Git LFS.

## Consequences

*   **Positive:**
    *   The backup repositories will remain small and performant.
    *   The solution is compatible with the vast majority of Git hosting providers.
    *   The implementation is simplified by leveraging a mature, existing command-line tool.
*   **Negative:**
    *   Users of BackupBot will need to have the Git LFS client installed on their host machine for both the bot to function and for them to perform manual restores.
    *   Storage and bandwidth for LFS objects are often metered and charged separately by hosting providers. The TSD accounts for this by requiring LFS quota monitoring and alerting.
