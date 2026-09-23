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

#include "libft.h"

static size_t	ft_strlen_aux(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

static char	*ft_liberable_return(void)
{
	char	*n;

	n = malloc(sizeof(char));
	if (n == NULL)
		return (NULL);
	n[0] = '\0';
	return (n);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*n;
	size_t	i;
	size_t	j;

	if (start > ft_strlen_aux(s) || len > ((size_t) - 1) - start)
		return (ft_liberable_return());
	if ((ft_strlen_aux(s) - (size_t)start) < len)
		n = malloc(sizeof(char) * ((ft_strlen_aux(s) - (size_t)start) + 1));
	else
		n = malloc(sizeof(char) * (len + 1));
	if (n == NULL)
		return (ft_liberable_return());
	i = start;
	j = 0;
	while (s[i] && i < (start + len))
		n[j++] = s[i++];
	n[j] = '\0';
	return (n);
}
