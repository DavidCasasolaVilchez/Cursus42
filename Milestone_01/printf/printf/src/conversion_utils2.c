/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   conversion_utils2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:50:17 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/28 10:20:07 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

int	ft_put_space_minus(t_context *cx, unsigned int x, int tam)
{
	int		aux;

	if (cx->prec != -1 && cx->prec > tam)
		aux = ft_flag_space(x, cx, cx->prec, 0);
	else
		aux = ft_flag_space(x, cx, tam, 0);
	return (aux);
}

int	ft_putu(t_context *cx, va_list a)
{
	unsigned int	u;
	int				tam;
	int				aux;

	u = va_arg(a, unsigned int);
	tam = ft_size_conversion(u, cx, 10, 0);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		tam += ft_flag_zero(u, cx, tam, 0);
		ft_putnbr_decimal_unsigned(u, 1);
		tam += ft_flag_space(u, cx, tam, 0);
	}
	else
	{
		if (cx->prec != -1 && cx->prec > tam)
			aux = ft_flag_space(u, cx, cx->prec, 0);
		else
			aux = ft_flag_space(u, cx, tam, 0);
		tam += ft_flag_zero(u, cx, tam, 0);
		ft_putnbr_decimal_unsigned(u, 1);
		tam += aux;
	}
	return (ft_free_context(cx, tam));
}

int	ft_putx(t_context *cx, va_list a)
{
	unsigned int	x;
	int				tam;
	int				aux;

	x = va_arg(a, unsigned int);
	tam = ft_size_conversion(x, cx, 16, 0);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		ft_flag_alternative(x, cx, 0);
		tam += ft_flag_zero(x, cx, tam, 0);
		ft_putnbr_hexadecimal(x, "0123456789abcdef", 1);
		tam += ft_flag_space(x, cx, tam, 0);
	}
	else
	{
		aux = ft_put_space_minus(cx, x, tam);
		ft_flag_alternative(x, cx, 0);
		tam += ft_flag_zero(x, cx, tam, 0);
		ft_putnbr_hexadecimal(x, "0123456789abcdef", 1);
		tam += aux;
	}
	if (ft_dt_flag(cx->flags, '#') == 1)
		tam += ((x != 0) * 2);
	return (ft_free_context(cx, tam));
}

int	ft_putxx(t_context *cx, va_list a)
{
	unsigned int	x;
	int				tam;
	int				aux;

	x = va_arg(a, unsigned int);
	tam = ft_size_conversion(x, cx, 16, 0);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		ft_flag_alternative(x, cx, 1);
		tam += ft_flag_zero(x, cx, tam, 0);
		ft_putnbr_hexadecimal(x, "0123456789ABCDEF", 1);
		tam += ft_flag_space(x, cx, tam, 0);
	}
	else
	{
		aux = ft_put_space_minus(cx, x, tam);
		ft_flag_alternative(x, cx, 1);
		tam += ft_flag_zero(x, cx, tam, 0);
		ft_putnbr_hexadecimal(x, "0123456789ABCDEF", 1);
		tam += aux;
	}
	if (ft_dt_flag(cx->flags, '#') == 1)
		tam += ((x != 0) * 2);
	return (ft_free_context(cx, tam));
}

int	ft_put_porcent(t_context *cx, va_list a)
{
	(void) cx;
	(void) a;
	ft_putchar_fd('%', 1);
	return (ft_free_context(cx, 1));
}
