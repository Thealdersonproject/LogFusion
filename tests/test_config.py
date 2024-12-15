import pytest
from yaplogger.config import Config
from yaplogger.constants import Constants


def test_default_configuration() -> None:
    """Tests that the default configuration of the Config class is correctly initialized with its default values.

    Verifies that the process ID, process name, process description, and process extras match
    the defined default constants.

    Returns:
        None: This function does not return any value.
    """
    config = Config()
    assert config.get_process_id() == Constants.PROCESS_UID_DEFAULT_VALUE
    assert config.get_configuration()[Constants.PROCESS_NAME_KEY] == Constants.PROCESS_NAME_DEFAULT_VALUE
    assert config.get_configuration()[Constants.PROCESS_DESCRIPTION_KEY] == Constants.DESCRIPTION_DEFAULT_VALUE
    assert config.get_configuration()[Constants.PROCESS_EXTRAS_KEY] == []

def test_custom_configuration() -> None:
    """Test customization of configuration in the Config object.

    This test ensures that the configuration object is properly customized
    with the provided details, and the configured values can be retrieved
    and validated. The function invokes the `configure` method with a custom
    configuration dictionary and verifies the customization through assertions.

    Raises:
        AssertionError: If any of the assertions fail when validating the configured details.
    """
    Config().configure(
        parameters={
            "process_uid": "custom_uid",
            "process_name": "custom_name",
            "process_description": "custom_description",
            "process_extras": [{"key1": "value1"}, {"key2": "value2"}],
        }
    )
    assert Config.get_process_id() == "custom_uid"
    assert Config.get_configuration()[Constants.PROCESS_NAME_KEY] == "custom_name"
    assert Config.get_configuration()[Constants.PROCESS_DESCRIPTION_KEY] == "custom_description"
    assert Config.get_configuration()[Constants.PROCESS_EXTRAS_KEY] == [{"key1": "value1"}, {"key2": "value2"}]

def test_missing_configuration() -> None:
    """Test function to verify the behavior when certain configuration keys are missing during the setup.

    It ensures that the Config object assigns the default where specified and returns
    the expected process ID and configuration values.

    Arguments:
        None

    Returns:
        None
    """
    Config().configure(parameters={"process_uid": "custom_uid"})
    assert Config.get_process_id() == "custom_uid"
    assert Config.get_configuration()[Constants.PROCESS_NAME_KEY] == Constants.PROCESS_NAME_DEFAULT_VALUE
    assert Config.get_configuration()[Constants.PROCESS_DESCRIPTION_KEY] == Constants.DESCRIPTION_DEFAULT_VALUE
    assert Config.get_configuration()[Constants.PROCESS_EXTRAS_KEY] == []

def test_invalid_configuration() -> None:
    """Tests for invalid configuration scenarios in the Config class to ensure proper error handling.

    Raises:
    ------
    ValueError
        If the provided configuration contains invalid values, such as a non-string `process_uid`
        or a `process_extras` that is not a list.
    KeyError
        If the configuration contains unrecognized keys that are not supported.
    """
    with pytest.raises(ValueError):  # noqa: PT011
        Config().configure(parameters={"process_uid": 123})

    with pytest.raises(ValueError):  # noqa: PT011
        Config().configure(parameters={"process_extras": "not a list"})

    with pytest.raises(KeyError):
        Config().configure(parameters={"invalid_key": "value"})
