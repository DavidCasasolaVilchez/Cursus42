# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_data.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/29 14:11:26 by dcasasol          #+#    #+#             #
#    Updated: 2026/09/29 14:11:27 by dcasasol         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, nm: str, h: int, a: int):
        self.name = nm
        self.height = h
        self.age = a

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 45, 80)
    p3 = Plant("Cactus", 15, 120)
    p1.show()
    p2.show()
    p3.show()
