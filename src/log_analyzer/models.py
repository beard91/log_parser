from dataclasses import dataclass
from datetime import datetime

# define a data class to represent a LogEntry
@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str