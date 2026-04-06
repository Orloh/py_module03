# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/06 14:27:53 by orhernan         #+#    #+#              #
#    Updated: 2026/04/06 14:43:55 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()

    players = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'jhon',
        'kevin',
        'Liam'
    ]
    print(f"Initial list of players: {players}")

    capitalized_all = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_all}")

    capitalized_only = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")
    print()

    score_dict = {name: random.randint(10, 1000) for name in capitalized_all}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = {n: s for n, s in score_dict.items() if s > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
