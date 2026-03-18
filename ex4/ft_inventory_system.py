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

    @classmethod
    def from_args(cls, args: list[str]) -> "Inventory":
        """Builds an Inventory from command-line strings"""
        new_inventory = cls()

        for item_string in args:
            try:
                item_name, quantity = item_string.split(":")
                qty = int(quantity)
                if qty < 0:
                    print(f"Warning: '{item_string} is invalid. Quantity cannot be negative.")
                    continue
                new_inventory.add_to_inventory(item_name, qty)
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
        new_tier = self.__get_tier(new_quantity)
        old_tier = self.__get_tier(old_quantity)

        if old_tier and old_tier != new_tier:
            self.__categories[old_tier].pop(item_name, None)
        if new_tier:
            self.__categories[new_tier].update({item_name: new_quantity})

    def get_num_of_item(self, item_name: str) -> int:
        return self.__items.get(item_name, 0)

    def add_to_inventory(self, item_name: str, quantity: int) -> None:
        """Adds loot to the items inventory and triggers category update."""
        old_quantity = self.get_num_of_item(item_name)
        self.__items[item_name] = old_quantity + quantity
        self.__categorise_inventory(item_name, old_quantity)

    def get_categories(self) -> dict[str, dict[str, int]]:
        """Returns the category dictionary."""
        return self.__categories

    def get_items(self) -> dict[str, int]:
        """Returns the items dictionary."""
        return self.__items

    def get_total_items(self) -> int:
        """Calculates the sum of all item quantities."""
        total = 0
        for qty in self.__items.values():
            total += qty
        return total

    def get_unique_items(self) -> int:
        """Returns the number of unique item types"""
        return len(self.__items.keys())

    def get_most_item(self) -> tuple[str, int]:
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
            return (most_name, max_qty)
        return ("", 0)

    def get_least_item(self) -> tuple[str, int]:
        """Finds the least abundant item."""
        for tier in ["scarce", "moderate", "surplus"]:
            tier_dict = self.__categories[tier]

            if not tier_dict:
                continue

            least_name = ""
            least_qty = None

            for name, qty in tier_dict.items():
                if least_qty is None or qty < least_qty:
                    least_qty = qty
                    least_name = name
            assert least_qty is not None
            return (least_name, least_qty)
        return ("", 0)

    def get_restock(self) -> list[str]:
        """Returns a list of item names that have exactly 1 quantity."""
        return [name for name, qty in self.__categories["scarce"].items() if qty == 1]

    def __str__(self) -> str:
        """String representation of the full inventory."""
        total = self.get_total_items()

        if total == 0:
            return "(empty inventory)"

        lines = []

        for name, qty in self.__items.items():
            percent = (qty / total) * 100
            unit_label = "unit" if qty == 1 else "units"
            lines.append(f"{name}: {qty} {unit_label} ({percent:.1f}%)")

        return "\n".join(lines)

    def __getitem__(self, item_name: str) -> str:
        """Allows inventory['item'] access with formatted output"""
        qty = self.get_num_of_item(item_name)
        total = self.get_total_items()

        if qty == 0:
            return f"(You don't have {item_name})"

        percent = (qty/total) * 100
        unit_label = "unit" if qty == 1 else "units"
        return f"{item_name}: {qty} {unit_label} ({percent:.1f}%)"


def main() -> None:
    print("=== Inventory System Analysis ===")
    my_inventory = Inventory.from_args(sys.argv[1:])

    print(f"Total items in inventory: {my_inventory.get_total_items()}")
    print(f"Unique item types: {my_inventory.get_unique_items()}")
    print()

    print("=== Current Inventory ===")
    print(my_inventory)
    print()

    print("=== Inventory Statistics ===")
    item_name, qty = my_inventory.get_most_item()
    print(f"Most abundant: {item_name} ({qty} {'unit' if qty == 1 else 'units'})")
    item_name, qty = my_inventory.get_least_item()
    print(f"Least abundant: {item_name} ({qty} {'unit' if qty == 1 else 'units'})")
    print()

    print("=== Item Categories ===")
    categories = my_inventory.get_categories()
    for tier, items in categories.items():
        if items:
            print(f"{tier.capitalize()}: {items}")
    print()

    print("=== Management Suggestions ===")
    print(f"Restock needed: {','.join(my_inventory.get_restock())}")
    print()

    print("=== Dictionary Properties Demo ===")
    items = my_inventory.get_items()
    keys = items.keys()
    values = items.values()
    lookup = "sword"
    print(f"Dictionary keys: {','.join(keys)}")
    print(f"Dictionary values: {','.join(f'{v}' for v in values)}")
    print(f"Sample lookup -'{lookup}' in inventory: {items.get(lookup, 0) != 0}")


if __name__ == "__main__":
    main()
