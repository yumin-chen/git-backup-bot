# ADR-002: Choice of Base Image

**Date:** 2025-11-30  
**Status:** Accepted

## Context
BackupBot must run in a lightweight, secure, and maintainable container environment. The base image determines default packages, update cadence, security profile, and compatibility with application dependencies.

## Decision
We have decided to use **Alpine Linux** as the default base image for all BackupBot container builds.

## Rationale
- **Minimal Footprint:** Reduces attack surface and container startup time.
- **Frequent Updates:** Alpine provides rapid security patches and CVE response.
- **Compatibility:** Supports Python 3.11+, Git LFS, SQLite, watchdog, and PyYAML.
- **Supply‑Chain Sovereignty:** Maintained in Switzerland by an open community, limiting reliance on US‑based vendors.
- **Community Support:** Widely used in cloud‑native and security‑focused deployments.

## Alternatives Considered
- **Debian/Ubuntu:** Larger images with broader package libraries but higher memory footprint.
- **Distroless/BusyBox:** Too minimal for required Python and Git tooling.

## Consequences
- **Positive:** Small, fast images; easier security updates.
- **Negative:** Need to test Alpine‑specific issues (musl vs glibc) and provide alternatives for debugging on other bases.

## Related ADRs
- ADR-001: Container Runtime Selection (Podman)
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01
