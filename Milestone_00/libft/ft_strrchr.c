/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_strrchr.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/08 17:00:50 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/08 17:54:40 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_strlen_aux_strrchr(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*p;
	char	*r;

	i = 0;
	p = (char *) s;
	r = NULL;
	if (c == 0)
		return (p + ft_strlen_aux_strrchr(p));
	while (s[i])
	{
		if (s[i] == (char)c)
			r = p;
		i++;
		p++;
		if (s[i] == '\0' && (char)c == '\0')
			r = p;
	}
	return (r);
}
