/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/08 16:32:56 by dcasasol          #+#    #+#             */
/*   Updated: 2026/10/04 23:16:25 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	s;
	size_t	d;

	i = -1;
	d = 0;
	s = 0;
	while (dst[d] != '\0')
		d++;
	while (src[s] != '\0')
		s++;
	if (size <= d || size == 0)
		return (size + s);
	while (src[++i] != '\0' && (d + i) < (size - 1))
		dst[d + i] = src[i];
	dst[d + i] = '\0';
	return (d + s);
}
