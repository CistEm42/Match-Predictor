"""
Runs all validation checks on the football dataset.
"""

from pathlib import Path
import pandas as pd
from datetime import datetime

from validators import (
    check_required_columns,
    check_duplicate_rows,
    check_duplicate_matches,
    check_invalid_dates,
    check_same_team_matches,
    check_negative_values,
    check_invalid_results,
    check_result_consistency,
    check_missing_values,
    get_team_names
)

# --------------------------------------------------
# Paths
# --------------------------------------------------

DATA_PATH = Path("data/processed/cleaned.csv")

REPORT_DIR = Path("data/validation_reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = REPORT_DIR / "validation_report.txt"


# --------------------------------------------------
# Validation Runner
# --------------------------------------------------

def run_validation():

    print("\nLoading dataset...")

    data = pd.read_csv(DATA_PATH)

    report_lines = []

    report_lines.append("=" * 60)
    report_lines.append("FOOTBALL DATA VALIDATION REPORT")
    report_lines.append("=" * 60)
    report_lines.append(
        f"Generated: {datetime.now()}"
    )
    report_lines.append("")

    # ----------------------------------------
    # Required Columns
    # ----------------------------------------

    missing_columns = check_required_columns(data)

    report_lines.append(
        f"Missing Columns: {len(missing_columns)}"
    )

    if missing_columns:
        report_lines.append(
            f"Missing -> {missing_columns}"
        )

    # ----------------------------------------
    # Duplicates
    # ----------------------------------------

    duplicate_rows = check_duplicate_rows(data)

    report_lines.append(
        f"Duplicate Rows: {duplicate_rows}"
    )

    duplicate_matches = check_duplicate_matches(data)

    report_lines.append(
        f"Duplicate Matches: {duplicate_matches}"
    )

    # ----------------------------------------
    # Dates
    # ----------------------------------------

    invalid_dates = check_invalid_dates(data)

    report_lines.append(
        f"Invalid Dates: {invalid_dates}"
    )

    # ----------------------------------------
    # Teams
    # ----------------------------------------

    same_team_matches = check_same_team_matches(data)

    report_lines.append(
        f"Same Team Fixtures: {same_team_matches}"
    )

    # ----------------------------------------
    # Results
    # ----------------------------------------

    invalid_results = check_invalid_results(data)

    report_lines.append(
        f"Invalid Results: {invalid_results}"
    )

    inconsistencies = check_result_consistency(data)

    report_lines.append(
        f"Result Inconsistencies: {inconsistencies}"
    )

    # ----------------------------------------
    # Negative Values
    # ----------------------------------------

    report_lines.append("")
    report_lines.append("NEGATIVE VALUE CHECKS")

    negative_results = check_negative_values(data)

    for column, count in negative_results.items():

        report_lines.append(
            f"{column}: {count}"
        )

    # ----------------------------------------
    # Missing Values
    # ----------------------------------------

    report_lines.append("")
    report_lines.append("MISSING VALUES")

    missing_values = check_missing_values(data)

    for column, count in missing_values.items():

        if count > 0:

            report_lines.append(
                f"{column}: {count}"
            )

    # ----------------------------------------
    # Team Summary
    # ----------------------------------------

    report_lines.append("")
    report_lines.append("TEAM SUMMARY")

    teams = get_team_names(data)

    report_lines.append(
        f"Total Teams: {len(teams)}"
    )

    # ----------------------------------------
    # Dataset Summary
    # ----------------------------------------

    report_lines.append("")
    report_lines.append("DATASET SUMMARY")

    report_lines.append(
        f"Rows: {data.shape[0]}"
    )

    report_lines.append(
        f"Columns: {data.shape[1]}"
    )

    # ----------------------------------------
    # Validation Status
    # ----------------------------------------

    critical_errors = (
        len(missing_columns)
        + duplicate_matches
        + invalid_dates
        + same_team_matches
        + invalid_results
        + inconsistencies
    )

    report_lines.append("")
    report_lines.append("=" * 60)

    if critical_errors == 0:

        report_lines.append(
            "VALIDATION STATUS: PASSED"
        )

    else:

        report_lines.append(
            "VALIDATION STATUS: FAILED"
        )

    report_lines.append("=" * 60)

    # ----------------------------------------
    # Save Report
    # ----------------------------------------

    with open(REPORT_PATH, "w") as f:

        for line in report_lines:

            f.write(str(line) + "\n")

    print("\nValidation complete.")
    print(f"Report saved to: {REPORT_PATH}")
    print(data["Date"].isna().sum())
    print(data["Date"].min())
    print(data["Date"].max())

    return report_lines


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    run_validation()