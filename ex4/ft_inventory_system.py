# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 20:58:01 by orhernan         #+#    #+#              #
#    Updated: 2026/03/17 00:00:34 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


class Inventory:
    def __init__(self) -> None:
        self.__items: dict[str, int] = {}
        self.__categories: dict[str, dict[str, int]] = {
            "scarce": {},
            "moderate": {},
            "surplus": {}
        }

    def get_num_of_item(self, item_name: str) -> int:
        return self.__items.get(item_name, 0)

    @classmethod
    def from_args(cls, args: list[str]) -> "Inventory":
        """Builds an Inventory from command-line strings"""
        new_inventory = cls()

        for item_string in args:
            try:
                item_name, quantity = item_string.split(":")
                new_inventory.add_to_inventory(item_name, int(quantity))
            except ValueError:
                print(f"Warning:'{item_string}' is invalid.")
                print("Use 'item:qty' format")

        return new_inventory

    @staticmethod
    def __get_tier(qty: int) -> str:
        """Determines the category tier based on item quantity."""
        if qty == 0:
            return ""
        elif qty < 3:
            return "scarce"
        elif qty < 5:
            return "moderate"
        else:
            return "surplus"

    def __categorise_inventory(self, item_name: str, old_quantity: int):
        """Calculates tiers and updates the nested category dictionary."""
        new_quantity = self.get_num_of_item(item_name)

        old_tier = self.__get_tier(old_quantity)
        new_tier = self.__get_tier(new_quantity)

        if old_tier and old_tier != new_tier:
            self.__categories[old_tier].pop(item_name, None)

        self.__categories[new_tier].update({item_name: new_quantity})

    def add_to_inventory(self, item_name: str, quantity: int) -> None:
        """Adds loot to the items inventory and triggers category update."""
        old_quantity = self.get_num_of_item(item_name)
        self.__items[item_name] = old_quantity + quantity
        self.__categorise_inventory(item_name, old_quantity)

    def get_categories(self) -> dict[str, dict[str, int]]:
        """Returns the category dictionary."""
        return self.__categories

    def get_total_items(self) -> int:
        """Calculates the sum of all item quantities."""
        total = 0
        for qty in self.__items.values():
            total += qty
        return total

    def get_unique_items(self) -> int:
        """Returns the number of unique item types"""
        return len(self.__items.keys())

    def get_most_item(self):
        """Finds the most abundant item."""
        for tier in ["surplus", "moderate", "scarce"]:
            tier_dict = self.__categories[tier]

            if not tier_dict:
                continue

            most_name = ""
            max_qty = -1

            for name, qty in tier_dict.items():
                if qty > max_qty:
                    max_qty = qty
                    most_name = name
            return most_name
        return ""


def main() -> None:
    my_inventory = Inventory.from_args(sys.argv[1:])
