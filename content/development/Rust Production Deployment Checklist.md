---
title: Rust Production Deployment Checklist
tags:
  - rust
  - deployment
  - devops
  - docker
---

Notes from [Deploying Rust to production checklist](https://kerkour.com/rust-production-checklist) by Sylvain Kerkour.

## Key Takeaways

- **Compilation profiles matter**: debug builds compile fast but run 10–50x slower than release builds. Always use `--release` for production, which enables level-3 optimizations, aggressive inlining, and strips debug assertions
- **Docker multi-stage builds**: compile in a full Rust environment, then copy only the final binary to a minimal image (e.g. `scratch` or `distroless`). This minimizes attack surface and image size
- **Static linking with musl**: target `x86_64-unknown-linux-musl` to produce fully static binaries with no runtime dependencies
- **Run as non-root**: follow least-privilege principles in containers (e.g. UID 1000)
- **Structured logging & tracing**: use the `tracing` crate for structured, async-aware observability. Include request/correlation IDs and instance metadata for multi-node deployments
- **Dependency caching in CI/CD**: leverage Docker layer caching and tools like `cargo-chef` to speed up builds, since optimized Rust compilation can take 15–20 minutes on medium projects
- **Minimal container contents**: ship only the binary and CA certificates — no shell, no package manager
