/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_lstadd_back.c                                  :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/10 15:26:55 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 15:26:55 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*nodo;

	if (lst == NULL)
		return ;
	nodo = *lst;
	if (*lst == NULL)
		*lst = new;
	else
	{
		while (nodo->next != NULL)
			nodo = nodo->next;
		nodo->next = new;
	}
}
