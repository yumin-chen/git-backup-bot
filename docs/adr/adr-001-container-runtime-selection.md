# ADR-001: Container Runtime Selection

## Status
Proposed

## Context
BackupBot requires containerization to:

- Ensure reliable, replicable deployment across multiple environments (development, CI, production).
- Provide isolation for process security, credential management, and ease of scaling.
- Support non-root execution and minimal OS footprint for best security practices.

The primary candidates considered for the container runtime were Docker Engine, Podman, and containerd.

### Evaluation Factors
- **Rootless Operation:** Podman natively supports rootless containers, reducing attack surface and aligning with BackupBot’s security requirements.
- **Open Source Governance:** Podman is developed under open source licenses and is maintained by Red Hat, with broad community adoption and no proprietary lock-in.
- **Compatibility:** Podman is OCI-compliant, supporting most Dockerfile workflows and compatible with CI/CD pipelines and orchestration (Kubernetes/Openshift).
- **Sovereignty and Supply Chain:** Podman can be installed and run without relying on cloud services, proprietary registries, or US-based vendor dependencies, benefiting sovereignty-conscious deployments.

## Decision
**Podman** is selected as the default container runtime for all BackupBot development, deployment, and scaling scenarios.

- All container images, deployment scripts, and documentation will focus on Podman usage.
- Compatibility with Docker Engine will be maintained where feasible, but not guaranteed.
- Multi-stage builds will be tested and validated in Podman first.
- Rootless deployment WILL BE the recommended mode.

## Consequences
- The team will rely on Podman CLI for development and operations.
- All CI/CD pipelines must use Podman for builds and tests.
- Developers must ensure that all images build and run successfully in Podman.
- Minor compatibility adjustments may be needed for Docker-specific features or entrypoints.
- Documentation will reference Podman commands and troubleshooting processes.

## Alternatives Considered
- **Docker Engine:** High ecosystem support, but stricter rootless constraints and higher supply chain centralization.
- **containerd:** Lower-level, less mature developer tooling.

## Related ADRs
- ADR-002: Base Image Selection
- ADR-011: Deployment and Scalability Practices

## Date
2025-12-01
