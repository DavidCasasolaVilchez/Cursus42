/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_calloc.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/09 11:18:50 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/09 11:24:57 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	unsigned char	*a;
	size_t			i;

	if (size != 0 && nmemb != 0)
	{
		if (size != 0 && nmemb > (((size_t) - 1) / size))
			return (NULL);
		a = malloc(size * nmemb);
		if (a == NULL)
			return (NULL);
		i = 0;
		while (i < (nmemb * size))
			a[i++] = 0;
		return ((void *) a);
	}
	return (malloc(1));
}
