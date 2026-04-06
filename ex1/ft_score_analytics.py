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


class EmptyScoreboardError(Exception):
    pass


class Scoreboard:
    def __init__(self, scores_str: list[str]) -> None:
        self.__scores = self.__parse_scores(scores_str)

        if len(self.__scores) == 0:
            raise EmptyScoreboardError("No valid scores to process.")

    @staticmethod
    def __parse_scores(scores_str: list[str]) -> list[int]:
        scores: list[int] = []
        for score in scores_str:
            try:
                scores.append(int(score))
            except ValueError:
                print(f"Parsing Error: '{score}' is not a valid input.")
                print("Warning: Skipping invalid input...")
        return scores

    def get_scores(self) -> list[int]:
        return self.__scores

    def get_num_players(self) -> int:
        return len(self.__scores)

    def get_sum_scores(self) -> int:
        return sum(self.__scores)

    def get_avg_score(self) -> float:
        return self.get_sum_scores() / self.get_num_players()

    def get_high_score(self) -> int:
        return max(self.__scores)

    def get_low_score(self) -> int:
        return min(self.__scores)

    def get_range_score(self) -> int:
        return self.get_high_score() - self.get_low_score()


def main() -> None:
    print("=== Player Score Analytics ===")
    try:
        if len(sys.argv) < 2:
            raise EmptyScoreboardError("No scores provided")
        board = Scoreboard(sys.argv[1:])
        print(f"Scores processed: {board.get_scores()}")
        print(f"Total players: {board.get_num_players()}")
        print(f"Total score: {board.get_sum_scores()}")
        print(f"Average score: {board.get_avg_score():.1f}")
        print(f"High score: {board.get_high_score()}")
        print(f"Low score: {board.get_low_score()}")
        print(f"Score range: {board.get_range_score()}")
    except EmptyScoreboardError as e:
        print(e)
        print("Usage python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
