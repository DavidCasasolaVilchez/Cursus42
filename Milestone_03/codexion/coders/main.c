#include "codexion.h"

int		check_cx(t_cx *cx, char **argv)
{
	pthread_mutex_lock(&cx->scheduler_mutex);
	cx->number_of_coders = int_checker(argv[1]);
	cx->time_to_burnout = int_checker(argv[2]);
	cx->time_to_compile = int_checker(argv[3]);
	cx->time_to_debug = int_checker(argv[4]);
	cx->time_to_refactor = int_checker(argv[5]);
	cx->number_of_compiles_required = int_checker(argv[6]);
	cx->dongle_cooldown = int_checker(argv[7]);
	cx->scheduler = scheduler_checker(argv[8]);
	cx->end = 0;
	cx->threads_created = 0;
	if (cx->number_of_coders == -1 || cx->time_to_burnout == -1 ||
		cx->time_to_compile == -1 || cx->time_to_debug == -1 ||
		cx->time_to_refactor == -1 || cx->number_of_compiles_required == -1 ||
		cx->dongle_cooldown == -1 || cx->scheduler == ERROR
		|| cx->number_of_coders < 2)
		return (pthread_mutex_unlock(&cx->scheduler_mutex),
			printf("Invalid arguments\n"), 0);
	if (!create_dongles(cx) || !create_coders(cx))
		return (pthread_mutex_unlock(&cx->scheduler_mutex), 0);
	if (pthread_create(&cx->monitor, NULL, start_monitor, cx) != 0)
		return (pthread_mutex_unlock(&cx->scheduler_mutex), 0);
	cx->monitor_started = 1;
	return (pthread_mutex_unlock(&cx->scheduler_mutex), 1);
}

int		main(int argc, char **argv)
{
	t_cx			*cx;
	struct timeval	now;

	if (argc != 9)
		return (printf("Invalid arguments\n"), 1);
	cx = ft_calloc(1, sizeof(t_cx));
	if (!cx)
		return(1);
	gettimeofday(&now, NULL);
	cx->program_start = now.tv_sec * 1000000LL + now.tv_usec;
	pthread_mutex_init(&cx->display, NULL);
	pthread_mutex_init(&cx->scheduler_mutex, NULL);
	pthread_cond_init(&cx->scheduler_changed, NULL);
	if (check_cx(cx, argv) == 0)
		return (free_context(cx), 1);
	pthread_mutex_lock(&cx->scheduler_mutex);
	cx->threads_created = 1;
	pthread_mutex_unlock(&cx->scheduler_mutex);
	pthread_cond_broadcast(&cx->scheduler_changed);
	pthread_join(cx->monitor, NULL);
	pthread_mutex_lock(&cx->scheduler_mutex);
	cx->monitor_started = 0;
	pthread_mutex_unlock(&cx->scheduler_mutex);
	displayer_finish(cx);
	return (free_context(cx), 0);
}
