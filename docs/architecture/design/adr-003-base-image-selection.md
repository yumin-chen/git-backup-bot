# ADR-003: Base Image Selection

**Date:** 2025-12-01
**Status:** Proposed

## Context
BackupBot must run in a lightweight, secure, and maintainable container environment. The base image choice determines the default packages, update frequency, security profile, and compatibility with application dependencies.

We considered several candidates:
- **Alpine Linux:** Highly minimal, security-focused, popular in container ecosystems, community maintained, low US dependency.
- **Debian/Ubuntu:** Well-supported, bigger image size, broader package library, higher memory footprint.
- **Other minimal distributions:** BusyBox, Distroless; very small, but may lack required features or libraries.

## Decision
**Alpine Linux** is selected as the mandatory base image for the BackupBot container in all deployment environments.

- Multi-stage builds will begin from the latest stable Alpine image (`alpine:latest`), with explicit version pinning where security or compatibility is required.
- All dependencies will be installed via Alpine’s APK package manager.
- Compatibility with other base images (Debian, Ubuntu) may be maintained for advanced users, but Alpine will be the default and recommended choice.

## Rationale
1.  **Minimal Footprint:** Alpine's small size reduces the attack surface and improves container startup time.
2.  **Security & Updates:** Alpine provides rapid security patches and is responsive to CVEs.
3.  **Supply-Chain Sovereignty:** Maintained in Switzerland by an open community, reducing reliance on US-based vendors and aligning with our goal of vendor neutrality.
4.  **Compatibility:** Supports Python 3.11+, Git LFS, SQLite, watchdog, PyYAML, and other required libraries.
5.  **Community Support:** Abundant usage guidance and established best practices in cloud-native and security-focused deployments.

## Alternatives Considered
- **Debian/Ubuntu:** Larger images, easier native package installation, but less optimal for minimal runtime environments due to higher memory footprint and larger attack surface.
- **Distroless/BusyBox:** Too minimal; lacks required functionality for Python and Git-based workflows.

## Consequences
### Positive
- Container images will be small and fast.
- Updates for critical fixes are easily maintained.
- Reduced reliance on single-vendor ecosystems.

### Negative
- Developers must test for Alpine-specific compatibility issues (e.g., `musl` vs `glibc`).
- Some debugging or legacy libraries may require alternatives or additional configuration compared to Debian-based images.

## Related ADRs
- ADR-002: Container Runtime Selection
- ADR-011: Deployment and Scalability Practices