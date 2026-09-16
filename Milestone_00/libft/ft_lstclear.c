/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_lstclear.c                                     :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/10 15:49:35 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 15:49:40 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*nodo1;
	t_list	*nodo2;

	if (lst == NULL || *lst == NULL)
		return ;
	nodo1 = *lst;
	while (nodo1->next != NULL)
	{
		del(nodo1->content);
		nodo2 = nodo1->next;
		free(nodo1);
		nodo1 = nodo2;
	}
	del(nodo1->content);
	free(nodo1);
	*lst = NULL;
}
