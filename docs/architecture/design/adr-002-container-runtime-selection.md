# ADR-002: Container Runtime & Technology Selection

**Date:** 2025-11-30
**Status:** Proposed

## Context
git-backup-bot requires a containerization strategy to ensure **reliable, replicable deployment** across all environments (development, CI, production) while adhering to **strict security and data sovereignty requirements**. The runtime must:
- Provide strong process isolation and support **non-root execution** by default.
- Be **OCI-compliant** to avoid vendor lock-in and ensure portability.
- Minimize reliance on proprietary or centralised monopoly services (sovereignty).
- Support robust service management for production deployments.
- Be **open-source** and **compliant with project licenses**.

## Decision
We have decided to use **Podman** as the primary container engine and **OCI-compliant containers** as the packaging standard.

- **Podman** is the default runtime for all development, CI/CD, and production workflows.
- **Rootless operation** is the mandatory deployment mode.
- The `Containerfile` will be written to OCI standards; while compatibility with Docker Engine is likely, it is **not guaranteed** as a priority over security features.

## Rationale
The decision is driven by a balance of security architecture and governance needs:

1.  **Security (Daemonless & Rootless):** Podman operates without a central, privileged daemon. Each container runs as a child process of the invoking user. This eliminates the "root daemon" attack surface common in Docker, directly satisfying the requirement for secure, non-root execution.
2.  **Sovereignty & Supply Chain:** Podman is developed under open-source licenses (Red Hat/Community) and can be fully operated without reliance on proprietary registries or centralized cloud services, aligning with the project's data sovereignty goals.
3.  **OCI Compliance:** Podman is fully compliant with Open Container Initiative standards. Images built with Podman can theoretically run on Docker, containerd, or Kubernetes, ensuring the project is not locked into a single tool.
4.  **System Integration:** Podman integrates natively with `systemd`, allowing containers to be managed as standard system services. This is superior for the "set and forget" nature of a backup bot compared to Docker's daemon management.
5.  **Developer Experience:** The CLI is a drop-in replacement for Docker, minimizing the learning curve for contributors.

## Alternatives Considered
-   **Docker Engine:** The industry standard, but its reliance on a privileged root daemon creates a larger attack surface. While "Rootless Docker" exists, it is not the default and has usability limitations. Additionally, Docker's ecosystem is more centralized (Docker Hub), which is less aligned with sovereignty goals.
-   **containerd:** A lower-level runtime excellent for Kubernetes but lacks the high-level developer tooling (CLI) required for easy local development and debugging.
-   **systemd-nspawn:** Highly integrated with Linux/systemd but lacks OCI compliance and cross-platform (macOS/Windows) tooling.

## Consequences
-   **Positive:**
    -   **Security:** Default rootless posture significantly reduces risk.
    -   **Operations:** CI/CD pipelines will use Podman, ensuring builds are reproducible in the target environment.
    -   **Flexibility:** Users are not forced to use a specific vendor's registry or cloud.
-   **Negative:**
    -   **Compatibility:** Some third-party tools hard-coded to look for `/var/run/docker.sock` may require configuration (e.g., using `podman.sock`).
    -   **Cross-Platform:** On macOS and Windows, Podman requires a virtual machine (Podman Machine), which can be slightly more complex to manage than Docker Desktop for novice users.
    -   **Strictness:** Developers must ensure images build in Podman; "it works in Docker" is not a valid acceptance criterion.

## Related ADRs
- ADR-001: Programming Language Selection
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01
