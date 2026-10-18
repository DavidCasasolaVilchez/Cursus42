# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 11:04:23 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 11:04:24 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    aviable = "Unknown unit type"
    match unit:
        case "packets":
            aviable = f"{quantity} {unit.lower()} aviable"
        case "grams":
            aviable = f"{quantity} {unit.lower()} total"
        case "area":
            aviable = f"covers {quantity} square meters"
    print(f"{seed_type.capitalize()} seeds: {aviable.lower()}")
