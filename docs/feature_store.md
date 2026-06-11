# Football Match Intelligence Platform - Feature Store Design

┌─────────────────────────────────────────────────────────────┐
│                      Feature Store                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Offline      │  │  Online      │  │  Batch       │      │
│  │  Feature      │  │  Serving     │  │  Pipeline    │      │
│  │  Store        │  │  Layer       │  │  (Daily)     │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                 │               │
│         └─────────────────┼─────────────────┘               │
│                           │                                 │
│                    ┌──────▼───────┐                         │
│                    │  Feature     │                         │
│                    │  Registry    │                         │
│                    └──────────────┘                         │
└─────────────────────────────────────────────────────────────┘

 Team Performance Features (Primary Key: Team + Season)
Feature Name	        Description	                               Data Type	Derived From
team_goals_avg	        Average goals per match (home+away)	            Float	        FTHG + FTAG
team_over_2.5_pct 	    % matches with over 2.5 goals	                Float	        TotalGoals > 2.5
team_corners_avg	    Average corners per match	                    Float	        HC + AC
team_over10.5_corners_pct	% matches with >10.5 corners            Float	        TotalCorners > 10.5
team_fouls_avg	        Average fouls per match	                        Float	        HF + AF
team_yellow_avg	        Average yellow cards per match	                Float	        HY + AY
team_red_avg	        Average red cards per match	                    Float	        HR + AR
team_shots_avg	        Average total shots per match	                Float	        HS + AS
team_shots_on_target_avg	    Average shots on target per match	    Float	        HST + AST

Home/Away Differential Features
Feature Name	        Description	                                    Data Type
home_advantage_corners	Home corners - Away corners (team-specific)	    Float
home_advantage_fouls	Home fouls - Away fouls (team-specific)	        Float
home_advantage_goals	Home goals - Away goals (team-specific)	        Float

Match Context Features
Feature Name	    Description	             Data Type	            Values
season	            Season identifier	    Categorical	        2022/2023, 2023/2024, 2024/2025, 2025/2026
is_home	            Home/Away indicator	        Binary	                   0/1
goal_category	  Goal range classification	    Categorical	            0-2, 3-4, 5+
corner_category	   Corner range classification	Categorical	    Under10.5, Over10.5

Aggression Index Features
Feature Name	        Description	                        Formula
aggression_score	Normalized foul + card metric	        MinMaxScaler(team_fouls_avg)
disciplinary_risk	Combined yellow/red card metric	        (HY+AY) + 3*(HR+AR)

## Objective

The feature store contains reusable features that can be used across:

* Match Outcome Prediction
* Over 2.5 Goals Prediction
* Corner Prediction
* Team Analytics

---

# Team Form Features

## home_form_5

Description:

Points earned by home team in previous 5 matches.

Formula:

(3 × Wins) + (1 × Draws)

Window:

Previous 5 matches.

---

## away_form_5

Points earned by away team in previous 5 matches.

---

## home_win_rate_10

Win percentage in previous 10 matches.

---

## away_win_rate_10

Win percentage in previous 10 matches.

---

# Goal Features

## home_avg_goals_5

Average goals scored in previous 5 matches.

---

## away_avg_goals_5

Average goals scored in previous 5 matches.

---

## home_avg_goals_conceded_5

Average goals conceded in previous 5 matches.

---

## away_avg_goals_conceded_5

Average goals conceded in previous 5 matches.

---

## goal_difference_form

Difference between team scoring and conceding rates.

---

# Shots Features

## home_avg_shots_5

Average shots in previous 5 matches.

---

## away_avg_shots_5

Average shots in previous 5 matches.

---

## home_avg_shots_on_target_5

Average shots on target in previous 5 matches.

---

## away_avg_shots_on_target_5

Average shots on target in previous 5 matches.

---

## shot_conversion_rate

Goals scored divided by shots on target.

---

# Corner Features

## home_avg_corners_5

Average corners won in previous 5 matches.

---

## away_avg_corners_5

Average corners won in previous 5 matches.

---

## home_corner_advantage

Difference between home and away corner averages.

---

## corner_difference

Home corners minus away corners.

---

# Discipline Features

## home_avg_fouls_5

Average fouls committed in previous 5 matches.

---

## away_avg_fouls_5

Average fouls committed in previous 5 matches.

---

## team_aggression_score

Normalized foul rate.

Range:

0 to 1

---

## yellow_card_rate

Average yellow cards per match.

---

# Head-to-Head Features

## h2h_home_wins

Historical home wins between teams.

---

## h2h_away_wins

Historical away wins between teams.

---

## h2h_goal_difference

Average goal difference in head-to-head meetings.

---

# League Context Features

## season_goal_rate

Average league goals during season.

---

## season_corner_rate

Average league corners during season.

---

## league_scoring_trend

League-wide scoring trend.

---

# Target Variables

## Match Outcome

Target:

FTR

Classes:

* H
* D
* A

---

## Over 2.5 Goals

Target:

Over2.5

Classes:

* 0
* 1

---

## Total Goals

Regression Target

TotalGoals

---

## Total Corners

Regression Target

TotalCorners
