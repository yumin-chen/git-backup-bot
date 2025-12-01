# ADR-002: Base Image Selection

**Date:** 2025-11-30  
**Status:** Proposed

## Context
BackupBot must run in a lightweight, secure, and maintainable container environment. The base image choice determines the default packages, update frequency, security profile, and compatibility with application dependencies.

### Candidates Considered

- **Alpine Linux:** Highly minimal, security-focused, popular in container ecosystems, community maintained, low US dependency.
- **Debian/Ubuntu:** Well-supported, bigger image size, broader package library, higher memory footprint.
- **Other minimal distributions:** BusyBox, Distroless; very small, but may lack required features or libraries.

### Evaluation Factors

- **Minimal footprint:** Reduces security risk and container startup time.
- **Update cadence:** Alpine updates frequently and is responsive to CVEs.
- **Compatibility:** Alpine supports Python 3.11+, Git LFS, SQLite, watchdog, PyYAML, and other required libraries.
- **Supply chain:** Alpine is maintained in Switzerland by an open community, reducing reliance on US-based vendors.
- **Community support:** Abundant usage guidance and established best practices in cloud-native and security-focused deployments.

## Decision
**Alpine Linux** is selected as the base image for the BackupBot container in all deployment environments.

- Multi-stage builds will begin from the latest stable Alpine image (`alpine:latest`), with explicit version pinning where security or compatibility is required.
- All dependencies will be installed via Alpine’s APK package manager.
- Compatibility with other base images (Debian, Ubuntu) may be maintained for advanced users, but Alpine will be the default and recommended choice.

## Consequences

- Container images will be small and fast.
- Updates for critical fixes are easily maintained.
- Developers must test for Alpine-specific compatibility issues (e.g., `musl` vs `glibc`).
- Some debugging or legacy libraries may require alternatives on other base images.

## Alternatives Considered

- **Debian/Ubuntu:** Larger images, easier native package installation, but less optimal for minimal runtime environments.
- **Distroless/BusyBox:** Not enough required functionality for Python and Git-based workflows.

## Related ADRs

- ADR-001: Container Runtime Selection (Podman)
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01