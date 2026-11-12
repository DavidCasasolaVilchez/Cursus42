/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   args_utils.c                                      :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/10/25 13:22:38 by dcasasol         #+#    #+#              */
/*   Updated: 2026/10/25 13:22:38 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	int_checker(char *input)
{
	int	n;

	n = atoi(input);
	if (n != 0 && n > 0)
		return (n);
	return (-1);
}

t_sch	scheduler_checker(char *input)
{
	if (!strcmp(input, "fifo"))
		return (FIFO);
	if (!strcmp(input, "edf"))
		return (EDF);
	return (ERROR);
}
