#include "codexion.h"

int	create_dongle(t_dongles **new, t_sch scheduler, int ncods)
{
	t_dongles	*dongle;

	dongle = malloc(sizeof(t_dongles));
	if (dongle == NULL)
		return (0);
	if (pthread_mutex_init(&dongle->mutex, NULL) != 0)
		return (free(new), 0);
	dongle->sch = scheduler;
	dongle->heap = malloc(sizeof(t_heap));
	if (dongle->heap == NULL)
		return (free(new), 0);
	dongle->heap->capacity = ncods;
	dongle->heap->size = 0;
	dongle->heap->requests =
		ft_calloc(dongle->heap->capacity, sizeof(t_request *));
	if (dongle->heap->requests == NULL)
		return (free(new), free(dongle->heap), 0);
	dongle->busy = 0;
	*new = dongle;
	return (1);
}

int	create_dongles(t_cx *cx)
{
	int		i;

	cx->dongles = ft_calloc(cx->number_of_coders + 1, sizeof(t_dongles *));
	if (cx->dongles == NULL)
		return (0);
	i = 0;
	while (i < cx->number_of_coders)
	{
		if (create_dongle(&cx->dongles[i],
			cx->scheduler, cx->number_of_coders) == 0)
			return (0);
		cx->dongles_created++;
		i++;
	}
	return (1);
}
