# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 10:47:11 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 10:47:12 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
