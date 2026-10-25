#ifndef CODEXION_H
# define CODEXION_H

# define _XOPEN_SOURCE 500

#include <pthread.h>
#include <sys/time.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

typedef enum e_sch
{
	EDF,
	FIFO,
	ERROR
}	t_sch;

typedef enum e_action
{
	TAKE_DONGLE,
	COMPILE,
	DEBUG,
	REFACTOR,
	BURNED,
	NONE
}	t_action;

typedef struct	s_cx t_cx;

typedef struct	s_coder
{
	int				id;
	t_cx			*cx;
	int				dleft;
	int				dright;
	pthread_t		*thread;
	int				num_compilations;
	struct timeval	*last_compile_start;
}	t_coder;

typedef struct s_request
{
	long long	arrival;
	long long	deadline;
	int			coder_id;
}	t_request;

typedef struct s_heap
{
	t_request	**requests;
	int			size;
	int			capacity;
}	t_heap;

typedef struct	s_dongles
{
	t_sch			sch;
	t_heap			*heap;
	pthread_mutex_t	mutex;
	int				busy;
}	t_dongles;

struct	s_cx
{
	int				number_of_compiles_required;
	int				number_of_coders;
	long long		time_to_refactor;
	long long		time_to_burnout;
	long long		time_to_compile;
	long long		dongle_cooldown;
	long long		time_to_debug;
	long long		program_start;
	t_dongles		**dongles;
	t_sch			scheduler;
	t_coder			**coders;
	pthread_t		monitor;
	pthread_mutex_t	display;
	pthread_mutex_t	scheduler_mutex;
	pthread_cond_t	scheduler_changed;
	int				end;
	int				dongles_created;
	int				coders_created;
	int				monitor_started;
	int				threads_created;
};

/* ### CHECKERS ### */
t_sch		scheduler_checker(char *input);
void		everyone_compile(t_cx *cx);
int			int_checker(char *input);

/* ### ACTIONS ### */
int			take_dongles(t_coder *coder, t_cx *cx);
void		compile(t_coder *cod);
void		leave_dongles(t_coder *coder, t_cx *cx);
void		refractor(t_coder *cod);
void		debbug(t_coder *cod);

/* ### CODE THREAD MANAGE ### */
t_coder		*init_coder(int i, t_cx *cx);
void		*start_coder(void *coder);
int			create_coders(t_cx *cx);

/* ### DONGLE THREAD MANAGE ### */
void		try_take_dongles(t_coder *cod);
int			create_dongles(t_cx *cx);

/* ### DONGLE THREAD MANAGE ### */
void		create_monitor(t_cx *cx);
void		*start_monitor(void *ptr);

/* ### HEAP MANAGE ### */
void		remove_from_heap(t_dongles *dongle);
void		reorder_heap(t_dongles *dongle);

/* ### CLEANER ### */
void		free_context(t_cx *cx);
void		*ft_calloc(unsigned int nmemb, unsigned int size);

/* ### DISPLAYER ### */
void		displayer(t_cx *cx, int id, t_action action);
void		displayer_finish(t_cx *cx);

#endif
