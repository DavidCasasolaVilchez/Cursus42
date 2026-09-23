/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_lstsize.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/10 15:18:42 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 15:18:42 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

unsigned int	ft_lstsize(t_list *lst)
{
	unsigned int	i;
	t_list			*nodo;

	if (lst == NULL)
		return (0);
	nodo = lst;
	i = 0;
	while (nodo->next != NULL)
	{
		i++;
		nodo = nodo->next;
	}
	return (i + 1);
}
