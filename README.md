# Log Parser

## Description
The Log Parser is a Python-based tool designed to analyze log files and generate a structured report in JSON format. It helps users extract meaningful insights from log data.

## Features
- Parse log files to extract entries.
- Generate a detailed report in JSON format.
- Easy-to-use and customizable.

## Prerequisites
- Python 3.8 or higher

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/beard91/log_parser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd log_parser
   ```

## Usage
1. Place your log file in the `log` directory and name it `sample_log.log`.
2. Run the script:
   ```bash
   python main.py
   ```
3. The generated report will be saved in the `report` directory (automatically generated) as `report.json`.

## Tests

The project includes a suite of tests to ensure the functionality of the log parser. Below is a description of the key test cases:

### Unit Tests

1. **Valid Log Line Parsing**:
   - Tests the ability to parse a correctly formatted log line.
   - Verifies that the timestamp, log level, and message are extracted correctly.

2. **Invalid Log Level**:
   - Tests the behavior when a log line contains an invalid log level.
   - Ensures that a `ValueError` is raised.

3. **Invalid Timestamp**:
   - Tests the behavior when a log line contains an invalid timestamp format.
   - Ensures that a `ValueError` is raised.

4. **Log File Parsing with Mixed Content**:
   - Tests the parsing of a log file containing valid lines, invalid lines, and empty lines.
   - Verifies that valid entries are processed and invalid entries are recorded.

5. **File Not Found**:
   - Tests the behavior when the specified log file does not exist.
   - Ensures that a `FileNotFoundError` is raised.

6. **Permission Denied**:
   - Tests the behavior when the log file cannot be read due to permission issues.
   - Ensures that a `PermissionError` is raised.

### Running Tests
To run the tests, use the following command:
```bash
pytest
```

## Directory Structure
```
log_parser/
├── main.py
├── pyproject.toml
├── README.md
├── src/
│   ├── log_analyzer/
│   │   ├── models.py
│   │   ├── parser.py
│   │   └── reporter.py
├── tests/
└── log/
    └── sample_log.log
```
