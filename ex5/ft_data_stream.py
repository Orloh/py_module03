# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 21:34:04 by orhernan         #+#    #+#              #
#    Updated: 2026/03/19 22:37:15 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


import random
import typing


def gen_event(
    players: list[str],
    actions: list[str]
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        random_index = random.randrange(len(events))
        yield events.pop(random_index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players = ['alice', 'bob', 'charlie', 'diana', 'edgar']
    actions = ['jump', 'run', 'eat', 'move', 'climb', 'release']
    stream = gen_event(players, actions)

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
    print()

    ten_events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for consumed in consume_event(ten_events):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
