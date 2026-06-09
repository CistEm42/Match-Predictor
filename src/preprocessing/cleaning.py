def remove_high_missing_columns(df, threshold=0.3):
    missing_ratio = df.isna().mean()
    df = df.dropna(subset=[
        "Date",
        "HomeTeam",
        "AwayTeam",
        "FTHG",
        "FTAG"
    ])

    # 3. Fill remaining small gaps
    df = df.fillna(0)

    cols_to_drop = missing_ratio[missing_ratio > threshold].index

    return df.drop(columns=cols_to_drop)