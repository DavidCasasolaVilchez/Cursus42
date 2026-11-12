/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   monitor_thread.c                                  :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/10/25 13:32:46 by dcasasol         #+#    #+#              */
/*   Updated: 2026/10/25 13:32:46 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	is_burned(t_cx *cx, struct timeval *now, int i)
{
	gettimeofday(now, NULL);
	pthread_mutex_lock(&cx->scheduler_mutex);
	if (cx->end)
	{
		pthread_mutex_unlock(&cx->scheduler_mutex);
		return (free(now), -1);
	}
	if ((now->tv_sec - cx->coders[i]->last_compile_start->tv_sec) * 1000000
		+now->tv_usec - cx->coders[i]->last_compile_start->tv_usec
		>= cx->time_to_burnout * 1000)
	{
		pthread_mutex_unlock(&cx->scheduler_mutex);
		displayer(cx, i + 1, BURNED);
		pthread_mutex_lock(&cx->scheduler_mutex);
		cx->end = 1;
		pthread_cond_broadcast(&cx->scheduler_changed);
		pthread_mutex_unlock(&cx->scheduler_mutex);
		return (free(now), -1);
	}
	pthread_mutex_unlock(&cx->scheduler_mutex);
	return (0);
}

void	*start_monitor(void *ptr)
{
	struct timeval	*now;
	t_cx			*cx;
	int				i;

	now = malloc(sizeof(struct timeval));
	cx = (t_cx *) ptr;
	if (!now)
		return (NULL);
	while (1)
	{
		i = 0;
		while (cx->coders[i])
		{
			if (is_burned(cx, now, i) == -1)
				return (NULL);
			i++;
		}
	}
	return (free(now), NULL);
}

void	create_monitor(t_cx *cx)
{
	pthread_create(&cx->monitor, NULL, start_monitor, cx);
}
