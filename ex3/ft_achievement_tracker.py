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


class Player:
    """Represents a game character with a set of achievements."""
    def __init__(self, name: str, achievements: set[str]) -> None:
        """Initializes the Player with capitalized name and achievements."""
        self.__name = name.capitalize()
        self.__achievements = set(achievements)

    def get_name(self) -> str:
        """Returns the player's name."""
        return self.__name

    def get_achievements(self) -> set[str]:
        """Returns the player's set of unlocked achievements."""
        return self.__achievements

    def __str__(self) -> str:
        """Returns a formatted string for player and their achievements."""
        return f"Player {self.__name} achievements: {self.__achievements}"


def get_all_achievements(players: list[Player]) -> set[str]:
    """Returns the union of all achievements across all players"""
    if not players:
        return set()

    all_unique: set[str] = set()
    for player in players:
        all_unique = all_unique.union(player.get_achievements())

    return all_unique


def get_common_achievements(players: list[Player]) -> set[str]:
    """Returns the intersection of achievements shared by all players."""
    if not players:
        return set()

    common_all: set[str] = players[0].get_achievements()
    for player in players:
        common_all = common_all.intersection(player.get_achievements())

    return common_all


def get_rare_achievements(players: list[Player]) -> set[str]:
    """Returns the set of achievements held by exactly one player."""
    if not players:
        return set()

    all_overlaps: set[str] = set()
    remaining_players = players[:]

    for p1 in players:
        remaining_players = remaining_players[1:]
        for p2 in remaining_players:
            overlap = compare_players(p1, p2)[0]
            all_overlaps = all_overlaps.union(overlap)

    return get_all_achievements(players).difference(all_overlaps)


def compare_players(
        p1: Player, p2: Player
) -> tuple[set[str], set[str], set[str]]:
    """Compare two Player achievements."""
    achv1, achv2 = p1.get_achievements(), p2.get_achievements()

    common = achv1.intersection(achv2)
    p1_unique = achv1.difference(achv2)
    p2_unique = achv2.difference(achv1)

    return (common, p1_unique, p2_unique)


def analyse_global_achievements(players: list[Player]) -> None:
    """Calculates and prints all players achivements analytics."""
    print("=== Achivement Analytics ===")

    all = get_all_achievements(players)
    common = get_common_achievements(players)
    rare = get_rare_achievements(players)

    print()
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements:{len(all)}")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")


def analyse_rivals(p1: Player, p2: Player) -> None:
    """Compares two specific players and prints the results."""
    name1 = p1.get_name()
    name2 = p2.get_name()
    common, p1_unique, p2_unique = compare_players(p1, p2)

    print()
    print(f"{name1} vs {name2} common: {common}")
    print(f"{name1} unique: {p1_unique}")
    print(f"{name2} unique: {p2_unique}")


def analyse_all_rivalries(players: list[Player]) -> None:
    """Itarates through all unique pair of rivals and compares them."""
    remaining_players = players[:]

    for p1 in players:
        remaining_players = remaining_players[1:]
        for p2 in remaining_players:
            analyse_rivals(p1, p2)


def spawn_players(player_data: list[tuple[str, set[str]]]) -> list[Player]:
    """Creates a list of Player froma a list of player data."""
    players = []

    for data in player_data:
        name, achievements = data
        new_player = Player(name, achievements)
        players.append(new_player)

    return players


def main() -> None:
    """Demo: shows the achievement analytics system."""
    print("=== Achievement Tracker System ===")
    print()
    player_data = [
            ("alice", {
                'first_kill',
                'level_10',
                'treasure_hunter',
                'speed_demon'}),
            ("bob", {
                'first_kill',
                'level_10',
                'boss_slayer',
                'collector'
                }),
            ("charlie", {
                'level_10',
                'treasure_hunter',
                'boss_slayer',
                'speed_demon',
                'perfectionist'
                })
    ]

    players = spawn_players(player_data)
    for player in players:
        print(player)
    print()

    analyse_global_achievements(players)
    analyse_all_rivalries(players)


if __name__ == "__main__":
    main()
