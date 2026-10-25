NAME		= codexion

CC			= cc
CFLAGS		= -Wall -Wextra -Werror -g
THFLAG		= -pthread
VERSIONFLAG	= -std=c89
RM			= rm -f

SRC_DIR		= coders
OBJ_DIR		= obj

SRC			= main.c \
			  args_utils.c \
			  coder_thread_utils.c \
			  coder_thread.c \
			  displayer_utils.c \
			  dongle_utils.c \
			  dongle_utils2.c \
			  exit_utils.c \
			  heap_utils.c \
			  memory_utils.c \
			  monitor_thread.c

OBJ			= $(addprefix $(OBJ_DIR)/, $(SRC:.c=.o))

WC			= wc -l
LOGFIFO		= medium-fifo.log
LOGEDF		= medium-edf.log

ARGS_EASY	= 250 1200 100 300 200 4 100 edf
ARGS_LEASY	= 200 1000 1 1 1 1 1 edf
ARGS_MEDE	= 250 1200 100 300 200 4 100 edf
ARGS_MEDF	= 250 1200 100 300 200 4 100 fifo
ARGS_EDFTB	= 8 5000 100 100 100 3 50 edf

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(VERSIONFLAG) $(CFLAGS) $(THFLAG) $(OBJ) -o $(NAME)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(SRC_DIR)/codexion.h | $(OBJ_DIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

clean:
	$(RM) -r $(OBJ_DIR)

fclean: clean
	$(RM) $(NAME)

re: fclean all

run: re
	./$(NAME) 8 12000 1000 3000 2000 4 1000 edf
	
run_easy: re
	./$(NAME) $(ARGS_EASY)
	
run_lesseasy: re
	./$(NAME) $(ARGS_LEASY)
	
run_medium: re
	./$(NAME) $(ARGS_MEDE) > $(LOGEDF)
	./$(NAME) $(ARGS_MEDF) > $(LOGFIFO)
	$(WC) $(LOGFIFO) $(LOGEDF)
	
run_edf_tiebreaker: re
	./$(NAME) $(ARGS_EDFTB)

.PHONY: all clean fclean re run
