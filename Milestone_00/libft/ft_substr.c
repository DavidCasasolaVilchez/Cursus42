/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_substr.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/09 11:46:32 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/09 11:46:32 by dcasasol        ###   ########.fr        */
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

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*n;
	size_t	i;
	size_t	j;

	if (start > ft_strlen(s) || len > ((size_t) - 1) - start)
		return (NULL);
	n = malloc(sizeof(char) * (len + 1));
	if (n == NULL)
		return (NULL);
	i = start;
	j = 0;
	while (s[i] && i < (start + len))
		n[j++] = s[i++];
	n[j] = '\0';
	return (n);
}
