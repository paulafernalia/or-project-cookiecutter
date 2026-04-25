import logging
import logging.config
import yaml
from pathlib import Path

def setup_logging():
    """Configure logging using a YAML configuration file."""
    config_path = Path("conf/logging.yml")

    with config_path.open("r") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)