# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 10:59:02 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 10:59:03 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive():
    days_left = int(input("Days until harvest: "))
    ft_recursive_count(1, days_left)
    print("Harvest time!")


def ft_recursive_count(i: int, days: int):
    print(f"Day {i}")
    if i < days:
        ft_recursive_count(i + 1, days)
