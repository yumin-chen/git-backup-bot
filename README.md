# git-backup-bot

`git-backup-bot` is a production-grade automated backup system that continuously monitors local directories, commits changes to Git repositories with LFS support, and pushes updates to remote storage.

## Features

- **Automated Backups:** Monitors local directories for changes and automatically commits them to a Git repository.
- **Git LFS Support:** Handles large files efficiently using Git LFS.
- **Containerized:** Deploys as a containerized application using Podman.
- **Configurable:** Uses a simple YAML file for configuration.
- **Resilient:** Includes state persistence and crash recovery capabilities.
- **Secure:** Designed to run as a non-root user with credential isolation.
- **Extensible:** Modular architecture allows for future expansion.

## Getting Started

### Prerequisites

- Podman
- Git
- Git LFS

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/backup-bot.git
   cd backup-bot
   ```

2. Create your configuration file from the example:
   ```bash
   cp config/config.yaml.example config/config.yaml
   ```

3. Edit `config/config.yaml` to match your environment.

4. Build the container image:
   ```bash
   podman build -t backup-bot .
   ```

5. Run the container:
   ```bash
   podman run -d --name backup-bot \
     -v ./config:/usr/src/app/config \
     -v /path/to/your/data:/path/to/your/data \
     -v /path/to/ssh/keys:/root/.ssh:ro \
     backup-bot
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
