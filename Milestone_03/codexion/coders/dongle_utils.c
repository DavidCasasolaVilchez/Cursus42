#include "codexion.h"

static int	request_is_first(t_heap *heap, int id)
{
	return (heap->size > 0 && heap->requests[0] != NULL
		&& heap->requests[0]->coder_id == id);
}

int	take_dongles(t_coder *coder, t_cx *cx)
{
	t_dongles	*left;
	t_dongles	*right;

	left = cx->dongles[coder->dleft];
	right = cx->dongles[coder->dright];
	pthread_mutex_lock(&cx->scheduler_mutex);
	while (!cx->end && (!request_is_first(left->heap, coder->id)
			|| !request_is_first(right->heap, coder->id)
			|| left->busy || right->busy))
		pthread_cond_wait(&cx->scheduler_changed, &cx->scheduler_mutex);
	if (cx->end)
		return (pthread_mutex_unlock(&cx->scheduler_mutex), 0);
	remove_from_heap(left);
	remove_from_heap(right);
	left->busy = 1;
	right->busy = 1;
	pthread_mutex_unlock(&cx->scheduler_mutex);
	displayer(cx, coder->id, TAKE_DONGLE);
	displayer(cx, coder->id, TAKE_DONGLE);
	return (1);
}

void	leave_dongles(t_coder *coder, t_cx *cx)
{
	t_dongles	*left;
	t_dongles	*right;

	left = cx->dongles[coder->dleft];
	right = cx->dongles[coder->dright];
	usleep((__useconds_t)cx->dongle_cooldown * 1000);
	pthread_mutex_lock(&cx->scheduler_mutex);
	left->busy = 0;
	right->busy = 0;
	pthread_cond_broadcast(&cx->scheduler_changed);
	pthread_mutex_unlock(&cx->scheduler_mutex);
}
