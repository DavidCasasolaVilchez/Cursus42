/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/23 09:28:10 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/23 14:06:20 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	if (s == NULL)
		return (0);
	while (s[i])
		i++;
	return (i);
}

int	ft_cnl(char *s, int r)
{
	int	i;

	i = 0;
	while (i < r)
	{
		if (s[i] == '\n')
			return (i + 1);
		i++;
	}
	return (-1);
}

char	*ft_realloc(t_buffer *line, char *buffer, int buffer_size)
{
	char	*new;
	int		i;

	if (line->size + buffer_size + 1 > line->capacity)
	{
		line->capacity *= 2;
		if (line->capacity < line->size + buffer_size + 1)
			line->capacity = line->size + buffer_size + 1;
		new = malloc(line->capacity);
		if (new == NULL)
			return (free(line->data), NULL);
		i = -1;
		while (++i < line->size)
			new[i] = line->data[i];
		free(line->data);
		line->data = new;
	}
	i = -1;
	while (++i < buffer_size)
		line->data[line->size + i] = buffer[i];
	line->size += buffer_size;
	line->data[line->size] = '\0';
	return (line->data);
}

void	ft_save_rest(char **rest, char *s, int pos)
{
	int		i;
	char	*new_rest;

	if (s == NULL)
		return ;
	i = 0;
	while (s[pos + i])
		i++;
	if (i != 0)
	{
		new_rest = malloc(i + 1);
		if (new_rest == NULL)
			return ;
		i = 0;
		while (s[pos])
			new_rest[i++] = s[pos++];
		new_rest[i] = '\0';
		free(*rest);
		*rest = new_rest;
	}
	else
	{
		free(*rest);
		*rest = NULL;
	}
}
