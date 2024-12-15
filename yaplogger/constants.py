# ./yaplogger/constants.py
"""This class holds all the constants for this project."""


class Constants:
    """Defines a set of constant keys and their default values used for describing a process.

    This class serves as a container for constant keys that represent specific attributes or
    descriptors of a process, such as its unique identifier, name, description, and any extra
    information. These constants can be used in applications to ensure consistency when referring
    to these properties. Additionally, default values are provided for each key, which can be used
    when actual values are not available.
    """

    # default keys
    PROCESS_UID_KEY: str = "process_uid"
    PROCESS_NAME_KEY: str = "process_name"
    PROCESS_DESCRIPTION_KEY: str = "process_description"
    PROCESS_EXTRAS_KEY: str = "process_extras"

    # default values
    PROCESS_UID_DEFAULT_VALUE: str = "<not_informed>"
    PROCESS_NAME_DEFAULT_VALUE: str = "<not_informed>"
    DESCRIPTION_DEFAULT_VALUE: str = "<not_informed>"
