NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
CPPFLAGS = -Iinclude

LIBFT = include/libft.a

SRC = src/ft_printf.c \
      src/conversion_utils1.c \
      src/conversion_utils2.c \
      src/context_utils.c \
      src/flag_utils1.c \
      src/flag_utils2.c \
      src/len_utils.c \
      src/puts_utils.c \
	  src/memory_utils.c 

OBJ = $(SRC:.c=.o)

all: $(NAME)

bonus: all

$(NAME): $(OBJ)
	ar x $(LIBFT)
	ar rcs $(NAME) $(OBJ) *.o
	rm -f *.o

%.o: %.c
	$(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re