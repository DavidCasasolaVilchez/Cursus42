NAME = libftprintf.a
BNAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
CPPFLAGS = -Iinclude

LIBFT = include/libft.a

SRC = src/ft_printf.c \
      src/context_utils.c \
      src/conversion_utils1.c \
      src/conversion_utils2.c \
      src/flag_utils1.c \
      src/flag_utils2.c \
      src/len_utils.c \
      src/memory_utils.c \
      src/puts_utils.c \

BSRC = src/ft_printf_bonus.c \
      src/context_utils_bonus.c \
      src/conversion_utils1_bonus.c \
      src/conversion_utils2_bonus.c \
      src/flag_utils1_bonus.c \
      src/flag_utils2_bonus.c \
      src/len_utils_bonus.c \
      src/memory_utils_bonus.c \
      src/puts_utils_bonus.c \

OBJ = $(SRC:.c=.o)
BOBJ = $(BSRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	ar x $(LIBFT)
	ar rcs $(NAME) $(OBJ) *.o
	rm -f *.o

%.o: %.c
	$(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $@

bonus: $(BNAME)

$(BNAME): $(BOBJ)
	ar x $(LIBFT)
	ar rcs $(BNAME) $(BOBJ) *.o
	rm -f *.o

clean:
	rm -f $(OBJ) $(BOBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re