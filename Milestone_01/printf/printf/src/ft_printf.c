/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/14 09:59:19 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/25 15:47:19 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

int	ft_printf(char const *str, ...)
{
	t_conversion	*conversions;
	int				res;
	int				i;
	int				p;
	va_list			a;

	conversions = ft_create_conversions();
	if (conversions == NULL || str == NULL)
		return (-1);
	va_start(a, str);
	res = 0;
	p = 0;
	i = -1;
	while (str[++i])
	{
		res = ft_char_lector(str, a, conversions, &i);
		if (res == -1)
			return (res);
		p += res;
	}
	return (ft_end_list(a, p, conversions));
}
