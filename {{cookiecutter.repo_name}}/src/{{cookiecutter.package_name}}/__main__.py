import logging

from {{cookiecutter.package_name}}.conf import setup_logging

def main() -> None:
    """Run package directly."""
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("Logging is working!")


if __name__ == "__main__":
    main()
