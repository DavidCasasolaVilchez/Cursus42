#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int		fd;
	char	*line;
	int		i;
	int		a;

	a = 0;
	if (a)
	{
		fd = STDIN_FILENO;
		i = 1;
		while (i < 10)
		{
			line = get_next_line(fd);
			if (line == NULL)
				break ;
			printf("CALL %d:\n", i);
			printf("line = [%s]\n", line);
			printf("strlen = %d\n", ft_strlen(line));
			printf("--------------------\n");
			free(line);
			i++;
		}
	}
	else
	{
		fd = open("README.md", O_RDONLY);
		if (fd == -1)
		{
			perror("open");
			return (1);
		}
		i = 1;
		while (1)
		{
			line = get_next_line(fd);
			if (line == NULL)
				break ;
			printf("CALL %d:\n", i);
			printf("line = [%s]\n", line);
			printf("strlen = %d\n", ft_strlen(line));
			printf("--------------------\n");
			free(line);
			i++;
		}
		printf("Fin");
		close(fd);
	}
	return (0);
}
