/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   ft_split.c                                        :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/09 18:01:16 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/10 14:22:12 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "ft_libft.h"

static size_t	ft_count_words(char const *s, char c)
{
	size_t	i;
	size_t	p;

	i = 0;
	p = 0;
	while (s[i])
	{
		if (s[i] != c && (i == 0 || s[i - 1] == c))
			p++;
		i++;
	}
	return (p);
}

static void	ft_free_all(char **split, size_t num)
{
	size_t	index;

	index = 0;
	while (index < num)
		free(split[index++]);
	free(split);
}

static char	*ft_insert_word(char const *s, size_t st, size_t end)
{
	size_t	i;
	char	*word;

	i = 0;
	word = malloc(sizeof(char) * (end - st + 1));
	if (word == NULL)
		return (NULL);
	while (st < end)
		word[i++] = s[st++];
	word[i] = '\0';
	return (word);
}

static int	ft_fill_split(char const *s, char c, char **split)
{
	size_t	i;
	size_t	start;
	size_t	n;

	i = 0;
	n = 0;
	while (s[i])
	{
		while (s[i] == c)
			i++;
		start = i;
		while (s[i] && s[i] != c)
			i++;
		if (i > start)
		{
			split[n] = ft_insert_word(s, start, i);
			if (split[n] == NULL)
				return (n);
			n++;
		}
	}
	split[n] = NULL;
	return (-1);
}

char	**ft_split(char const *s, char c)
{
	char	**split;
	size_t	n_words;
	int		result;

	n_words = ft_count_words(s, c);
	split = malloc(sizeof(char *) * (n_words + 1));
	if (split == NULL)
		return (NULL);
	result = ft_fill_split(s, c, split);
	if (result != -1)
	{
		ft_free_all(split, result);
		return (NULL);
	}
	return (split);
}
