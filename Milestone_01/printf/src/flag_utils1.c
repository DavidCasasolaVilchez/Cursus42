/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   flag_utils1.c                                     :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/16 16:50:14 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:50:14 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libftprintf.h"

void	ft_flag_sign(int num, t_context *cx)
{
	if (num < 0)
		ft_putchar_fd('-', 1);
	if (ft_dt_flag(cx->flags, ' ') == 1 || ft_dt_flag(cx->flags, '+') == 1)
		if (ft_dt_flag(cx->flags, '+') == 1)
			ft_flag_putsign(num, '+');
	else
		ft_flag_putsign(num, ' ');
}

int	ft_flag_zero(int num, t_context *cx, int tam, int sgn)
{
	if (cx->prec != -1)
	{
		if ((ft_dt_flag(cx->flags, ' ') == 1 || ft_dt_flag(cx->flags, '+') == 1
				|| num < 0) && sgn == 1)
			tam--;
		if ((cx->prec - tam) < 0)
			return (0);
		ft_fill((cx->prec - tam), '0');
		return (cx->prec - tam);
	}
	else if (ft_dt_flag(cx->flags, '0') == 1
		&& ft_dt_flag(cx->flags, '-') == 0)
	{
		if ((cx->width - tam) < 0)
			return (0);
		ft_fill((cx->width - tam), '0');
		return (cx->width - tam);
	}
	return (0);
}

int	ft_flag_prec(char *s, t_context *cx)
{
	int	i;

	i = 0;
	if (cx->prec != -1)
		while (s[i] && i < cx->prec)
			ft_putchar_fd(s[i++], 1);
	else
		while (s[i])
			ft_putchar_fd(s[i++], 1);
	return (i);
}

int	ft_flag_space(int num, t_context *cx, int tam, int sgn)
{
	if (ft_dt_flag(cx->flags, '0') == 0 || cx->prec != -1)
	{
		if (cx->prec != -1)
		{
			if ((ft_dt_flag(cx->flags, ' ') == 1
					|| ft_dt_flag(cx->flags, '+') == 1 || num < 0) && sgn == 1)
				tam++;
			if ((cx->width - tam) < 0)
				return (0);
			ft_fill((cx->width - tam), ' ');
			return (cx->width - tam);
		}
	}
	else
	{
		if ((cx->width - tam) < 0)
			return (0);
		ft_fill((cx->width - tam), ' ');
		return (cx->width - tam);
	}
}

int	ft_flag_alternative(int num, t_context *cx, int may)
{
	if (ft_dt_flag(cx->flags, '#') == 1)
	{
		if (num != 0)
		{
			if (may == 0)
				ft_putstr_fd("0x", 1);
			else
				ft_putstr_fd("0X", 1);
			return (2);
		}
		ft_putstr_fd("0", 1);
		return (1);
	}
}
