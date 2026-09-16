/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_strchr.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/08 16:43:18 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/08 16:43:18 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

char	*ft_strchr(const char *s, int c)
{
	int		i;
	char	*p;

	i = 0;
	p = (char *) s;
	while (s[i])
	{
		if (s[i] == c)
			return (p);
		i++;
		p++;
	}
	if (c == '\0')
		return (p);
	return (NULL);
}
