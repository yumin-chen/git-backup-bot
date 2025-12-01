import yaml
import logging
import os

CONFIG_PATH = "/usr/src/app/config/config.yaml"

def main():
    """
    Main function for the BackupBot.
    Loads configuration, sets up logging, and prints a startup message.
    """
    print("--- BackupBot Starting ---")

    # Load configuration
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)
        print(f"Successfully loaded configuration from {CONFIG_PATH}")
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found at {CONFIG_PATH}. Make sure to mount it correctly.")
        return
    except yaml.YAMLError as e:
        print(f"ERROR: Failed to parse configuration file: {e}")
        return

    # Set up logging
    log_config = config.get('logging', {})
    log_file = log_config.get('file_path', '/usr/src/app/logs/backup.log')
    log_level = log_config.get('level', 'INFO').upper()

    # Ensure log directory exists (though the Containerfile should create it)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.info("BackupBot application started successfully.")
    logging.info("This is a test log message to verify write permissions.")

    # In the future, the application's main loop would start here.
    print("\nApplication finished its current task and will now exit.")


if __name__ == "__main__":
    main()
