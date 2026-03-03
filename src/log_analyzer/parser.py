from datetime import datetime
from typing import List
from .models import LogEntry

# parse a single line of the log file into a LogEntry object
def parse_log_line(line: str) -> LogEntry:
    parts = line.strip().split(" | ")
    timestamp_str, level, message = parts
    
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    
    return LogEntry(
        timestamp=timestamp,
        level=level,
        message=message
    )

# parse the entire log file and return a list of LogEntry objects
def parse_log_file(file_path: str) -> List[LogEntry]:
    entries = []
    
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                entry = parse_log_line(line)
                entries.append(entry)
    
    return entries