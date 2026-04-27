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
    num_achievements = random.randint(7, 20)
    chosen = random.sample(ALL_ACHIEVEMENTS, num_achievements)
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice: tuple[str, set[str]] = ("Alice", gen_player_achievements())
    bob: tuple[str, set[str]] = ("Bob", gen_player_achievements())
    charlie: tuple[str, set[str]] = ("Charlie", gen_player_achievements())
    diana: tuple[str, set[str]] = ("Diana", gen_player_achievements())

    players: list[tuple[str, set[str]]] = [alice, bob, charlie, diana]

    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    print()

    all_distinct: set[str] = set()
    common_achievements: set[str] = set(ALL_ACHIEVEMENTS)

    for _, achievements in players:
        all_distinct = all_distinct.union(achievements)
        common_achievements = common_achievements.intersection(achievements)

    print(f"All distinct achievements: {all_distinct}")
    print()

    print(f"Common achievements: {common_achievements}")
    print()

    for name, achievements in players:
        others_union: set[str] = set()
        for other_name, other_achievements in players:
            if name != other_name:
                others_union = set.union(others_union, other_achievements)

        exclusive: set[str] = set.difference(achievements, others_union)
        print(f"Only {name} has: {exclusive}")

    print()

    master_set: set[str] = set(ALL_ACHIEVEMENTS)
    for name, achievements in players:
        missing: set[str] = set.difference(master_set, achievements)
        print(f"{name} is missing: {missing}")
        print()


if __name__ == "__main__":
    main()
