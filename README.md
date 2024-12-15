Here is a sample `README.md` file for the YapLogger project:

**YapLogger**
================

**Description**
-----------

YapLogger is a centralized logging solution for projects with multiple steps and workflows. It facilitates tracing by identifying processes throughout their execution using a unique execution ID. Logging during the process should help the engineering team debug issues. Additionally, it is crucial for ensuring business outcomes by analyzing system behavior.

**Features**
-----------

* **Centralized logging**: YapLogger provides a single point of truth for logging across multiple processes and workflows.
* **Unique execution ID**: Each process is assigned a unique ID to facilitate tracing and debugging.
* **Configurable logging**: YapLogger allows for customization of logging levels, formats, and sinks.
* **Terminal sink**: Log messages can be output to the terminal for easy debugging.

**Getting Started**
---------------

### Installation

To install YapLogger, run the following command:

```
pip install yaplogger
```

### Usage

To use YapLogger, simply import the `YapLogger` class and initialize it with the required parameters:
```python
from yaplogger import YapLogger

logger = YapLogger(process_name="My Process", description="This is a sample process")
logger.info("This is an info message")
```

### Configuration

YapLogger can be configured to use different logging levels, formats, and sinks. For more information, see the [Configuration](#configuration) section.

**Configuration**
---------------

### Logging Levels

YapLogger supports the following logging levels:

* **Trace**: 5
* **Debug**: 10
* **Info**: 20
* **Success**: 25
* **Warning**: 30
* **Error**: 40
* **Critical**: 50

### Logging Formats

YapLogger supports the following logging formats:

* **YYYY-MM-DD HH24:MI:SS.ZZZ**: Default format for log messages

### Sinks

YapLogger supports the following sinks:

* **Terminal**: Output log messages to the terminal

**Contributing**
------------

Contributions to YapLogger are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

**License**
-------

YapLogger is licensed under the [MIT License](LICENSE).

**Authors**
---------

* Thiago Dias - [thiago@thir.info](mailto:thiago@thir.info)

