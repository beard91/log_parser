from datetime import datetime
from log_analyzer.models import LogEntry, ParseResult
from log_analyzer.reporter import generate_report


def test_generate_report_counts_levels_and_errors():
    entries = [
        LogEntry("2026-03-01 10:15:23", "INFO", "Application started"),
        LogEntry("2026-03-01 10:15:30", "ERROR", "Database connection failed"),
        LogEntry("2026-03-01 10:16:05", "ERROR", "Database connection failed"),
    ]

    bad_entries = [
        LogEntry("2026-03-01 10:17:30", "ERR", "Database connection failed"),
        LogEntry("2026-03-01 10:18:00", "NOTOK", "Application started"),
    ]
    result = ParseResult(valid_entries=entries, invalid_entries=bad_entries)

    report = generate_report(result)

    assert report["total_valid_entries"] == 3
    assert report["total_invalid_entries"] == 2
    assert report["levels"]["ERROR"] == 2
    assert report["levels"]["INFO"] == 1
    assert report["errors"]["Database connection failed"] == 2
    assert report["start_time"] == "2026-03-01 10:15:23"
    assert report["end_time"] == "2026-03-01 10:16:05"