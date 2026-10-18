# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 10:53:40 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 10:53:41 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    days_left = int(input("Days until harvest: "))
    for i in range(days_left):
        print(f"Day {i + 1}")
    print("Harvest time!")
