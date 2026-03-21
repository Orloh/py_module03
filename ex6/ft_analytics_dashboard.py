# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/21 20:36:26 by orhernan         #+#    #+#              #
#    Updated: 2026/03/21 22:51:17 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from typing import Any


def main() -> None:
    """
    Demo list, dict, and set comprehensions using hardcoded gaming data.
    """
    # Hardcoded sample data
    players: list[dict[str, Any]] = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "speed_demon"],
            "is_active": True,
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "collector"
            ],
            "is_active": True,
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["level_10", "treasure_hunter", "boss_slayer"],
            "is_active": True,
            "region": "east"
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["first_kill"],
            "is_active": False,
            "region": "central"
        }
    ]

    print("=== Game Analytics Dashboard ===\n")

    # --- List Comprehensions ---
    print("=== List Comprehension Examples ===")

    filter = 2000
    high_scorers: list[str] = [
        p["name"] for p in players if p["score"] > filter
    ]
    print(f"High scorers (>{filter}): {high_scorers}")

    scores_doubled: list[int] = [
        p["score"] * 2 for p in players
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [
        p["name"] for p in players if p["is_active"]
    ]
    print(f"Active players: {active_players}\n")

    # --- Dict Comprehensions ---
    print("=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {
        p["name"]: p["score"] for p in players if p["is_active"]
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([p for p in players if p["score"] > 2000 and p["is_active"]]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2000 and p["is_active"]]),
        "low": len([p for p in players if p["score"] < 1500 and p["is_active"]]),
    }
    score_categories = {k: v for k, v in score_categories.items() if v > 0}
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        p["name"]: len(p["achievements"]) for p in players if p["is_active"]
    }
    print(f"Achievement counts: {achievement_counts}\n")

    # --- Set Comprehensions ---
    print("=== Set Comprehension Examples ===")

    unique_players: set[str] = {
        p["name"] for p in players
    }
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {
        ach for p in players for ach in p["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}\n")

    active_regions: set[str] = {
        p["region"] for p in players
    }
    print(f"Active regions: {active_regions}\n")

    # --- Combined Analysis ---
    print("=== Combined Analysis ===")

    total_players: int = len(unique_players)
    print(f"Total players: {total_players}")

    print(f"Total unique achievements: {len(unique_achievements)}")

    avg_score: float = sum(player_scores.values()) / total_players if total_players > 0 else 0.0
    print(f"Average score: {avg_score}")

    max_score: int = max(player_scores.values()) if player_scores else 0
    top_performers: list[str] = [
        name for name, score in player_scores.items() if score == max_score
    ]

    if top_performers:
        top_name: str = top_performers[0]
        top_ach_count: int = achievement_counts.get(top_name, 0)
        print(f"Top performer: {top_name} ({max_score} points, {top_ach_count} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
