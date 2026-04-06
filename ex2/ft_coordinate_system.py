# *********************************************************************** #
#                                                                         #
#                                                    :::      ::::::::    #
#    ft_coordinate_system.py                       :+:      :+:    :+:    #
#                                                +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>        +#+  +:+       +#+         #
#                                            +#+#+#+#+#+   +#+            #
#    Created: 2026/03/11 18:41:15 by orhernan     #+#    #+#              #
#    Updated: 2026/03/11 19:09:19 by orhernan    ###   ########.fr        #
#                                                                         #
# *********************************************************************** #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        usr_in = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = usr_in.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []
        is_valid = True

        for part in parts:
            cleaned_part = part.strip()
            try:
                coords.append(float(cleaned_part))
            except ValueError:
                print(f"Error on parameter '{cleaned_part}': could "
                      f"not convert string to float: '{cleaned_part}'")
                is_valid = False
                break

        if is_valid and len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")
    print()

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_points = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(
        f"Distance between the 2 sets of coordinates: {round(dist_points, 4)}"
    )


if __name__ == "__main__":
    main()
