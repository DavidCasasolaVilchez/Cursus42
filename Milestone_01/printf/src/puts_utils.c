/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   puts_utils.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/16 16:49:38 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:49:38 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libftprintf.h"

void	ft_puthex(unsigned long mem, char *base)
{
	if (mem > 0)
		ft_puthex(mem / 16, base);
	else
		return ;
	ft_putchar_fd(base[mem % 16], 1);
}

void	ft_putnbr_hexadecimal(unsigned int num, char *base)
{
	if (num > 0)
		ft_puthex(num / 16, base);
	else
		return ;
	ft_putchar_fd(base[num % 16], 1);
}

void	ft_putnbr_decimal(int d)
{
	long	l;

	l = d;
	if (l < 0)
		l = -l;
	if (l > 0)
		ft_putnbr_decimal(l / 10);
	else
		return ;
	ft_putchar_fd("0123456789"[l % 10], 1);
}

void	ft_putnbr_decimal_unsigned(unsigned int d)
{
	if (d < 0)
		d = -d;
	if (d > 0)
		ft_putnbr_decimal(d / 10);
	else
		return ;
	ft_putchar_fd("0123456789"[d % 10], 1);
}
