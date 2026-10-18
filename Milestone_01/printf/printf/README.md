*Este proyecto ha sido creado como parte del currículo de 42 por dcasasol.*

# ft_printf

## Descripción

`ft_printf` es una implementación propia de la función variádica `printf` de la biblioteca estándar de C. El objetivo del proyecto es reproducir su comportamiento para un conjunto definido de conversiones, gestionar argumentos de tipos diferentes y devolver el número de caracteres escritos.

La implementación está escrita en C y se construye como la biblioteca estática `libftprintf.a`. El código está dividido entre el análisis del formato, la creación del contexto de cada conversión, el cálculo de longitudes, el formateo de valores y las funciones de salida.

Se incluyen dos variantes:

- **Mandatory:** conversiones `c`, `s`, `p`, `d`, `i`, `u`, `x`, `X` y `%`.
- **Bonus:** añade las flags `-`, `0`, `.`, `#`, `+` y espacio, junto con el ancho mínimo y la precisión según las reglas de `printf`.

## Características

- Acepta un número variable de argumentos mediante `stdarg.h`.
- Devuelve el número de caracteres escritos o `-1` ante un error de memoria o formato no válido.
- Gestiona caracteres, cadenas, punteros, enteros con y sin signo y números hexadecimales.
- Admite el formato de punteros en hexadecimal y las variantes hexadecimal en minúsculas y mayúsculas.
- Aplica ancho, precisión, alineación, relleno con ceros, prefijos alternativos y signos en la versión bonus.
- Libera el contexto y las estructuras temporales creadas durante el formateo.

## Estructura del proyecto

```text
printf/
├── Makefile
├── include/
│   ├── ft_libft.h
│   ├── ft_printf.h
│   └── ft_printf_bonus.h
├── src/
│   ├── ft_printf.c
│   ├── ft_printf_bonus.c
│   ├── context_utils*.c
│   ├── conversion_utils*.c
│   ├── flag_utils*.c
│   ├── len_utils*.c
│   ├── memory_utils*.c
│   └── puts_utils*.c
└── README.md
```

## Instrucciones

### Requisitos

- Un compilador compatible con C, por ejemplo `cc` o `clang`.
- `make`.
- Una implementación de `libft` compilada como `libft.a` en `include/libft.a`. El `Makefile` la extrae e incorpora a `libftprintf.a`.
- Opcionalmente, Valgrind para las comprobaciones de fugas y accesos inválidos.

### Compilación

Desde esta carpeta, que es la raíz del repositorio evaluado:

```bash
make
```

La biblioteca generada queda en:

```text
libftprintf.a
```

Para compilar un programa propio que use la biblioteca:

```bash
cc main.c -Iinclude -L. -lftprintf -o main
./main
```

El programa debe incluir una de las cabeceras públicas:

```c
#include "ft_printf.h"
```

Para construir la variante bonus:

```bash
make bonus
```

Las variantes obligatoria y bonus exponen la misma función `ft_printf`; por ello, deben compilarse y enlazarse por separado, no mezclarse en el mismo binario.

### Limpieza

```bash
make clean   # elimina los objetos temporales
make fclean  # elimina objetos y libftprintf.a
make re      # recompila desde cero
```


## Algoritmo y estructuras de datos

### Algoritmo de análisis

El formato se procesa en una única pasada, de izquierda a derecha, con complejidad temporal lineal respecto a la longitud de la cadena: $O(n)$. `ft_printf` recorre cada carácter y acumula el número de caracteres producido por cada fragmento.

Cuando encuentra `%`, el analizador avanza por las siguientes partes de la conversión:

1. Flags (`-`, `0`, `#`, `+` y espacio).
2. Ancho mínimo, formado por uno o más dígitos.
3. Precisión, introducida por `.` y seguida de sus dígitos.
4. Especificador de conversión (`c`, `s`, `p`, `d`, `i`, `u`, `x`, `X` o `%`).

Una vez obtenido el contexto, se aplica la función de salida correspondiente. Las longitudes numéricas se calculan antes de imprimir para poder decidir el relleno, el signo, el prefijo hexadecimal y la posición del valor dentro del ancho solicitado.

### Justificación de las estructuras

Cada conversión se representa con `t_context`, que agrupa sus flags, ancho y precisión. Esta estructura evita pasar varios parámetros independientes entre las funciones de formateo y permite que cada conversión trabaje con una configuración aislada.

El despachado se realiza con una tabla de estructuras `t_conversion`. Cada entrada contiene el carácter de conversión y un puntero a la función que lo procesa. Esta elección evita una cadena extensa de condiciones para cada especificador, facilita mantener separadas las responsabilidades y permite asociar directamente `c`, `s`, `p`, `d`, `i`, `u`, `x`, `X` y `%` con sus formateadores.

Las flags se almacenan en una cadena dinámica dentro del contexto. Se eliminan duplicados al analizar la conversión y se consultan cuando cada formateador decide el signo, el relleno o la alineación. Para números se usan funciones de cálculo de longitud y bases explícitas, lo que permite obtener el tamaño necesario sin convertir previamente todo el valor en una cadena.

La solución no necesita una estructura enlazada ni una tabla de tamaño proporcional al texto completo: el estado de una conversión solo vive durante su procesamiento. Esta decisión mantiene el consumo de memoria auxiliar acotado al contexto y a la tabla de conversiones, es decir, $O(1)$ respecto al tamaño del formato, aparte de las cadenas y buffers temporales necesarios para una salida concreta.

## Recursos

- [Man page de `printf(3)`](https://man7.org/linux/man-pages/man3/printf.3.html): especificadores, flags, ancho, precisión y valor de retorno.
- [Man page de `stdarg(3)`](https://man7.org/linux/man-pages/man3/stdarg.3.html): uso de `va_list`, `va_start`, `va_arg` y `va_end`.
- [Referencia de `printf` en cppreference](https://en.cppreference.com/w/c/io/fprintf): descripción del formato y reglas de las conversiones de la biblioteca estándar.
- [Documentación de GNU C sobre argumentos variádicos](https://gcc.gnu.org/onlinedocs/gcc/Variadic-Functions.html): fundamentos de funciones con un número variable de argumentos.
- `tester/README.md` y `tester2/README.md`: instrucciones locales de los comprobadores incluidos en este repositorio.

### Uso de inteligencia artificial

La IA se ha utilizado para preparar y revisar este README: organizar la información para personas no familiarizadas con el proyecto, resumir el flujo de compilación, documentar la interfaz y explicar el algoritmo y las estructuras de datos a partir del código existente. También se ha empleado como apoyo de revisión para comprobar que las instrucciones distinguen la versión mandatory de la bonus y reflejan el prerrequisito de `libft.a`.

La IA no sustituye la validación del código: la compilación, la ejecución de los testers y la comprobación de fugas deben realizarse en el entorno local del proyecto.
