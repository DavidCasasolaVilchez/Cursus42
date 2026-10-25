#include "codexion.h"

void	compile(t_coder *cod)
{
	displayer(cod->cx, cod->id, COMPILE);
	pthread_mutex_lock(&cod->cx->scheduler_mutex);
	gettimeofday(cod->last_compile_start, NULL);
	pthread_mutex_unlock(&cod->cx->scheduler_mutex);
	usleep((__useconds_t)cod->cx->time_to_compile * 1000);
	pthread_mutex_lock(&cod->cx->scheduler_mutex);
	cod->num_compilations++;
	pthread_mutex_unlock(&cod->cx->scheduler_mutex);
	pthread_mutex_lock(&cod->cx->display);
	pthread_mutex_unlock(&cod->cx->display);
	everyone_compile(cod->cx);
}

void	everyone_compile(t_cx *cx)
{
	int		i;
	pthread_mutex_lock(&cx->scheduler_mutex);
	i = 0;
	while (i < cx->number_of_coders
		&& cx->coders[i]->num_compilations
			>= cx->number_of_compiles_required)
	{
		i++;
	}
	if (i == cx->number_of_coders)
	{
		cx->end = 1;
		pthread_cond_broadcast(&cx->scheduler_changed);
	}
	pthread_mutex_unlock(&cx->scheduler_mutex);
}

void	debbug(t_coder *cod)
{
	displayer(cod->cx, cod->id, DEBUG);
	usleep((__useconds_t)cod->cx->time_to_debug * 1000);
}

void	refractor(t_coder *cod)
{
	displayer(cod->cx, cod->id, REFACTOR);
	usleep((__useconds_t)cod->cx->time_to_refactor * 1000);
}

void	try_take_dongles(t_coder *cod)
{
	t_request		*right_req;
	t_request		*left_req;
	struct timeval	*now;

	now = malloc(sizeof(struct timeval));
	right_req = malloc(sizeof(t_request));
	left_req = malloc(sizeof(t_request));
	if (!right_req || !left_req || !now)
		return free(right_req), free(left_req), free(now);
	gettimeofday(now, NULL);
	right_req->coder_id = cod->id;
	right_req->arrival = now->tv_sec * 1000000LL + now->tv_usec;
	right_req->deadline = cod->last_compile_start->tv_sec * 1000000LL
		+ cod->last_compile_start->tv_usec
		+ cod->cx->time_to_burnout * 1000;
	*left_req = *right_req;
	pthread_mutex_lock(&cod->cx->scheduler_mutex);
	cod->cx->dongles[cod->dright]->heap->requests[
		cod->cx->dongles[cod->dright]->heap->size++] = right_req;
	cod->cx->dongles[cod->dleft]->heap->requests[
		cod->cx->dongles[cod->dleft]->heap->size++] = left_req;
	reorder_heap(cod->cx->dongles[cod->dright]);
	reorder_heap(cod->cx->dongles[cod->dleft]);
	pthread_cond_broadcast(&cod->cx->scheduler_changed);
	pthread_mutex_unlock(&cod->cx->scheduler_mutex);
	free(now);
}
