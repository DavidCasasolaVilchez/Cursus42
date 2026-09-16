/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_strtrim.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/09 13:08:19 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/09 13:08:19 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

static size_t	ft_is_set(char c, char const *set)
{
	size_t	i;

	i = 0;
	while (set[i])
	{
		if (c == set[i])
			return (0);
		i++;
	}
	return (1);
}

static size_t	ft_strlen_1(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

static size_t	ft_strlen_1_trim(char const *s1, size_t len, char const *set)
{
	size_t	i;
	size_t	trim;

	i = 0;
	trim = 0;
	while (s1[i] && ft_is_set(s1[i++], set) == 0)
		trim++;
	i = len - 1;
	while (i >= 0 && ft_is_set(s1[i--], set) == 0)
		trim++;
	return (len - trim);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;
	size_t	t;
	size_t	f;
	char	*c;

	t = ft_strlen_1_trim(s1, ft_strlen_1(s1), set);
	c = malloc(sizeof(char) * (t + 1));
	if (c == NULL)
		return (NULL);
	i = ft_strlen_1(s1) - 1;
	f = 0;
	while (ft_is_set(s1[i--], set) == 0)
		f++;
	i = 0;
	j = 0;
	while (s1[i] && ft_is_set(s1[i], set) == 0)
		i++;
	while (s1[i] && s1[i + f])
		c[j++] = s1[i++];
	c[j] = '\0';
	return (c);
}
