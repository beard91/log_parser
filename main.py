import json
import logging
from src.log_analyzer.parser import parse_log_file
from src.log_analyzer.reporter import generate_report
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting log analysis")

    file_path = "log\\sample_log.log"
    entries = parse_log_file(file_path)

    # path where the report will be saved, using os.path.join for cross-platform compatibility
    report_dir = os.path.join(os.getcwd(), "report")

    # create the report directory if it doesn't exist, exist_ok=True prevents an error if the directory already exists
    os.makedirs(report_dir, exist_ok=True)

    report = generate_report(entries)

    # save the report to a JSON file, 'with' is used to safely close the file after writing
    with open(os.path.join(report_dir, "report.json"), "w") as f:
        # json.dump is used to convert a Python object to a JSON format, with indentation for readability
        json.dump(report, f, indent=4)

    logger.info("Report generated successfully")

if __name__ == "__main__":
    main()
