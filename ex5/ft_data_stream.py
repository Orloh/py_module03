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
import time
import tracemalloc


def event_generator(total: int) -> Generator[tuple[str, int, str], None, None]:
    """
    Yield game events as (player, level, action)
    """
    names = ["alice", "bob", "charlie", "diana"]
    levels = [5, 8, 3, 10]
    actions = ["killed monster", "found treasure", "leveled up"]

    for index in range(total):
        name = names[index % len(names)]
        level = levels[index % len(levels)]
        action = actions[index % len(actions)]
        if action == "leveled up":
             level += 1
        yield (name, level, action)


def fibonacci_generator() -> Generator[int, None, None]:
    """
    Infinite fibonacci sequence...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """
    Determine if an integer is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    step = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += step
        step = 6 - step
    return True


def prime_generator(start: int = 2) -> Generator[int, None, None]:
    """
    Prime number generator...
    """
    num = start
    while True:
        if is_prime(num):
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    total_events = 10
    print(f"Processing {total_events} game events...\n")

    tracemalloc.start()
    t0 = time.perf_counter()

    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    index = 0
    to_show = 6
    for name, level, action in event_generator(total_events):
        if index <= to_show:
            print(f"Event {index}: Player {name} (level {level}) {action}")

        if level >= 10:
            high_level_count += 1
        if action == "found treasure":
            treasure_count += 1
        if action == "leveled up":
            level_up_count += 1
        index += 1

    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print(f"Memory usage: {peak / 1024:.1f}KB")
    print(f"Processing time: {elapsed:.6f} seconds")
    print()
    print("=== Generator Demonstration ===")
    f_stream = fibonacci_generator()
    f_nums = [f"{next(f_stream)}" for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(f_nums)}")
    p_stream = prime_generator()
    p_nums = [f"{next(p_stream)}" for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(p_nums)}")


if __name__ == "__main__":
    main()
