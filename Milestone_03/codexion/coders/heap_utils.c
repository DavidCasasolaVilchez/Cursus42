#include "codexion.h"

void	reorder_heap(t_dongles *dongle)
{
	t_request	*aux;
	int			i;
	int			j;

	i = 0;
	while (i < dongle->heap->size)
	{
		j = i + 1;
		while (j < dongle->heap->size)
		{
			if ((dongle->sch == EDF
					&& dongle->heap->requests[j]->deadline
					< dongle->heap->requests[i]->deadline)
				|| (dongle->sch == FIFO
					&& dongle->heap->requests[j]->arrival
					< dongle->heap->requests[i]->arrival))
			{
				aux = dongle->heap->requests[i];
				dongle->heap->requests[i] = dongle->heap->requests[j];
				dongle->heap->requests[j] = aux;
			}
			j++;
		}
		i++;
	}
}

void	remove_from_heap(t_dongles *dongle)
{
	int	i;

	if (dongle->heap->size == 0)
		return ;
	free(dongle->heap->requests[0]);
	i = 1;
	while (i < dongle->heap->size)
	{
		dongle->heap->requests[i - 1] = dongle->heap->requests[i];
		i++;
	}
	dongle->heap->requests[dongle->heap->size - 1] = NULL;
	dongle->heap->size--;
}
