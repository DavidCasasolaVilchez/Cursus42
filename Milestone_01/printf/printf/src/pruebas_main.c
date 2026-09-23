/* ************************************************************************** */
/*                                                                            */
/*                                                       :::      ::::::::    */
/*   main.c                                            :+:      :+:    :+:    */
/*                                                   +:+ +:+         +:+      */
/*   By: dcasasol <dcasasol@student.42malaga.com>  #+#  +:+       +#+         */
/*                                               +#+#+#+#+#+   +#+            */
/*   Created: 2026/09/16 16:49:40 by dcasasol         #+#    #+#              */
/*   Updated: 2026/09/16 16:49:40 by dcasasol        ###   ########.fr        */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"
#include <limits.h>
#include <stdio.h>

int	main(void)
{
	int	len_original;
	int	len_tuya;
	/*int	variable;

	variable = 42;
	printf("========================================\n");
	printf("        TESTS BASICOS\n");
	printf("========================================\n\n");
	printf("--- TEST 1: Texto simple ---\n");
	len_original = printf("Original: Hola Mundo\n");
	len_tuya = ft_printf("Tuya:     Hola Mundo\n");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 2: %%c ---\n");
	len_original = printf("Original: [%c]\n", 'A');
	len_tuya = ft_printf("Tuya:     [%c]\n", 'A');
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 3: %%s ---\n");
	len_original = printf("Original: [%s]\n", "42 Malaga");
	len_tuya = ft_printf("Tuya:     [%s]\n", "42 Malaga");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 4: %%d / %%i ---\n");
	len_original = printf("Original: [%d] [%i]\n", 42, -2147483648);
	len_tuya = ft_printf("Tuya:     [%d] [%i]\n", 42, -2147483648);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 5: %%%% ---\n");
	len_original = printf("Original: [100%%]\n");
	len_tuya = ft_printf("Tuya:     [100%%]\n");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 6: %%x / %%X ---\n");
	len_original = printf("Original: [%x] [%X]\n", 255, 255);
	len_tuya = ft_printf("Tuya:     [%x] [%X]\n", 255, 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 7: %%p ---\n");
	len_original = printf("Original: [%p]\n", &variable);
	len_tuya = ft_printf("Tuya:     [%p]\n", &variable);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        TESTS DE WIDTH\n");
	printf("========================================\n\n");
	printf("--- TEST 8: width con %%d ---\n");
	len_original = printf("Original: [%10d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%10d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 9: width con %%s ---\n");
	len_original = printf("Original: [%15s]\n", "Hola");
	len_tuya = ft_printf("Tuya:     [%15s]\n", "Hola");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 10: width con %%c ---\n");
	len_original = printf("Original: [%10c]\n", 'A');
	len_tuya = ft_printf("Tuya:     [%10c]\n", 'A');
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        FLAG '-'\n");
	printf("========================================\n\n");
	printf("--- TEST 11: %- ---\n");
	len_original = printf("Original: [%-10d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%-10d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%-10s]\n", "Hola");
	len_tuya = ft_printf("Tuya:     [%-10s]\n", "Hola");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        FLAG '0'\n");
	printf("========================================\n\n");
	printf("--- TEST 12: %0 ---\n");
	len_original = printf("Original: [%010d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%010d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%010x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%010x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        FLAG '+'\n");
	printf("========================================\n\n");
	printf("--- TEST 13: %+ ---\n");
	len_original = printf("Original: [%+d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%+d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%+d]\n", -42);
	len_tuya = ft_printf("Tuya:     [%+d]\n", -42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%+10d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%+10d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        FLAG ' '\n");
	printf("========================================\n\n");
	printf("--- TEST 14: espacio ---\n");
	len_original = printf("Original: [% d]\n", 42);
	len_tuya = ft_printf("Tuya:     [% d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [% 10d]\n", 42);
	len_tuya = ft_printf("Tuya:     [% 10d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        FLAG '#'\n");
	printf("========================================\n\n");
	printf("--- TEST 15: # con hexadecimal ---\n");
	len_original = printf("Original: [%#x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%#x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%#X]\n", 255);
	len_tuya = ft_printf("Tuya:     [%#X]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	len_original = printf("Original: [%#10x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%#10x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        PRECISION '.'\n");
	printf("========================================\n\n");
	printf("--- TEST 16: precisión con %%d ---\n");
	len_original = printf("Original: [%.5d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%.5d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 17: precisión con %%u ---\n");
	len_original = printf("Original: [%.8u]\n", 42);
	len_tuya = ft_printf("Tuya:     [%.8u]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 18: precisión con %%x ---\n");
	len_original = printf("Original: [%.8x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%.8x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 19: precisión con %%s ---\n");
	len_original = printf("Original: [%.5s]\n", "Hola Mundo");
	len_tuya = ft_printf("Tuya:     [%.5s]\n", "Hola Mundo");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("        COMBINACIONES\n");
	printf("========================================\n\n");
	printf("--- TEST 20: - + width ---\n");
	len_original = printf("Original: [%-+10d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%-+10d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 21: 0 + width ---\n");
	len_original = printf("Original: [%+010d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%+010d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 22: # + width ---\n");
	len_original = printf("Original: [%#10x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%#10x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 23: # + 0 + width ---\n");
	len_original = printf("Original: [%#010x]\n", 255);
	len_tuya = ft_printf("Tuya:     [%#010x]\n", 255);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 24: + + precision ---\n");
	len_original = printf("Original: [%+.5d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%+.5d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 25: width + precision ---\n");
	len_original = printf("Original: [%10.5d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%10.5d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 26: 0 + precision ---\n");
	len_original = printf("Original: [%010.5d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%010.5d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("--- TEST 27: espacio + width + precision ---\n");
	len_original = printf("Original: [% 10.5d]\n", 42);
	len_tuya = ft_printf("Tuya:     [% 10.5d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n");
	printf("========================================\n");
	printf("        TESTS DE CASOS LIMITE\n");
	printf("========================================\n");
	printf("\n--- TEST 28: precisión 0 con %%d y 0 ---\n");
	len_original = printf("Original: [%.0d]\n", 0);
	len_tuya = ft_printf("Tuya:     [%.0d]\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 29: + y 0 con width ---\n");
	len_original = printf("Original: [%+05d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%+05d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 30: 0 + width + precision ---\n");
	len_original = printf("Original: [%05.3d]\n", 42);
	len_tuya = ft_printf("Tuya:     [%05.3d]\n", 42);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 31: # con hexadecimal 0 ---\n");
	len_original = printf("Original: [%#x]\n", 0);
	len_tuya = ft_printf("Tuya:     [%#x]\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 32: precisión 0 con hexadecimal 0 ---\n");
	len_original = printf("Original: [%.0x]\n", 0);
	len_tuya = ft_printf("Tuya:     [%.0x]\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 33: width + precisión 0 con 0 ---\n");
	len_original = printf("Original: [%10.0d]\n", 0);
	len_tuya = ft_printf("Tuya:     [%10.0d]\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 34: precisión con %%s ---\n");
	len_original = printf("Original: [%.5s]\n", "Hola");
	len_tuya = ft_printf("Tuya:     [%.5s]\n", "Hola");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("\n--- TEST 35: - + precisión con %%s ---\n");
	len_original = printf("Original: [%-10.5s]\n", "Hola mundo");
	len_tuya = ft_printf("Tuya:     [%-10.5s]\n", "Hola mundo");
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);
	printf("========================================\n");
	printf("              FIN TESTS\n");
	printf("========================================\n");
	return (0);*/

	//
	len_original = printf("printf:    %%#x[1] -> %#x\n", 0);
	len_tuya = ft_printf("ft_printf: %%#x[1] -> %#x\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);

	/*len_original = printf("printf:    %%#x[1] -> %#x\n", LONG_MIN);
	len_tuya = ft_printf("ft_printf: %%#x[1] -> %#x\n", LONG_MIN);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);

	len_original = printf("printf:    %%#x[1] -> %#x\n", 0);
	len_tuya = ft_printf("ft_printf: %%#x[1] -> %#x\n", 0);
	printf("Retorno -> Original: %d | Tuyo: %d\n\n", len_original, len_tuya);*/

}
