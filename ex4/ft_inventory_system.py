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


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(':')

        if len(parts) != 2:
            print(f"Error invalid parameter '{arg}'")
            continue

        item_name = parts[0].strip()
        quantity_str = parts[1].strip()

        if item_name in inventory:
            print(f"Redundant item '{item_name}' discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    if total_quantity > 0:
        for item_name, quantity in inventory.items():
            percentage = round((quantity / total_quantity) * 100, 1)
            print(f"Item {item_name} represents {percentage}%")

        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item_name in item_list:
            if inventory[item_name] > inventory[most_abundant]:
                most_abundant = item_name
            if inventory[item_name] < inventory[least_abundant]:
                least_abundant = item_name

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
