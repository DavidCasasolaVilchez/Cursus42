/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_strjoin.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/09 12:12:43 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/09 12:12:43 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	i;
	size_t	t;
	size_t	t1;
	size_t	t2;
	char	*c;

	t1 = ft_strlen(s1);
	t2 = ft_strlen(s2);
	t = t1 + t2;
	c = malloc(sizeof(char) * (t + 1));
	if (c == NULL)
		return (NULL);
	i = -1;
	while (++i < t1)
		c[i] = s1[i];
	i = -1;
	while (++i < t2)
		c[t1 + i] = s2[i];
	c[t1 + t2] = '\0';
	return (c);
}
