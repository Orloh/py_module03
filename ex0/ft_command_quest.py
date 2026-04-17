# *********************************************************************** #
#                                                                         #
#                                                    :::      ::::::::    #
#    ft_command_quest.py                           :+:      :+:    :+:    #
#                                                +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>        +#+  +:+       +#+         #
#                                            +#+#+#+#+#+   +#+            #
#    Created: 2026/03/09 18:28:46 by orhernan     #+#    #+#              #
#    Updated: 2026/03/09 18:31:52 by orhernan    ###   ########.fr        #
#                                                                         #
# *********************************************************************** #

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")

    args = sys.argv
    total_args = len(sys.argv)

    if total_args == 1:
        print(f"Program name: {args[0]}")
        print("No arguments provided!")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {total_args - 1}")
        for i, arg in enumerate(args[1:], start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    ft_command_quest()
