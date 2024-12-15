#whoami::./tests/test_config.py
"""Tests for the Config class."""
from yaplogger.config import Config
from yaplogger.constants import Constants


def test_default_configuration_initialization() -> None:
    """Test that default configuration is correctly initialized."""
    config = Config()
    assert config.parameters[Constants.PROCESS_UID_KEY] == Constants.PROCESS_UID_DEFAULT_VALUE
    assert config.parameters[Constants.PROCESS_NAME_KEY] == Constants.PROCESS_NAME_DEFAULT_VALUE
    assert config.parameters[Constants.PROCESS_DESCRIPTION_KEY] == Constants.DESCRIPTION_DEFAULT_VALUE
    assert config.parameters[Constants.PROCESS_EXTRAS_KEY] == []


def test_configure_with_custom_parameters() -> None:
    """Test that configuration updates correctly with custom parameters."""
    config = Config()
    custom_parameters = {
        Constants.PROCESS_UID_KEY: "custom_uid",
        Constants.PROCESS_NAME_KEY: "custom_name",
        Constants.PROCESS_DESCRIPTION_KEY: "custom_description",
    }
    updated_config = config.configure(parameters=custom_parameters)
    assert updated_config[Constants.PROCESS_UID_KEY] == "custom_uid"
    assert updated_config[Constants.PROCESS_NAME_KEY] == "custom_name"
    assert updated_config[Constants.PROCESS_DESCRIPTION_KEY] == "custom_description"


def test_configure_with_unrecognized_keys() -> None:
    """Test that unrecognized keys are added to extras."""
    config = Config()
    custom_parameters = {
        "unknown_key_1": "value1",
        "unknown_key_2": "value2",
    }
    updated_config = config.configure(parameters=custom_parameters)
    extras = updated_config[Constants.PROCESS_EXTRAS_KEY]
    assert {"unknown_key_1": "value1"} in extras
    assert {"unknown_key_2": "value2"} in extras


def test_get_process_id_default() -> None:
    """Test that the default process ID is returned if not set."""
    config = Config()
    process_id = config.get_process_id()
    assert process_id == Constants.PROCESS_UID_DEFAULT_VALUE


def test_get_process_id_after_configuration() -> None:
    """Test that process ID is correctly generated and retrieved after configuration."""
    config = Config()
    config.configure(parameters={})
    process_id = config.get_process_id()
    assert process_id != Constants.PROCESS_UID_DEFAULT_VALUE
    assert isinstance(process_id, str)
    assert len(process_id) > 0