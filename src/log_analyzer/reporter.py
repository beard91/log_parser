from collections import Counter
from typing import List, Dict
from .models import LogEntry, ParseResult

def  generate_report(parse_result: ParseResult) -> Dict:
    valid_entries = parse_result.valid_entries
    invalid_entries = parse_result.invalid_entries
    level_counts = Counter(entry.level for entry in valid_entries)
    error_counts = Counter(entry.message for entry in valid_entries if entry.level == "ERROR")

    if valid_entries:
        start_time = str(min(entry.timestamp for entry in valid_entries))
        end_time = str(max(entry.timestamp for entry in valid_entries))
    else:
        start_time = None
        end_time = None

    return {
        "total_valid_entries": len(valid_entries),
        "total_invalid_entries": len(invalid_entries),
        "levels": dict(level_counts),
        "errors": dict(error_counts),
        "start_time": start_time,
        "end_time": end_time
    }