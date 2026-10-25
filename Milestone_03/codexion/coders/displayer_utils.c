#include "codexion.h"

void	displayer(t_cx *cx, int id, t_action action)
{
	struct timeval	now;
	long long		mom;

	pthread_mutex_lock(&cx->display);
	gettimeofday(&now, NULL);
	mom = now.tv_sec * 1000000LL + now.tv_usec - cx->program_start;
	if (action == TAKE_DONGLE)
		printf("\033[35m%lld %d has taken a dongle\n", (mom / 1000), id);
	else if (action == COMPILE)
		printf("\033[32m%lld %d is compiling\n", (mom / 1000), id);
	else if (action == DEBUG)
		printf("\033[33m%lld %d is debugging\n", (mom / 1000), id);
	else if (action == REFACTOR)
		printf("\033[34m%lld %d is refactoring\n", (mom / 1000), id);
	else if (action == BURNED)
		printf("\033[31m%lld %d burned out\n", (mom / 1000), id);
	pthread_mutex_unlock(&cx->display);
}

void	displayer_finish(t_cx *cx)
{
	int	i;
	int	b;
	
	b = 0;
	i = -1;
	pthread_mutex_lock(&cx->display);
	printf("\033[95m\n\nResults:\n");
	while (++i < cx->coders_created)
	{
		if (cx->coders[i]->num_compilations <
			cx->number_of_compiles_required)
			b = 1;
		printf("\tThe coder %d has compiled %d times\n",
			cx->coders[i]->id, cx->coders[i]->num_compilations);
	}
	if (b == 0)
		printf("\nThe program has ended because all the coders have performed"
			" %d compilations\n", cx->number_of_compiles_required);
	else
		printf("\nThe program has ended because a coder has burned out\n");
	pthread_mutex_unlock(&cx->display);

}
