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


from typing import Generator


def event_stream(limit: int) -> Generator[tuple[str, str, int], None, None]:
    names = ["alice", "bob", "charlie", "diana"]
    events = ["killed monster", "found treasure", "leveled up"]
    levels = [4, 10, 15]

    for index in range(limit):
        name = names[index % len(names)]
        event = events [index % len(events)]
        level = levels[index % len(levels)]
        yield (name, event, level)


def fibonacci_stream(limit: int = 10) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_stream(limit: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < limit:
        is_prime = True
        for index in range(2, num):
            if num % index == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1
