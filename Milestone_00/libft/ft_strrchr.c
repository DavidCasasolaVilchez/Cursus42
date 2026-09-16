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

#include "ft_libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*p;
	char	*r;

	i = 0;
	p = (char *) s;
	r = NULL;
	while (s[i])
	{
		if (s[i] == c)
			r = p;
		i++;
		p++;
		if (s[i] == '\0' && c == '\0')
			r = p;
	}
	return (r);
}
