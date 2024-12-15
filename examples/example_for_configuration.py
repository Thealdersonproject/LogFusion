#whoami::./examples/example_for_configuration.py
"""This is an example for how to set YapLogger configurations."""
from yaplogger import Log


def main() -> None:
    """Configures a process with provided configurations.

    Allows customization of various attributes such as process UID, name, description, and additional metadata.

    Returns:
        None
    """
    # Create a custom configuration
    parameters = dict(
        process_uid="my-process-uid",
        process_name="My Process",
        process_description="This is my process.",
        process_extras={
            "version": "1.0.0",
            "environment": "development",
        },
    )

    log = Log(parameters=parameters).logger
    log.info("Hello from the other side. # INFO")
    log.debug("Hello from the other side. # DEBUG, This message should not appear.")
    log.warning("Hello from the other side. # WARNING")

    log.info("Straight out of loguru.")


if __name__ == "__main__":
    main()
