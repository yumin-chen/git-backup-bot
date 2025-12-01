# ADR-003: Choice of State Storage

**Date:** 2025-11-30
**Status:** Accepted

## Context

The BackupBot application requires a persistent storage mechanism to maintain its internal state and ensure operational resilience. This state includes the change queue, push history, LFS usage metrics, and checkpoints for crash recovery. The chosen solution must be lightweight, self-contained, and not require an external server or complex setup, aligning with the project's goal of being easy to deploy and manage, even in self-hosted environments.

## Decision

We have decided to use **SQLite** as the database engine for storing all persistent application state. The database will be stored in a single file on a persistent volume mounted into the container.

## Rationale

The choice of SQLite is based on the following reasons:

1.  **Zero-Configuration and Serverless:** SQLite is a self-contained, serverless, transactional SQL database engine. It does not require a separate server process to be installed, configured, or managed. This dramatically simplifies the deployment and operational overhead of BackupBot, making it more accessible to a wider range of users.
2.  **Transactional Integrity (ACID):** SQLite is fully ACID-compliant (Atomicity, Consistency, Isolation, Durability). This is a critical requirement for managing the change queue, where operations must be atomic to prevent data loss or duplicate processing, especially during crash recovery.
3.  **Portability and Simplicity:** The entire database is stored in a single file on disk. This makes it incredibly easy to back up, move, and manage the application's state. It fits perfectly with the containerized deployment model, where the state can be persisted by simply mounting a single file or a directory.
4.  **Performance:** For the expected workload of a single-instance backup agent, SQLite's performance is more than sufficient. The database will primarily handle serialized writes to the queue and occasional reads, which SQLite excels at.
5.  **Excellent Python Integration:** Python's standard library includes the `sqlite3` module, providing a robust and well-supported interface out of the box without requiring any external dependencies.

## Alternatives Considered

*   **PostgreSQL or MySQL:** These are powerful, client-server SQL databases. While they offer advanced features and scalability, they would require users to set up and manage a separate database server, which adds significant complexity to the deployment process. This contradicts the goal of making BackupBot a simple, self-contained application.
*   **LMDB (Lightning Memory-Mapped Database):** LMDB is a very high-performance, transactional key-value store. While it is an excellent choice for certain workloads, it is not a relational database. Using it would require building more complex data management logic in the application layer. SQLite's relational model and SQL interface are a better fit for querying and managing the structured state data (like push history) that BackupBot requires.
*   **Flat Files (e.g., JSON, Pickle):** Using simple files for state management is the easiest approach but lacks transactional integrity. A crash during a file write could lead to a corrupted state file, making recovery difficult and unreliable. This does not meet the TSD's requirement for operational resilience.

## Consequences

*   **Positive:**
    *   Simplified deployment and maintenance for the end-user.
    *   Guaranteed transactional integrity for state changes.
    *   No additional external dependencies are required for the application to run.
*   **Negative:**
    *   SQLite is not well-suited for high-concurrency writes from multiple processes. This is not a concern for BackupBot's single-writer architecture but limits future designs that might involve multiple concurrent workers acting on the same database.
    *   The entire dataset must fit on a single host, which limits scalability for extremely large state databases. However, the state data is expected to be small, and this is a reasonable trade-off for the simplicity gained.
