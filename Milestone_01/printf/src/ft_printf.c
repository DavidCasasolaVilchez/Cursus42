/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_printf.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/14 09:59:19 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:49:57 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libftprintf.h"

int	ft_printf(char const *str, ...)
{
	int		i;
	int		p;
	int		res;
	va_list	a;

	va_start(a, str);
	res = 0;
	p = 0;
	i = -1;
	while (str[++i])
	{
		if (str[i] != '%')
		{
			ft_putchar_fd(str[i], 1);
			p++;
		}
		else
		{
			res = ft_evaluate_conversion(str, &i, a, ft_create_conversions());
			if (res == -1)
				return (-1);
			p += res;
		}
	}
	return (p);
}
