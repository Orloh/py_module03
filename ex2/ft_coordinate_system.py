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


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.__coordinate = (x, y, z)

    @classmethod
    def from_string(cls, coord_str: str) -> "Point | None":
        print(f'Parsing coordinates:"{coord_str}"')
        try:
            parts = coord_str.split()

            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])

            return cls(x, y, z)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args:{e.args}")
            return None
