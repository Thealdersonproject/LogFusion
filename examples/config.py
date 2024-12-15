#./examples/config.py  # noqa: INP001
"""This is an example for how to set YapLogger configurations."""
from yaplogger.config import Config


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

    Config.configure(parameters=parameters)


if __name__ == "__main__":
    main()
