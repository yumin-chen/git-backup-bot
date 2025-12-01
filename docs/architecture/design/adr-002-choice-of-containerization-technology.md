# ADR-002: Choice of Containerization Technology

**Date:** 2025-11-30
**Status:** Accepted

## Context

The BackupBot application is designed to be a self-contained, portable, and secure service. To meet these requirements, it must be packaged and deployed using a containerization technology. The chosen technology should be compliant with modern standards, emphasize security, and not require a privileged daemon for execution, aligning with the project's principles of security and data sovereignty.

## Decision

We have decided to use **OCI-compliant containers, with Podman as the primary recommended container engine**. The official deployment documentation and `Containerfile` will be tailored for Podman.

## Rationale

The decision to use Podman and OCI containers is based on the following key factors:

1.  **Security (Daemonless Architecture):** Podman operates without a central, privileged daemon. Each container is managed as a child process of the user who starts it. This rootless model is inherently more secure than daemon-based architectures, as it prevents potential container-to-host privilege escalation vulnerabilities through the daemon. This aligns directly with the TSD's emphasis on non-root execution and security.
2.  **OCI Compliance:** Podman is fully compliant with the Open Container Initiative (OCI) standards for container images and runtimes. This means that while we recommend Podman, the `Containerfile` we produce can be built and run by any other OCI-compliant engine, such as Docker, containerd, or Buildah, ensuring broad compatibility and avoiding vendor lock-in.
3.  **Developer Experience:** The Podman command-line interface (CLI) is a drop-in replacement for the Docker CLI. Developers familiar with Docker can adopt Podman with virtually no learning curve, which is beneficial for an open-source project.
4.  **Ecosystem Integration:** Podman integrates well with modern Linux systems that use systemd for service management, allowing containers to be managed as systemd services for robust, production-grade deployments.

## Alternatives Considered

*   **Docker Engine:** Docker is the most widely known container engine and has a vast ecosystem. However, its reliance on a privileged, root-owned daemon presents a larger attack surface than Podman's daemonless model. While Docker can be run in a rootless mode, it is not the default and can have limitations. Given the security focus of BackupBot, Podman's default security posture is preferable.
*   **systemd-nspawn:** This is a containerization technology that is tightly integrated with systemd. While it is very powerful for Linux-based deployments, it is not OCI-compliant and lacks the cross-platform (e.g., macOS) developer tooling that Podman and Docker provide.

## Consequences

*   **Positive:**
    *   Improved security posture due to the default rootless, daemonless architecture.
    *   Full compatibility with the broader OCI container ecosystem.
    *   Easy adoption for developers familiar with Docker.
*   **Negative:**
    *   Some less-common, third-party tools that are hard-coded to interact with the Docker daemon's socket (`/var/run/docker.sock`) may not work with Podman out of the box, though this is becoming less common.
    *   While Podman is a first-class citizen on Linux, the user experience on macOS and Windows relies on a virtual machine, which can be more complex than Docker Desktop for some users. However, the primary deployment target for the application itself is a Linux server.
