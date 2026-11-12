/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   memory_utils.c                                    :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/10/25 13:45:18 by dcasasol         #+#    #+#              */
/*   Updated: 2026/10/25 13:45:18 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	*ft_calloc(unsigned int nmemb, unsigned int size)
{
	unsigned char	*a;
	unsigned int	i;

	if (size != 0 && nmemb != 0)
	{
		if (size != 0 && nmemb > (((unsigned int) - 1) / size))
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
