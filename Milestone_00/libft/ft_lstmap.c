/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_lstmap.c                                       :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/10 17:52:40 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 17:52:40 by dcasasol        ###   ########.fr        */
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

static void	ft_lstadd_back_1(t_list *lst, t_list *new)
{
	t_list	*nodo;

	nodo = lst;
	if (lst == NULL)
		lst = new;
	else
	{
		while (nodo->next != NULL)
			nodo = nodo->next;
		nodo->next = new;
	}
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*res;
	t_list	*nodo;

	res = NULL;
	while (lst != NULL)
	{
		nodo = malloc(sizeof(t_list));
		if (nodo == NULL)
		{
			ft_lstclear(&res, del);
			return (NULL);
		}
		nodo->content = f(lst->content);
		nodo->next = NULL;
		if (res == NULL)
			res = nodo;
		else
			ft_lstadd_back_1(res, nodo);
		lst = lst->next;
	}
	return (res);
}
