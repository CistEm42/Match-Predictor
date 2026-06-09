"""
Validation functions for football match data.
"""

import pandas as pd

from schema import (
    REQUIRED_COLUMNS,
    VALID_RESULTS,
    NON_NEGATIVE_COLUMNS
)


def check_required_columns(data: pd.DataFrame):
    """
    Verify required columns exist.
    """

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in data.columns
    ]

    return missing_columns


def check_duplicate_rows(data: pd.DataFrame):
    """
    Check duplicate records.
    """

    return int(data.duplicated().sum())


def check_duplicate_matches(data: pd.DataFrame):
    """
    Check duplicate football matches.
    """

    duplicate_matches = data.duplicated(
        subset=["Date", "HomeTeam", "AwayTeam"]
    )

    return int(duplicate_matches.sum())


def check_invalid_dates(data: pd.DataFrame):
    """
    Check date conversion issues.
    """

    # dates = pd.to_datetime(
    #     data["Date"],
    #     dayfirst=True,
    #     errors="coerce"
    # )

    return (data['Date'].isna().sum())


def check_same_team_matches(data: pd.DataFrame):
    """
    Home team cannot equal away team.
    """

    invalid = (
        data["HomeTeam"].str.strip().str.lower()
        ==
        data["AwayTeam"].str.strip().str.lower()
    )

    return int(invalid.sum())


def check_negative_values(data: pd.DataFrame):
    """
    Check negative values in numeric stats.
    """

    results = {}

    for column in NON_NEGATIVE_COLUMNS:

        if column in data.columns:

            count = int((data[column] < 0).sum())

            results[column] = count

    return results


def check_invalid_results(data: pd.DataFrame):
    """
    Check FTR contains only H, D, A.
    """

    invalid = ~data["FTR"].isin(VALID_RESULTS)

    return int(invalid.sum())


def check_result_consistency(data: pd.DataFrame):
    """
    Validate result matches goals.
    """

    inconsistencies = 0

    for _, row in data.iterrows():

        home_goals = row["FTHG"]
        away_goals = row["FTAG"]
        result = row["FTR"]

        expected_result = None

        if home_goals > away_goals:
            expected_result = "H"

        elif home_goals < away_goals:
            expected_result = "A"

        else:
            expected_result = "D"

        if result != expected_result:
            inconsistencies += 1

    return inconsistencies


def check_missing_values(data: pd.DataFrame):
    """
    Missing values by column.
    """

    return data.isnull().sum().sort_values(
        ascending=False
    )

def get_team_names(data: pd.DataFrame):
    """
    Unique team names.
    Useful for spotting inconsistencies.
    """

    home_teams = set(data["HomeTeam"].unique())
    away_teams = set(data["AwayTeam"].unique())

    return sorted(home_teams.union(away_teams))
