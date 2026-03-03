from collections import Counter
from typing import List, Dict
from .models import LogEntry

def generate_report(entries: List[LogEntry]) -> Dict:
    level_counts = Counter(entry.level for entry in entries)
    
    return {
        "total_entries": len(entries),
        "levels": dict(level_counts),
    }