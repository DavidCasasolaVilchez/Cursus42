#include "codexion.h"

static void	free_coder(t_coder **c, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (c[i]->last_compile_start != NULL)
			free(c[i]->last_compile_start);
		if (c[i]->thread != NULL)
			free(c[i]->thread);
		c[i]->cx = NULL;
		if (c[i] != NULL)
			free(c[i]);
		i++;
	}
	free(c);
}

static void	finish_threads(t_dongles **d, int dsize, t_coder **c, int csize)
{
	int	i;

	i = 0;
	while (i < csize)
		pthread_join(*c[i++]->thread, NULL);
	i = 0;
	while (i < dsize)
		pthread_mutex_destroy(&d[i++]->mutex);
}

static void	free_heap(t_heap *h)
{
	while (h->size > 0)
	{
		if (h->requests[h->size - 1] != NULL)
			free(h->requests[h->size - 1]);
		h->size--;
	}
	free(h->requests);
	if (h != NULL)
		free(h);
}

static void	free_dongles(t_dongles **d, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (d[i]->heap != NULL)
			free_heap(d[i]->heap);
		if (d != NULL)
			free(d[i]);
		i++;
	}
	free(d);
}

void	free_context(t_cx *cx)
{
	pthread_mutex_lock(&cx->scheduler_mutex);
	cx->end = 1;
	pthread_cond_broadcast(&cx->scheduler_changed);
	pthread_mutex_unlock(&cx->scheduler_mutex);
	if (cx->monitor_started)
		pthread_join(cx->monitor, NULL);
	finish_threads(cx->dongles, cx->dongles_created,
		cx->coders, cx->coders_created);
	free_coder(cx->coders, cx->coders_created);
	free_dongles(cx->dongles, cx->dongles_created);
	pthread_mutex_destroy(&cx->display);
	pthread_cond_destroy(&cx->scheduler_changed);
	pthread_mutex_destroy(&cx->scheduler_mutex);
	if (cx != NULL)
		free(cx);
}
