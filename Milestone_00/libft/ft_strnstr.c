/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_strnstr.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/08 17:48:21 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/08 17:54:36 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

static int	ft_check_match(const char *b, const char *t, size_t i, size_t l)
{
	size_t	j;

	j = 0;
	while (t[j] && (i + j) < l)
	{
		if (t[j] != b[i + j])
			return (0);
		j++;
	}
	if (t[j] == '\0')
		return (1);
	return (0);
}

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;

	if (little[0] == '\0')
		return ((char *) big);
	i = 0;
	while (big[i] && i < len)
	{
		if (ft_check_match(big, little, i, len))
			return ((char *) & big[i]);
		i++;
	}
	return (NULL);
}
