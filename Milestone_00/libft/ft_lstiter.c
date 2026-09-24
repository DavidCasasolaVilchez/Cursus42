/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/10 15:52:46 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/24 16:39:31 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list	*nodo;

	if (lst == NULL || f == NULL)
		return ;
	nodo = lst;
	while (nodo->next != NULL)
	{
		f(nodo->content);
		nodo = nodo->next;
	}
	f(nodo->content);
}
