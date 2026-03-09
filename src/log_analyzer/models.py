from dataclasses import dataclass
from datetime import datetime

# define a data class to represent a LogEntry
@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str

# define a data class to represent the result of parsing the log file, including valid and invalid entries
@dataclass
class ParseResult:
    valid_entries: list[LogEntry]
    invalid_entries: list[str]