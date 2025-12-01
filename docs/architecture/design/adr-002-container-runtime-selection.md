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

* **Runtime:** **Podman** is the default runtime for all development, CI/CD, and production workflows.
* **Deployment Mode:** **Rootless operation** is the **mandatory** deployment mode for all production and CI environments to minimize the attack surface.
* **Standard:** All container images will be written to **OCI standards** and validated using Podman. Compatibility with Docker Engine is not guaranteed and is not a priority over security or sovereignty features.

---

### Rationale
The decision adopts the **stricter** governance and **broader** architectural standard, driven by a balance of security architecture, standards compliance, and governance needs:

1.  **Security Architecture (Daemonless & Rootless):** Podman operates without a central, privileged daemon, with each container running as a child process of the invoking user. This **eliminates the "root daemon" attack surface** common in Docker and natively supports the mandatory requirement for **secure, non-root execution**. 
2.  **OCI Compliance & Standards:** Podman is fully compliant with **Open Container Initiative (OCI)** standards. Images built with Podman can theoretically run on any OCI-compliant runtime (Docker, containerd, Kubernetes), ensuring the project is not locked into a single tool or vendor.
3.  **Governance & Sovereignty:** Podman is developed under **open-source licenses** (Red Hat/Community) and can be fully operated without reliance on proprietary registries or centralized cloud services. This directly aligns with the project's **data sovereignty goals** and avoids vendor lock-in.
4.  **System Integration & Operations:** Podman integrates natively with **`systemd`**, allowing containers to be managed as standard system services. This is superior for the "set and forget" nature of a backup bot compared to Docker's daemon management.
5.  **Developer Experience:** The CLI is a drop-in replacement for the Docker CLI, minimizing the learning curve for contributors while still delivering superior security.

---

### Alternatives Considered
* **Docker Desktop:** While convenient for development, it relies on a **privileged root daemon** and is not suitable for production environments due to security and compliance concerns.
* **containerd:** A lightweight runtime suitable for Kubernetes, but it lacks the developer tooling required for easy local development and debugging.
* **Docker Engine:** The industry standard, but its reliance on a **privileged root daemon** creates a larger attack surface. While "Rootless Docker" exists, it's not the default and has usability limitations. Its ecosystem is also more centralized (Docker Hub), which is less aligned with sovereignty goals.
* **containerd:** A lower-level runtime excellent for Kubernetes but **lacks the high-level developer tooling (CLI)** required for easy local development and debugging.
* **systemd-nspawn:** Highly integrated with Linux/systemd but **lacks OCI compliance** and cross-platform (macOS/Windows) tooling.

---

### Consequences

#### **✅ Positive**
* **Security:** The default **rootless and daemonless** posture significantly reduces the attack surface and overall security risk.
* **Flexibility:** OCI compliance ensures portability, and open-source governance ensures users are not forced to use a specific vendor's registry or cloud.
* **Operations:** Native `systemd` integration provides robust service management for production deployments.

#### **❌ Negative**
* **Compatibility:** Some third-party tools hard-coded to look for the traditional `/var/run/docker.sock` may require manual configuration (e.g., configuring them to use `podman.sock`).
* **Cross-Platform:** On macOS and Windows, Podman requires a virtual machine (**Podman Machine**), which can be slightly more complex to manage than Docker Desktop for novice users.

#### **📝 Operational Mandates**
* All **CI/CD pipelines must use Podman** for all container builds and tests.
* **Developers must test on Podman** first; **"it works in Docker" is not a valid acceptance criterion.**
* The team will rely on the Podman CLI for development and operations, and all documentation must reflect Podman commands.

---

### Related ADRs
* ADR-003: Base Image Selection
* ADR-011: Deployment and Scalability Practices

---

