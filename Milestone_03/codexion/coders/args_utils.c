#include "codexion.h"

int	int_checker(char *input)
{
	int		n;

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