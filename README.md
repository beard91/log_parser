Simple log parser

Insert in \log folder the log file with name "sample_log.log" with a format like below:
    2025-03-01 10:15:23 | INFO | Application started
    2025-03-01 10:15:25 | WARNING | Slow response detected
    2025-03-01 10:15:30 | ERROR | Database connection failed
    2025-03-01 10:16:00 | INFO | Retrying connection
    2025-03-01 10:16:05 | ERROR | Retry failed


In \report folder (which is created authomatically if doesn't exist) the JSON output report with following information:
    - number of entries (=lines/events)
    - how many log levels are present for each level (INFO, WARNING, ERROR)

Below the JSON output report format:
    {
        "total_entries": 5,
        "levels": {
            "INFO": 2,
            "WARNING": 1,
            "ERROR": 2
        }
    }



Execute it with command : python -m main


Tests in \tests folder are still ongoing and not completed
    