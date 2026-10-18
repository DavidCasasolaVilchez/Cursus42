/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   flag_utils2_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:49:59 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/29 11:44:09 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf_bonus.h"

int	ft_dt_flag(char *flags, char search)
{
	int	i;

	i = 0;
	while (flags[i])
		if (flags[i++] == search)
			return (1);
	return (0);
}

int	ft_size_conversion(int num, t_context *cx, int base, int sgn)
{
	int	len;

	len = ft_numlen(num, base, sgn);
	if ((ft_dt_flag(cx->flags, ' ') == 1 || ft_dt_flag(cx->flags, '+') == 1
			|| num < 0) && sgn == 1)
		len++;
	return (len);
}

void	ft_fill(int tam, char car)
{
	int	i;

	i = 0;
	while (i < tam)
	{
		ft_putchar_fd(car, 1);
		i++;
	}
}

void	ft_flag_putsign(int num, char plus)
{
	if (num >= 0)
		ft_putchar_fd(plus, 1);
}
