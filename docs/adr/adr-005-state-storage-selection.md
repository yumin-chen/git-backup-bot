# ADR-005: State Storage Selection

## Status
Proposed

## Context
BackupBot requires a persistent, transactional, and lightweight database to store its operational state. This includes the change queue, push history, LFS usage metrics, and recovery checkpoints. The chosen solution must be self-contained and require zero-touch administration to align with the project's goal of simple, sovereign deployment.

### Candidates Considered

- **SQLite:** Serverless, public domain, file-based, ACID-compliant SQL database engine.
- **PostgreSQL/MySQL:** Client-server SQL databases requiring a separate, managed service.
- **LMDB (Lightning DB):** High-performance, embedded key-value store.
- **Flat files (JSON, etc.):** Simple, but lack transactional integrity.

### Evaluation Factors

- **Simplicity:** SQLite is serverless and integrated directly into the Python standard library, requiring no external services.
- **Transactional Integrity:** SQLite is fully ACID-compliant, which is critical for preventing state corruption during crashes or interruptions.
- **Portability:** The entire database is a single file, making it trivial to mount, back up, and manage in a container environment.
- **Performance:** SQLite's performance is more than adequate for the serialized, single-writer workload of BackupBot.
- **Ecosystem:** Native support in Python (`sqlite3`) means no external dependencies are needed.

## Decision
**SQLite** is selected as the database engine for storing all of BackupBot's persistent application state. The database will be stored in a single `backup.db` file within a persistent volume.

- The application will interact with the database using Python's built-in `sqlite3` library.
- All state changes (e.g., queue operations) will be wrapped in transactions to ensure atomicity.

## Consequences

- Deployment is simplified, as no external database server is required.
- The application's state is fully portable and easy to manage.
- Concurrency is limited to a single writer, which fits the application's architecture but constrains future designs involving multiple concurrent processes.
- The database size is limited by the host's file system, which is a reasonable trade-off for this use case.

## Alternatives Considered

- **PostgreSQL:** Rejected due to the high operational overhead of requiring a separate server.
- **LMDB:** Rejected because its key-value model is less suitable for the relational queries needed for history and metrics than a SQL database.
- **Flat Files:** Rejected due to the lack of ACID compliance and the high risk of state corruption.

## Related ADRs

- ADR-001: Container Runtime Selection (Podman)
- ADR-004: Language Selection (Python)

## Date
2025-12-01
