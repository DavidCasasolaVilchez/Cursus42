/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   context_utils.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:50:23 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/28 10:47:21 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

int	ft_evaluate_conversion(char const *str, int *ptr, va_list a,
	t_conversion *convers)
{
	t_context	*cx;
	char		car;
	int			i;

	i = 0;
	cx = malloc(sizeof(t_context));
	if (cx == NULL)
		return (ft_free_context(cx, -1));
	cx->prec = -1;
	cx->width = 0;
	*ptr += 1;
	*ptr = ft_get_context(str, *ptr, cx);
	car = str[*ptr];
	while (convers[i].indx != '\0')
	{
		if (convers[i].indx == car)
			return (convers[i].func(cx, a));
		i++;
	}
	return (ft_free_context(cx, -1));
}

int	ft_count_flags(char const *str, int ptr)
{
	int		i;
	int		cf;
	char	characters[6];

	i = -1;
	while ("-0# +"[++i] != '\0')
		characters[i] = "-0# +"[i];
	characters[i] = '\0';
	cf = 0;
	while (str[ptr])
	{
		i = 0;
		while (characters[i])
		{
			if (characters[i] == str[ptr])
			{
				cf++;
				characters[i] = '_';
			}
			i++;
		}
		ptr++;
	}
	return (cf);
}

int	ft_content_char(char *characters, char *flags, char search)
{
	int	i;

	i = 0;
	while (characters[i])
	{
		if (characters[i] == search)
		{
			i = 0;
			while (flags[i])
			{
				if (flags[i] == search)
					return (0);
				i++;
			}
			return (1);
		}
		i++;
	}
	return (0);
}

int	ft_get_context(char const *str, int ptr, t_context *cx)
{
	int	j;

	j = 0;
	cx->flags = malloc(sizeof(char) * (ft_count_flags(str, ptr) + 1));
	if (cx->flags == NULL)
		return (ft_free_context(cx, -1));
	cx->flags[j] = '\0';
	while (ft_content_char("-0# +", cx->flags, str[ptr]) == 1)
	{
		cx->flags[j++] = str[ptr++];
		cx->flags[j] = '\0';
	}
	while (str[ptr] >= 48 && str[ptr] <= 57)
		cx->width = (cx->width * 10) + (str[ptr++] - '0');
	if (str[ptr] == '.')
	{
		ptr++;
		cx->prec = 0;
		while (str[ptr] >= 48 && str[ptr] <= 57)
			cx->prec = (cx->prec * 10) + (str[ptr++] - '0');
	}
	return (ptr);
}

t_conversion	*ft_create_conversions(void)
{
	t_conversion	*cs;

	cs = malloc(sizeof(t_conversion) * 10);
	if (cs == NULL)
		return (NULL);
	cs[0] = (t_conversion){'c', ft_putc};
	cs[1] = (t_conversion){'s', ft_puts};
	cs[2] = (t_conversion){'p', ft_putp};
	cs[3] = (t_conversion){'d', ft_putd};
	cs[4] = (t_conversion){'i', ft_puti};
	cs[5] = (t_conversion){'u', ft_putu};
	cs[6] = (t_conversion){'x', ft_putx};
	cs[7] = (t_conversion){'X', ft_putxx};
	cs[8] = (t_conversion){'%', ft_put_porcent};
	cs[9] = (t_conversion){'\0', ft_put_porcent};
	return (cs);
}
