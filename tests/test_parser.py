from log_analyzer.parser import parse_log_line, parse_log_file
import pytest


def test_parse_valid_log_line():
    line = "2026-03-01 10:15:23 | INFO | Application started"
    entry = parse_log_line(line)

    assert entry.level == "INFO"
    assert entry.message == "Application started"
    assert entry.timestamp.strftime("%Y-%m-%d %H:%M:%S") == "2026-03-01 10:15:23"


def test_parse_invalid_level():
    line = "2026-03-01 10:15:23 | INF | Wrong level"

    try:
        parse_log_line(line)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_parse_invalid_timestamp():
    line = "not-a-date | INFO | Hello"

    try:
        parse_log_line(line)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_parse_log_file_with_invalid_lines(tmp_path):
    content = "\n".join(
        [
            "2026-03-01 10:15:23 | INFO | Application started",
            "invalid line",
            "2026-03-01 10:15:30 | ERROR | Database connection failed",
            "",
            "2026-03-01 10:15:30 | ERROR",
        ]
    )

    log_file = tmp_path / "sample.log"
    log_file.write_text(content, encoding="utf-8")

    result = parse_log_file(str(log_file))

    assert len(result.valid_entries) == 2
    assert len(result.invalid_entries) == 2

def test_parse_log_file_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_log_file("non_existent_file.log")

def test_parse_log_file_invalid_path():
    with pytest.raises(OSError):
        parse_log_file("invalid_path/<>.log")