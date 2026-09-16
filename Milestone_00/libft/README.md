*Este proyecto ha sido creado como parte del currículo de 42 por dcasasol.*

# Libft

## Descripción

Libft es una biblioteca personal escrita en lenguaje `C`. El objetivo del proyecto es recrear funciones habituales de la biblioteca estándar de C y desarrollar funciones auxiliares reutilizables para futuros proyectos.

La biblioteca permite trabajar con:

- Caracteres.
- Cadenas de texto.
- Memoria.
- Asignación dinámica.
- Conversión de datos.
- Escritura en descriptores de archivo.
- Listas enlazadas.

### Descripción detallada de las funciones
#### Funciones de comprobación y conversión de caracteres
- ``ft_isalpha(int c):`` comprueba si `c` es una letra mayúscula o minúscula. Devuelve un valor distinto de cero si lo es y `0` en caso contrario.
- ``ft_isdigit(int c):`` comprueba si `c` representa un dígito entre `0` y `9`.
- ``ft_isalnum(int c):`` comprueba si `c` es una letra o un dígito.
- ``ft_isascii(int c):`` comprueba si `c` pertenece al conjunto de caracteres ASCII, entre `0` y `127`.
- ``ft_isprint(int c):`` comprueba si `c` es un carácter imprimible.
- ``ft_toupper(int c):`` convierte una letra minúscula en mayúscula. Los demás caracteres se devuelven sin cambios.
- ``ft_tolower(int c):`` convierte una letra mayúscula en minúscula. Los demás caracteres se devuelven sin cambios.

#### Funciones de memoria

- ``ft_memset(void *s,int c, size_t n):`` rellena los primeros `n` bytes de una zona de memoria con el valor indicado por `c`. Devuelve el puntero a la zona modificada.
- ``ft_bzero(void *s,size_t n):`` establece los primeros `n` bytes de una zona de memoria a cero.
- ``ft_memcpy(void *dest,const void *src, size_t n):`` copia `n` bytes desde `src` hasta `dest`. Las zonas de memoria no deben solaparse.
- ``ft_memmove(void *dest,const void *src, size_t n):`` copia `n` bytes entre dos zonas de memoria y permite que estas se solapen.
- ``ft_memchr(const void *s int c, size_t n):`` busca la primera aparición de c dentro de los primeros `n` bytes de `s`. Devuelve un puntero a la coincidencia o `NULL`.
- ``ft_memcmp(const void *s1 const void *s2, size_t n):`` compara los primeros n bytes de dos zonas de memoria y devuelve la diferencia entre el primer par de bytes distintos.
- ``ft_calloc(size_t nmemb,size_t size):`` reserva memoria para `nmemb` elementos de `size` bytes y la inicializa a cero. Devuelve `NULL` si la reserva falla o se produce un desbordamiento de tamaño.

#### Funciones de cadenas

- ``ft_strlen(const char *s: `` calcula y devuelve la longitud de una cadena, sin contar el carácter nulo final.
- ``ft_strlcpy(char *dst,const char *src, size_t size):`` copia `src` en `dst` limitando el número de caracteres copiados y garantizando, cuando es posible, la terminación nula.
- ``ft_strlcat(char *dst,const char *src, size_t size):`` concatena `src` al final de `dst` respetando el tamaño total del búfer y garantizando, cuando es posible, la terminación nula.
- ``ft_strchr(const char *s int c):`` busca la primera aparición de `c` en `s`. Devuelve un puntero al carácter encontrado o `NULL`.
- ``ft_strrchr(const char *s int c):`` busca la última aparición de `c` en `s`. Devuelve un puntero al carácter encontrado o `NULL`.
- ``ft_strncmp(const char *s1 const char *s2, size_t n):`` compara como máximo los primeros `n` caracteres de dos cadenas.
- ``ft_strnstr(const char *big const char *little, size_t len):`` busca `little` dentro de los primeros `len` caracteres de `big`.
- ``ft_strdup(const char *s: `` crea una copia de `s` reservando memoria dinámica para ella.
- ``ft_atoi(const char *nptr: `` convierte la parte numérica inicial de una cadena en un entero, gestionando espacios en blanco y los signos `+` y `-`.
- ``ft_substr(char const *s unsigned int start, size_t len):`` crea una nueva cadena comenzando en la posición `start` y con una longitud máxima de `len`.
- ``ft_strjoin(char const *s1 char const *s2):`` reserva memoria y devuelve una nueva cadena formada por la concatenación de `s1` y `s2`.
- ``ft_strtrim(char const *s1 char const *set):`` elimina del principio y del final de `s1` todos los caracteres que aparezcan en `set`.
- ``ft_split(char const *s char c):`` divide una cadena en un array de cadenas utilizando `c` como separador. El array termina con un puntero `NULL`.
- ``ft_itoa(int n):`` convierte un número entero en una cadena reservada dinámicamente.
- ``ft_strmapi(char const *s char (*f)(unsigned int, char)):`` aplica `f` a cada carácter de `s` y devuelve una nueva cadena con los resultados.
- ``ft_striteri(char *s,void (*f)(unsigned int, char *)):`` aplica `f` a cada carácter de `s`, permitiendo modificar la cadena original.

#### Funciones de escritura

- ``ft_putchar_fd(char c,int fd):`` escribe un carácter en el descriptor de archivo `fd`.
- ``ft_putstr_fd(char *s,int fd):`` escribe una cadena en el descriptor `fd`.
- ``ft_putendl_fd(char *s,int fd):`` escribe una cadena seguida de un salto de línea en `fd`.
- ``ft_putnbr_fd(int n,int fd):`` convierte un número entero a texto y lo escribe en el descriptor `fd`.

#### Funciones de listas enlazadas

La biblioteca utiliza la estructura `t_list`, formada por un puntero al contenido del nodo y otro al siguiente nodo:
El proyecto está implementado siguiendo las restricciones habituales de 42, utilizando únicamente las funciones permitidas y gestionando manualmente la memoria dinámica.
```bash
typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;
```
- ``ft_lstnew(void *content):`` reserva memoria y crea un nuevo nodo con el contenido indicado. El puntero `next` se inicializa a `NULL`.
- ``ft_lstadd_front(t_list **lst, t_list *new):`` añade `new` al principio de la lista y actualiza el puntero inicial.
- ``ft_lstsize(t_list *lst):`` recorre la lista y devuelve el número total de nodos.
- ``ft_lstlast(t_list *lst):`` recorre la lista y devuelve un puntero a su último nodo.
- ``ft_lstadd_back(t_list **lst, t_list *new):`` añade `new` al final de la lista.
- ``ft_lstdelone(t_list *lst, void (*del)(void *)):`` aplica `del` al contenido de un nodo y libera el nodo.
- ``ft_lstclear(t_list **lst, void (*del)(void *)):`` elimina todos los nodos de la lista, libera sus contenidos mediante `del` y establece la lista a `NULL`.
- ``ft_lstiter(t_list *lst, void (*f)(void *)):`` recorre la lista y aplica `f` al contenido de cada nodo.
- ``ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *)):`` crea una nueva lista aplicando `f` al contenido de cada nodo. Si falla una reserva de memoria, utiliza `del` para liberar los elementos ya creados.

## Instrucciones

### Compilación

Para compilar la biblioteca, ejecuta:

```bash
make
```
Este comando genera la biblioteca estática `libft.a`.

### Limpieza
Para eliminar los archivos objeto:
```bash
make clean
```
Para eliminar los archivos objeto y la biblioteca compilada:
```bash
make fclean
```
Para limpiar y recompilar todo el proyecto:
```bash
make re
```

### Integración en un proyecto
Incluye la cabecera de la biblioteca en el archivo C:
```bash
#include "- ``ft_libft.h"
```
Compila tu programa enlazándolo con `libft.a`:
```bash
cc -Wall -Wextra -Werror -Iinclude main.c -L. -lft -o ejec
```

### Ejecución
Ejecuta el programa compilado con:
```bash
./ejec
```
## Recursos
- Manuales de las funciones estándar mediante el comando `man`.
- Subject oficial del proyecto `Libft` de 42.

### Uso de inteligencia artificial
La inteligencia artificial se ha utilizado como herramienta de apoyo durante el desarrollo y la documentación del proyecto para:
- Consultar el funcionamiento esperado de algunas funciones estándar de C.
- Revisar posibles puntos de inflexión de algunas funciones.
- Organizar y redactar este archivo README.

La inteligencia artificial se ha utilizado como apoyo, pero la implementación y revisión final del código corresponden al autor del proyecto.