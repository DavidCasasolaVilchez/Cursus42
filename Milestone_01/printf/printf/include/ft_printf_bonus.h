/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_bonus.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dcasasol <dcasasol@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/16 16:50:26 by dcasasol          #+#    #+#             */
/*   Updated: 2026/09/29 11:43:47 by dcasasol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

# include "ft_libft.h"
# include <stdarg.h>

typedef struct s_context
{
	char	*flags;
	int		width;
	int		prec;
}	t_context;

typedef struct s_conversion
{
	char	indx;
	int		(*func)(t_context *cx, va_list a);
}	t_conversion;

int				ft_printf(char const *str, ...);

int				ft_slen(char *s);
int				ft_numlen_ulong(unsigned long num, int base);
int				ft_numlen_sgn(int num, int base);
int				ft_numlen_unsgn(unsigned int num, int base);
int				ft_numlen(int num, int base, int sgn);

int				ft_free_context(t_context *cx, int ret);
int				ft_end_list(va_list a, int p, t_conversion	*co);
int				ft_char_lector(char const *str, va_list a,
					t_conversion *cn, int *i);

void			ft_flag_sign(int num, t_context *cx);
int				ft_flag_zero(int num, t_context *cx, int tam, int sgn);
int				ft_flag_prec(char *s, t_context *cx);
int				ft_flag_space(int num, t_context *cx, int tam, int sgn);
int				ft_flag_alternative(int num, t_context *cx, int may);

int				ft_dt_flag(char *flags, char search);
int				ft_size_conversion(int num, t_context *cx, int base, int sgn);
void			ft_fill(int tam, char car);
void			ft_flag_putsign(int num, char plus);

void			ft_puthex(unsigned long mem, char *base, int pn);
void			ft_putnbr_hexadecimal(unsigned int num, char *base, int pn);
void			ft_putnbr_decimal(int d, int pn);
void			ft_putnbr_decimal_unsigned(unsigned int d, int pn);
int				ft_print_char(char c);

int				ft_putc(t_context *cx, va_list a);
int				ft_puts(t_context *cx, va_list a);
int				ft_putp(t_context *cx, va_list a);
int				ft_putd(t_context *cx, va_list a);
int				ft_puti(t_context *cx, va_list a);
int				ft_putu(t_context *cx, va_list a);
int				ft_putx(t_context *cx, va_list a);
int				ft_putxx(t_context *cx, va_list a);
int				ft_put_porcent(t_context *cx, va_list a);
int				ft_put_space_minus(t_context *cx, unsigned int x, int tam);

int				ft_evaluate_conversion(char const *str, int *ptr,
					va_list a, t_conversion *convers);
int				ft_count_flags(char const *str, int ptr);
int				ft_content_char(char *characters, char *flags, char search);
int				ft_get_context(char const *str, int ptr, t_context *cx);
t_conversion	*ft_create_conversions(void);

#endif
