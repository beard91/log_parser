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
   git clone https://github.com/your-repo/log_parser.git
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
3. The generated report will be saved in the `report` directory as `report.json`.

## Tests
Tests are still ongoing and not completed

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
