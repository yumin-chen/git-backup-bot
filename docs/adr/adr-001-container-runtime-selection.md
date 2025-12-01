# ADR-001: Container Runtime Selection

## Status
Approved

## Context
We need to select a container runtime that meets our requirements for the automated backup system.

## Decision
After evaluating several options, we have selected Podman as the preferred container runtime for our project.

## Consequences
Using Podman allows us to maintain a daemonless container workflow which is beneficial for our backup system workflow.
