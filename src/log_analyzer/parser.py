from datetime import datetime
from .models import LogEntry, ParseResult

LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

# parse a single line of the log file into a LogEntry object
def parse_log_line(line: str) -> LogEntry:
    parts = line.strip().split(" | ")
    timestamp_str, level, message = parts

# validate the timestamp and log level, and create a LogEntry object  
    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"Invalid timestamp format in line: {line}")
    
    if level not in LOG_LEVELS:
        raise ValueError(f"Invalid log level in line: {line}")

    return LogEntry(
        timestamp=timestamp,
        level=level,
        message=message
    )

# parse the entire log file and return a list of LogEntry objects
def parse_log_file(file_path: str) -> ParseResult:
    valid_entries : list[LogEntry] = []
    invalid_entries : list[str] = []

    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                try:
                    entry = parse_log_line(line)
                    valid_entries.append(entry)
                except ValueError:
                    invalid_entries.append(line)
            else:
                continue
    return ParseResult(
        valid_entries=valid_entries,
        invalid_entries=invalid_entries
    )