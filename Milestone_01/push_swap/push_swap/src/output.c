/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   output.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jucortes <jucortes@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/29 10:00:00 by jucortes          #+#    #+#             */
/*   Updated: 2026/09/29 10:00:00 by jucortes         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

const char	*op_name(int op)
{
	static const char	*names[N_OPS] = {
		"sa",
		"sb",
		"ss",
		"pa",
		"pb",
		"ra",
		"rb",
		"rr",
		"rra",
		"rrb",
		"rrr"
	};

	if (op < 0 || op >= N_OPS)
		return ("");
	return (names[op]);
}

static void	write_all(const char *buf, size_t len)
{
	ssize_t	w;

	while (len > 0)
	{
		w = write(1, buf, len);
		if (w <= 0)
			return ;
		buf += w;
		len -= w;
	}
}

static size_t	fill(t_ps *p, char *buf)
{
	size_t		pos;
	int			i;
	const char	*name;

	pos = 0;
	i = 0;
	while (i < p->nops)
	{
		name = op_name(p->ops[i++]);
		pos += ft_strlcpy(buf + pos, name, 5);
		buf[pos++] = '\n';
	}
	return (pos);
}

void	print_ops(t_ps *p)
{
	char	*buf;

	if (p->nops == 0)
		return ;
	buf = malloc((size_t)p->nops * 5);
	if (!buf)
		return ;
	write_all(buf, fill(p, buf));
	free(buf);
}
