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


class Point:
    """Represents a 3D coordinate poiont in the game world."""

    def __init__(self, x: int, y: int, z: int) -> None:
        """Initializes the POint with immutable x, y and z coordinates."""
        self.__coordinate = (x, y, z)

    @classmethod
    def from_string(cls, coord_str: str) -> "Point | None":
        """
        Creates a Point instance from a comma-separated string.
        Returns None if parsing fails due to invalid formatting.
        """
        try:
            parts = coord_str.split(",")

            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])

            return cls(x, y, z)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args:{e.args}")
            return None

    def get_coordinate(self) -> tuple[int, int, int]:
        """Access private coordinate tuple."""
        return self.__coordinate

    def calculate_distance(self, target: "Point | None" = None) -> float:
        """Calculates 3D distance to another point or the origin (0, 0, 0)."""
        x1, y1, z1 = self.__coordinate
        if target is None:
            x2, y2, z2 = (0, 0, 0)
        else:
            x2, y2, z2 = target.get_coordinate()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def show_position(self) -> None:
        """Demonstrates tuple unpacking and prints the current position."""
        x, y, z = self.__coordinate
        print(f"Player at x={x}, y={y}, z={z}")

    def __str__(self) -> str:
        """Returns the string representation of the coordinate tuple."""
        return f"{self.__coordinate}"


def main() -> None:
    """Demo: testing of the Point class"""
    print("=== Game Coordinate System ===")

    p1 = Point(10, 20, 5)
    origin = Point(0, 0, 0)

    print(f"Position created {p1}")
    distance1 = p1.calculate_distance(origin)
    print(f"Distance between {origin} and {p1}: {distance1:.2f}")

    coordinates = "3,4,0"
    print(f'Parsing coordinates: "{coordinates}"')
    p2 = Point.from_string(coordinates)
    if p2 is not None:
        print(f"Parsed position: {p2}")
        distance2 = p2.calculate_distance(origin)
        print(f"Distance between {origin} and {p2}: {distance2:.2f}")

    invalid = "abc, def, ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')
    p3 = Point.from_string(invalid)
    if p3 is not None:
        print(f"This should not be printed: {p3}")

    print("Unpacking demonstration:")
    p1.show_position()
    if p2 is not None:
        p2.show_position()


if __name__ == "__main__":
    main()
