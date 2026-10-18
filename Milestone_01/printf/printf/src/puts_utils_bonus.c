/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   puts_utils_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:49:38 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/29 11:44:19 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf_bonus.h"

void	ft_puthex(unsigned long mem, char *base, int pn)
{
	if (mem == 0 && pn == 1)
		ft_putstr_fd("(nil)", 1);
	else
	{
		if (mem > 0)
			ft_puthex(mem / 16, base, 0);
		else
			return ;
		ft_putchar_fd(base[mem % 16], 1);
	}
}

void	ft_putnbr_hexadecimal(unsigned int num, char *base, int pn)
{
	if (num == 0 && pn == 1)
		ft_putchar_fd('0', 1);
	else
	{
		if (num > 0)
			ft_puthex(num / 16, base, 0);
		else
			return ;
		ft_putchar_fd(base[num % 16], 1);
	}
}

void	ft_putnbr_decimal(int d, int pn)
{
	long	l;

	l = d;
	if (l == 0 && pn == 1)
		ft_putchar_fd('0', 1);
	else
	{
		if (l < 0)
			l = -l;
		if (l > 0)
			ft_putnbr_decimal(l / 10, 0);
		else
			return ;
		ft_putchar_fd("0123456789"[l % 10], 1);
	}
}

void	ft_putnbr_decimal_unsigned(unsigned int d, int pn)
{
	if (d == 0 && pn == 1)
		ft_putchar_fd('0', 1);
	else
	{
		if (d < 0)
			d = -d;
		if (d > 0)
			ft_putnbr_decimal(d / 10, 0);
		else
			return ;
		ft_putchar_fd("0123456789"[d % 10], 1);
	}
}

int	ft_print_char(char c)
{
	ft_putchar_fd(c, 1);
	return (1);
}
