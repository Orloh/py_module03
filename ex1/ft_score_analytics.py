# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/10 19:22:28 by orhernan         #+#    #+#              #
#    Updated: 2026/03/10 20:57:10 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


class Scoreboard:
    def __init__(self, scores_str: list[str]) -> None:
        self.__scores = self.__parse_scores(scores_str)

    @staticmethod
    def __parse_scores(scores_str: list[str]) -> list[int]:
        scores: list[int] = []
        for score in scores_str:
            try:
                scores.append(int(score))
            except ValueError as e:
                print(f"Parsing Error: {e}")
                print("Warning: Skipping invalid scores...")
        return scores

    def get_high_score(self) -> int:
        return max(self.__scores)

    def get_low_score(self) -> int:
        return min(self.__scores)


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage python3 ft_score_analytcs.py <score1> <score2> ...")
        return
    board = Scoreboard(sys.argv[1:])
    print(board.get_high_score())
    print(board.get_low_score())


if __name__ == "__main__":
    main()
