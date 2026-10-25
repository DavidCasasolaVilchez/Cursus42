#include "codexion.h"

int	create_coders(t_cx *cx)
{
	int		i;

	cx->coders = ft_calloc(cx->number_of_coders + 1, sizeof(t_coder *));
	if (cx->coders == NULL)
		return (0);
	i = 0;
	while (i < cx->number_of_coders)
	{
		cx->coders[i] = init_coder(i, cx);
		if (cx->coders[i] == NULL)
			return (0);
		cx->coders_created++;
		i++;
	}
	return (1);
}

static int	context_ended(t_cx *cx)
{
	int	end;

	pthread_mutex_lock(&cx->scheduler_mutex);
	end = cx->end;
	pthread_mutex_unlock(&cx->scheduler_mutex);
	return (end);
}

void	*start_coder(void *ptr)
{
	t_coder *coder;

	coder = (t_coder *)ptr;
	pthread_mutex_lock(&coder->cx->scheduler_mutex);
	while (coder->cx->threads_created == 0)
		pthread_cond_wait(&coder->cx->scheduler_changed,
			&coder->cx->scheduler_mutex);
	pthread_mutex_unlock(&coder->cx->scheduler_mutex);
	while (!context_ended(coder->cx))
	{
		try_take_dongles(coder);
		if (!take_dongles(coder, coder->cx))
			return (NULL);
		compile(coder);
		leave_dongles(coder, coder->cx);
		if (context_ended(coder->cx))
			break;
		debbug(coder);
		if (context_ended(coder->cx))
			break;
		refractor(coder);
	}
	return (NULL);
}

void	select_dongles(t_coder *c, int num_coders)
{
	if (c->id == 0)
		c->dright = 0;
	else
		c->dright = c->id - 1;
	if (c->id == (num_coders))
		c->dleft = 0;
	else
		c->dleft = c->id;
}

t_coder	*init_coder(int i, t_cx *cx)
{
	t_coder		*c;

	c = malloc(sizeof(t_coder));
	if (c == NULL)
		return (NULL);
	c->id = i + 1;
	c->num_compilations = 0;
	select_dongles(c, cx->number_of_coders);
	c->cx = cx;
	c->last_compile_start = malloc(sizeof(struct timeval));
	if (!c->last_compile_start)
		return (free(c), NULL);
	gettimeofday(c->last_compile_start, NULL);
	c->thread = malloc(sizeof(pthread_t));
	if (c->thread == NULL)
		return (free(c->last_compile_start), free(c), NULL);
	if (pthread_create(c->thread, NULL, start_coder, c) != 0)
		return (free(c->thread), free(c->last_compile_start), free(c), NULL);
	return (c);
}
