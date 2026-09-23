/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   len_utils.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/16 16:49:28 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:49:53 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

int	ft_slen(char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

int	ft_numlen_ulong(unsigned long num, int base)
{
	int	i;

	i = 0;
	if (num == 0)
		return (1);
	while (num > 0)
	{
		i++;
		num /= base;
	}
	return (i);
}

int	ft_numlen_sgn(int num, int base)
{
	int		i;
	long	lnum;

	lnum = (long) num;
	i = 0;
	if (lnum == 0)
		return (1);
	if (lnum < 0)
		lnum = -lnum;
	while (lnum > 0)
	{
		i++;
		lnum /= base;
	}
	return (i);
}

int	ft_numlen_unsgn(unsigned int num, int base)
{
	int	i;

	i = 0;
	if (num == 0)
		return (1);
	while (num > 0)
	{
		i++;
		num /= base;
	}
	return (i);
}

int	ft_numlen(int num, int base, int sgn)
{
	if (sgn == 1)
		return (ft_numlen_sgn(num, base));
	return (ft_numlen_unsgn((unsigned int) num, base));
}
