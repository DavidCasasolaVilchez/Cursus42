/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_lstlast.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/10 15:21:04 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 15:21:04 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	t_list	*nodo;

	if (lst == NULL)
		return (NULL);
	nodo = lst;
	while (nodo->next != NULL)
		nodo = nodo->next;
	return (nodo);
}
