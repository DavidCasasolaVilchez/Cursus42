/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/08 16:12:03 by dcasasol          #+#    #+#             */
/*   Updated: 2026/10/04 23:42:07 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	s;

	i = -1;
	s = 0;
	while (src[s] != '\0')
		s++;
	if (size == 0)
		return (s);
	while (src[++i] != '\0' && i < (size - 1))
		dst[i] = src[i];
	dst[i] = '\0';
	return (s);
}
