# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_harvest_total.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 10:42:52 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 10:42:53 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    harvest = 0
    harvest += int(input("Day 1 harvest: "))
    harvest += int(input("Day 2 harvest: "))
    harvest += int(input("Day 3 harvest: "))
    print(f"Total harvest: {harvest}")
