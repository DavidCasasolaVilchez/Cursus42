/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/23 09:27:49 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/28 12:18:40 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static t_buffer	*ft_init_buffer(void)
{
	t_buffer	*buf;

	buf = malloc(sizeof(t_buffer));
	if (buf == NULL)
		return (NULL);
	buf->capacity = 42;
	buf->size = 0;
	buf->data = malloc(sizeof(char) * buf->capacity);
	if (buf->data == NULL)
		return (free(buf), NULL);
	buf->data[0] = '\0';
	return (buf);
}

static char	*ft_comprobate_rest(char **rest, int size, t_buffer *ln)
{
	char	*aux;
	int		posnl;
	int		i;

	if (*rest == NULL)
		return (NULL);
	posnl = ft_cnl(*rest, size);
	if (posnl == -1)
		return (NULL);
	ln->data = ft_realloc(ln, *rest, posnl);
	if (ln->data == NULL)
		return (NULL);
	aux = malloc(size - posnl + 1);
	if (aux == NULL)
		return (NULL);
	i = 0;
	while (i < (size - posnl))
	{
		aux[i] = (*rest)[posnl + i];
		i++;
	}
	aux[i] = '\0';
	ft_save_rest(rest, aux, 0);
	return (free(aux), ln->data);
}

static char	*ft_process_buffer(char *buffer, int res,
		char **rest, t_buffer *line)
{
	int		posnl;
	char	*new_line;

	posnl = ft_cnl(buffer, res);
	if (posnl != -1)
	{
		new_line = ft_realloc(line, buffer, posnl);
		if (new_line == NULL)
			return (NULL);
		ft_save_rest(rest, buffer, posnl);
		return (new_line);
	}
	new_line = ft_realloc(line, buffer, res);
	if (new_line == NULL)
		return (NULL);
	return (new_line);
}

static char	*ft_read_loop(int fd, char **rest, t_buffer *line)
{
	int		res;
	char	*buffer;

	buffer = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (buffer == NULL)
		return (free(line->data), NULL);
	res = read(fd, buffer, BUFFER_SIZE);
	if (res == -1)
		return (free(line->data), free(buffer), NULL);
	while (res > 0)
	{
		buffer[res] = '\0';
		line->data = ft_process_buffer(buffer, res, rest, line);
		if (ft_cnl(buffer, res) != -1 || line->data == NULL)
			return (free(buffer), line->data);
		res = read(fd, buffer, BUFFER_SIZE);
		if (res == -1)
			return (free(line->data), free(buffer), NULL);
	}
	if (line->data[0] == '\0')
		return (free(line->data), free(buffer), NULL);
	free(*rest);
	*rest = NULL;
	return (free(buffer), line->data);
}

char	*get_next_line(int fd)
{
	static char	*rest[1024];
	char		*result;
	t_buffer	*line;
	int			rest_len;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	rest_len = ft_strlen(rest[fd]);
	line = ft_init_buffer();
	if (line == NULL)
		return (NULL);
	if (ft_comprobate_rest(&rest[fd], rest_len, line) != NULL)
	{
		result = line->data;
		return (free(line), result);
	}
	line->data = ft_realloc(line, rest[fd], rest_len);
	free(rest[fd]);
	rest[fd] = NULL;
	if (line->data == NULL)
		return (NULL);
	result = ft_read_loop(fd, &rest[fd], line);
	return (free(line), result);
}
