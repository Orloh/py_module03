# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/13 18:58:59 by orhernan         #+#    #+#              #
#    Updated: 2026/03/14 22:32:22 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'Hidden Path Finder', 'First Steps', 'Collector Supreme',
    'Untouchable', 'Sharp Mind', 'Boss Slayer', 'Lore Master',
    'Pacifist Run', 'Flawless Victory', 'Master Blacksmith',
    'Dragon Tamer', 'Night Owl', 'Gladiator', 'Shadow Assassin',
    'Millionaire', 'Godlike'
]


def gen_player_achievements() -> set[str]:
    num_achievements = random.randint(5, 10)
    chosen = random.sample(ALL_ACHIEVEMENTS, num_achievements)
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()

    all_distinct = set.union(*players.values())
    print(f"All distinct achievements: {all_distinct}")
    print()

    common_achievements = set.intersection(*players.values())
    print(f"Common achievements: {common_achievements}")
    print()

    for name, achievements in players.items():
        others_union: set = set()
        for other_name, other_achievements in players.items():
            if name != other_name:
                others_union = set.union(others_union, other_achievements)

        exclusive = set.difference(achievements, others_union)
        print(f"Only {name} has: {exclusive}")

    print()

    master_set = set(ALL_ACHIEVEMENTS)
    for name, achievements in players.items():
        missing = set.difference(master_set, achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
