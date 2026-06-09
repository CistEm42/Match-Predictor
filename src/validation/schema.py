"""
Defines the expected structure of the football dataset.
"""

# Required columns for Version 1
REQUIRED_COLUMNS = [
    "Date",
    "HomeTeam",
    "AwayTeam",
    "FTHG",
    "FTAG",
    "FTR",
]

# Expected data types
EXPECTED_DTYPES = {
    "Date": "datetime64[ns]",
    "HomeTeam": "object",
    "AwayTeam": "object",
    "FTHG": "int64",
    "FTAG": "int64",
    "FTR": "object",
}

# Valid match outcomes
VALID_RESULTS = ["H", "D", "A"]

# Numeric columns that should never be negative
NON_NEGATIVE_COLUMNS = [
    "FTHG",
    "FTAG",
    "HS",
    "AS",
    "HST",
    "AST",
    "HC",
    "AC",
    "HF",
    "AF",
    "HY",
    "AY",
    "HR",
    "AR",
]