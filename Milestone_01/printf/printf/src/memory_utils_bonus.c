/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   memory_utils_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:49:38 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/29 11:44:17 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf_bonus.h"

int	ft_end_list(va_list a, int p, t_conversion	*co)
{
	free(co);
	va_end(a);
	return (p);
}

int	ft_free_context(t_context *cx, int ret)
{
	if (cx != NULL)
	{
		free(cx->flags);
		free(cx);
	}
	return (ret);
}

int	ft_char_lector(char const *str, va_list a, t_conversion *cn, int *i)
{
	int		res;

	if (str[*i] != '%')
		return (ft_print_char(str[*i]));
	res = ft_evaluate_conversion(str, i, a, cn);
	if (res == -1)
		return (ft_end_list(a, -1, cn));
	return (res);
}
