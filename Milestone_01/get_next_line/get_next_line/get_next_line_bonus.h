/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.h                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/23 09:28:04 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/23 14:05:24 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# include <unistd.h>
# include <stdlib.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

typedef struct s_buffer
{
	char	*data;
	int		size;
	int		capacity;
}	t_buffer;

char	*get_next_line(int fd);

int		ft_strlen(char *s);
int		ft_cnl(char *s, int r);
char	*ft_realloc(t_buffer *line, char *buffer, int buffer_size);
void	ft_save_rest(char **rest, char *s, int pos);

#endif