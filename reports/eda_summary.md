# Football Match Intelligence Platform - Exploratory Data Analysis Summary

## Dataset Overview

The dataset consists of English Premier League matches across multiple seasons:

* 2022/23
* 2023/24
* 2024/25
* 2025/26

The objective is to identify patterns that can be transformed into predictive features for machine learning models.

---

# Match Outcome Analysis

Match outcomes were analyzed using the Full Time Result (FTR) variable.

Key findings:

* Home wins occur more frequently than away wins.
* Draws are the least common outcome.
* Home advantage exists across all seasons.

Home wins dominate: 44.47% of matches end in home victories

Away wins: 31.45% of matches

Draws: 24.08% of matches

Over four seasons, home advantage remains significant but has shown slight variation

Implication:

Home advantage should be incorporated into future feature engineering.

Potential Features:

* home_advantage_score
* home_win_rate
* away_win_rate

---

# Goal Analysis
Season	Avg Goals/Match	Over 2.5 %
2022/2023	2.85	52.63%
2023/2024	3.28	64.74%
2024/2025	2.93	56.58%
2025/2026	2.75	55.00%

Key Insights:

2023/2024 stands out with highest average goals (3.28) and over 2.5 percentage (64.74%)

Goal distribution is right-skewed; most matches have 2-4 goals

Peak goal-scoring matches: Liverpool 9-0 Bournemouth, Sheffield United 0-8 Newcastle

Linear regression shows a negative but not statistically significant trend (slope: -0.065, p-value: 0.633)

Top Teams by Average Goals (Home + Away):

Sheffield United: 3.66

Luton: 3.61

Tottenham: 3.30

Liverpool: 3.24

Man City: 3.19



## Goal Distribution

Total goals were calculated as:

TotalGoals = FTHG + FTAG

Key findings:

* Most matches contain between 1 and 4 goals.
* Average goals per match are relatively stable across seasons.
* High-scoring matches are common.

## Over 2.5 Goals Analysis

A binary target was created:

Over2.5 = 1 if TotalGoals > 2

Key findings:

* More than half of matches exceed 2.5 goals.
* The 2023/24 season produced the highest percentage of Over 2.5 matches.

Implication:

Over 2.5 Goals is a suitable classification target.

Potential Features:

* team_goal_rate
* recent_goal_form
* attack_strength
* defensive_strength

---

# Seasonal Goal Trends

Goals per season were analyzed.

Key findings:

* Goal scoring peaked during the 2023/24 season.
* Goal production declined slightly afterward.
* Linear regression showed a weak negative trend.
* The trend was not statistically significant.

Implication:

Season-level scoring trends may still provide useful context.

Potential Features:

* season_goal_rate
* league_scoring_trend

---

# Corner Analysis

TotalCorners = HC + AC

Seasonal Corner Trends:

Season	Avg Corners/Match
2022/2023	10.11
2023/2024	10.84
2024/2025	10.30
2025/2026	10.00

Home vs Away Corner Advantage:

Home corners average: 5.65 per match

Away corners average: 4.66 per match

Difference: +0.99 corners advantage for home teams

p-value: 1.76e-19 → statistically significant

Top Teams by Total Corners Won:

- Man City: 1,022 corners

- Liverpool: 1,008 corners

- Arsenal: 946 corners

Top Teams by Over 10.5 Corners %:

- Arsenal: 10.53%

- Aston Villa: 7.24%

- Chelsea: 7.24%

## High-Corner Teams

Several teams consistently generated more corners than others.

Implication:

Corner generation appears to be a team characteristic.

## Home Corner Advantage

Key findings:

* Home teams earn more corners than away teams.
* Difference is statistically significant.

Implication:

Home corner advantage should be considered during feature engineering.

Potential Features:

* home_avg_corners_5
* away_avg_corners_5
* home_corner_advantage
* corner_difference

---

# Fouls Analysis

TotalFouls = HF + AF

Home vs Away Fouls:

Home fouls average: 10.70 per match

Away fouls average: 11.14 per match

p-value: 0.00046 → statistically significant

Top Teams by Total Fouls Committed:

- Wolves: 1,914 fouls

- Bournemouth: 1,868 fouls

- Tottenham: 1,757 fouls

Top Teams by Average Fouls/Match:

- Wolves: 12.59

- Bournemouth: 12.29

- Southampton: 11.70

Key findings:

* Certain teams consistently commit more fouls.
* Away teams commit slightly more fouls than home teams.
* Difference is statistically significant.

Implication:

Discipline-related features may contain predictive information.

Potential Features:

* team_aggression_score
* home_avg_fouls_5
* away_avg_fouls_5
* foul_difference

---

# Correlation Analysis
Strong Correlations:

HST ↔ FTHG: 0.58 (moderate positive)

AST ↔ FTAG: 0.58 (moderate positive)

HS ↔ HST: 0.69 (strong positive)

AS ↔ AST: 0.67 (strong positive)

Weak Correlations:

HC ↔ FTHG: 0.06 (very weak)

AC ↔ FTAG: 0.06 (very weak)

HF ↔ HY: 0.34 (weak positive)

AF ↔ AY: 0.38 (weak positive)

Fouls ↔ Red Cards: ~0.06 (very weak)

Key Insight: Shots on target have a moderate correlation with goals, while corners show almost no correlation. This suggests that shot quality (on-target attempts) is a much better predictor of scoring than set-piece volume.

## Shots vs Goals

Key findings:

* Total shots show weak correlation with goals.
* Shots on target show moderate correlation with goals.

Implication:

Shots on target are stronger predictors than total shots.

Potential Features:

* recent_shots_on_target
* shots_on_target_ratio
* attacking_efficiency

---

## Corners vs Goals

Key findings:

* Corners have very weak correlation with goals.

Implication:

Corners alone are unlikely to be strong predictors of scoring.

Potential Features:

* corner_form
* corner_difference

---

## Fouls vs Cards

Key findings:

* Weak positive relationship between fouls and yellow cards.
* Very weak relationship between fouls and red cards.

Implication:

Discipline metrics may contribute to specialized prediction tasks.

Potential Features:

* yellow_card_rate
* discipline_score

---

# Newly Engineered Variables Created During EDA

* TotalGoals
* TotalCorners
* TotalFouls
* TotalYellowCards
* TotalShotsOnTarget
* Over2.5

---

# Main Conclusions

The strongest predictive signals discovered during EDA include:

1. Home advantage
2. Team attacking strength
3. Recent goal-scoring form
4. Shots on target
5. Team discipline patterns
6. Team corner generation tendencies

Home advantage is real and significant for both corners and fouls, though away teams commit slightly more fouls.

2023/2024 was an outlier season with unusually high goal-scoring (3.28 avg vs 2.85-2.93 in other seasons).

Shots on target are the best predictor of goals among available statistics.

Corners have minimal predictive value for goal-scoring outcomes.

Fouls moderately correlate with yellow cards but show virtually no relationship with red cards.

Teams like Wolves, Bournemouth, and Tottenham consistently rank high in physical/aggressive metrics (fouls).

These findings will guide feature engineering and model development.
