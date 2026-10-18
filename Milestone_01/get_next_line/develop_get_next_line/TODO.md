# get_next_line

Hay que asegurarse de que la función se comporta adecuadamente cuando lea de un archivo y cuando lea de `stdin`.

## Requisitos

- La línea devuelta debe terminar con `\n`.
- La única excepción es cuando se ha llegado al final del archivo y este no termina con un `\n`.
- El archivo de cabecera `get_next_line.h` debe incluir, como mínimo, el prototipo de la función `get_next_line`.
- Se pueden añadir todas las funciones de ayuda necesarias en el archivo `get_next_line_utils.c`.
- El programa debe compilar con el indicador `-D BUFFER_SIZE=n`.

### `BUFFER_SIZE`

Este indicador determina el tamaño del buffer utilizado por las lecturas de `read()` en `get_next_line()`. El parámetro será modificado por las personas evaluadoras y por Moulinette para probar el programa.

El programa se compilará de la siguiente forma, utilizando como ejemplo un tamaño de buffer de `42`:

```sh
cc -Wall -Werror -Wextra -D BUFFER_SIZE=42 <archivos>.c
```

Se considera que `get_next_line()` tiene un comportamiento indeterminado en los siguientes casos:

- El archivo al que apunta el descriptor de archivo ha cambiado desde la última llamada, siempre que `read()` no haya llegado al final del archivo.
- Lo que se lee es un archivo binario.

No obstante, es posible implementar alguna manera lógica de sortear el problema de los archivos binarios, si se desea.

## Lectura

La función debe leer lo menos posible cada vez que se llame a `get_next_line()`. Si encuentra un salto de línea, debe devolver la línea actual. No se debe leer el archivo entero para después procesar cada línea.

La implementación debe funcionar correctamente con los siguientes valores de `BUFFER_SIZE`:

- `9999`
- `1`
- `10000000`

## Prohibiciones

- No se permite el uso de `libft` en este proyecto.
- Se prohíbe el uso de `lseek`.
- Se prohíbe el uso de variables globales.

## Bonus

### Una única variable estática

Desarrollar `get_next_line()` utilizando una sola variable estática.

### Múltiples descriptores de archivo

`get_next_line()` debe poder gestionar múltiples descriptores de archivo simultáneamente.

Por ejemplo, si hay tres descriptores disponibles para lectura (`3`, `4` y `5`), se debe poder leer de un descriptor distinto en cada llamada sin perder el seguimiento del estado de lectura de cada descriptor ni devolver una línea perteneciente a otro descriptor.

Esto significa que se debe poder utilizar `get_next_line()` una vez sobre el descriptor `3`, otra vez sobre el descriptor `4` y otra vez sobre el descriptor `5`, de forma alterna y sucesiva, sin perder el seguimiento del estado de lectura de ninguno de ellos.

### Archivos bonus

Se debe añadir el sufijo `_bonus.[c|h]` a los archivos de la parte bonus.

Además de los archivos de la parte obligatoria, se deben entregar los siguientes tres archivos:

- `get_next_line_bonus.c`
- `get_next_line_bonus.h`
- `get_next_line_utils_bonus.c`