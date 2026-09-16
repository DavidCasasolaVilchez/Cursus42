/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   conversion_utils1.c                               :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/16 16:50:19 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:50:19 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libftprintf.h"

int	ft_putc(t_context *cx, va_list a)
{
	char	c;
	int		tam;

	tam = 1;
	c = va_arg(a, char);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		ft_putchar_fd(c, 1);
		tam += ft_flag_space(0, cx, tam, 1);
	}
	else
	{
		tam += ft_flag_space(0, cx, tam, 1);
		ft_putchar_fd(c, 1);
	}
	return (tam);
}

int	ft_puts(t_context *cx, va_list a)
{
	char	*s;
	int		tam;
	int		len;

	tam = 0;
	s = malloc(sizeof(char *));
	if (s == NULL)
		return (0);
	s = va_arg(a, char *);
	len = ft_slen(s);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		tam += ft_flag_prec(s, cx);
		tam += ft_flag_space(0, cx, tam, 1);
	}
	else
	{
		if (cx->prec != -1 && len > cx->prec)
			tam += ft_flag_space(0, cx, cx->prec, 1);
		else
			tam += ft_flag_space(0, cx, len, 1);
		tam += ft_flag_prec(s, cx);
	}
	return (tam);
}

int	ft_putp(t_context *cx, va_list a)
{
	unsigned long	mem;
	void			*ptr;
	int				tam;

	ptr = va_arg(a, void *);
	mem = (unsigned long) ptr;
	tam = 2 + ft_numlen_ulong(mem, 16);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		write(1, "0x", 2);
		ft_puthex(mem, "0123456789abcdef");
		tam += ft_flag_space(0, cx, tam, 1);
	}
	else
	{
		tam += ft_flag_space(0, cx, tam, 1);
		write(1, "0x", 2);
		ft_puthex(mem, "0123456789abcdef");
	}
	return (tam);
}

int	ft_putd(t_context *cx, va_list a)
{
	int	d;
	int	tam;
	int	aux;

	d = va_arg(a, int);
	tam = ft_size_conversion(d, cx, 10, 1);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		ft_flag_sign(d, cx);
		tam += ft_flag_zero(d, cx, tam, 1);
		ft_putnbr_decimal(d);
		tam += ft_flag_space(d, cx, tam, 1);
		return (tam);
	}
	if (cx->prec != -1 && cx->prec >= tam)
		aux = ft_flag_space(d, cx, cx->prec, 1);
	else
		aux = ft_flag_space(d, cx, tam, 1);
	ft_flag_sign(d, cx);
	tam += ft_flag_zero(d, cx, tam, 1);
	ft_putnbr_decimal(d);
	return (tam + aux);
}

int	ft_puti(t_context *cx, va_list a)
{
	int	i;
	int	tam;
	int	aux;

	i = va_arg(a, int);
	tam = ft_size_conversion(i, cx, 10, 1);
	if (ft_dt_flag(cx->flags, '-') == 1)
	{
		ft_flag_sign(i, cx);
		tam += ft_flag_zero(i, cx, tam, 1);
		ft_putnbr_decimal(i);
		tam += ft_flag_space(i, cx, tam, 1);
		return (tam);
	}
	if (cx->prec != -1 && cx->prec >= tam)
		aux = ft_flag_space(i, cx, cx->prec, 1);
	else
		aux = ft_flag_space(i, cx, tam, 1);
	ft_flag_sign(i, cx);
	tam += ft_flag_zero(i, cx, tam, 1);
	ft_putnbr_decimal(i);
	return (tam + aux);
}
