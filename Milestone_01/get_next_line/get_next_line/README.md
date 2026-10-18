*Este proyecto ha sido creado como parte del currículo de 42 por dcasasol.*

# get_next_line

## Descripción

`get_next_line` es un proyecto del currículo de 42 cuyo objetivo es implementar una función capaz de devolver, una llamada cada vez, la siguiente línea disponible desde un descriptor de archivo.

La función pública es:

```c
char *get_next_line(int fd);
```

En cada llamada, la función lee únicamente lo necesario para obtener una línea. Cuando encuentra un salto de línea, devuelve una cadena que incluye ese `\n`. Si llega al final del archivo sin más datos, devuelve `NULL`. También debe devolver `NULL` cuando se produce un error de lectura o de memoria.

El proyecto incluye:

- La implementación obligatoria en `get_next_line.c`, `get_next_line.h` y `get_next_line_utils.c`.
- La implementación bonus en `get_next_line_bonus.c`, `get_next_line_bonus.h` y `get_next_line_utils_bonus.c`.
- El fichero `test.txt`, utilizado como entrada de ejemplo.

## Instrucciones

### Compilación

No se utiliza una biblioteca externa ni `libft`. La implementación puede compilarse directamente con `cc`:

```sh
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 \\
   get_next_line.c get_next_line_utils.c main.c -o gnl
```

Para compilar la versión bonus:

```sh
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 \\
   get_next_line_bonus.c get_next_line_utils_bonus.c main.c -o gnl_bonus
```

`main.c` debe ser un programa de prueba que incluya el header correspondiente y llame a `get_next_line`.

El valor de `BUFFER_SIZE` se puede cambiar en la compilación. Algunos valores útiles para comprobar el comportamiento son `1`, `7`, `8`, `42`, `1024`, `1025` y `9999`:

```sh
cc -Wall -Wextra -Werror -D BUFFER_SIZE=1 \\
   get_next_line.c get_next_line_utils.c main.c -o gnl_bs1
```

### Ejecución

Para leer un archivo, el programa de prueba debe abrirlo con `open()` y pasar el descriptor a `get_next_line`:

```sh
./gnl test.txt
```

Para leer desde la entrada estándar, se puede redirigir un archivo:

```sh
./gnl < test.txt
```

También se puede escribir directamente en la terminal y finalizar la entrada con `Ctrl-D`.

Un patrón típico de lectura es:

```c
char *line;

line = get_next_line(fd);
while (line != NULL)
{
    write(1, line, ft_strlen(line));
    free(line);
    line = get_next_line(fd);
}
```

La función no libera la cadena devuelta: el código que la recibe debe hacerlo después de utilizarla.

### Bonus

La versión bonus mantiene un resto independiente por descriptor de archivo. Por ello permite alternar llamadas sobre varios descriptores sin mezclar las líneas pendientes:

```c
line_a = get_next_line(fd_a);
line_b = get_next_line(fd_b);
line_a = get_next_line(fd_a);
line_b = get_next_line(fd_b);
```

## Algoritmo y justificación

La implementación utiliza un algoritmo de lectura incremental basado en tres elementos:

1. Un buffer temporal de tamaño `BUFFER_SIZE` recibe los datos mediante `read()`.
2. Un buffer dinámico `t_buffer` acumula los fragmentos que forman la línea actual. Su capacidad aumenta cuando el contenido no cabe.
3. El resto de bytes que aparecen después del primer `\n` se guarda para la siguiente llamada.

El flujo de una llamada es el siguiente:

1. Se valida el descriptor y el valor de `BUFFER_SIZE`.
2. Se comprueba si el resto guardado ya contiene un salto de línea. Si es así, se completa la línea sin realizar otra lectura.
3. Si todavía no hay una línea completa, se lee un bloque del descriptor.
4. Se busca el primer `\n` del bloque.
5. Si se encuentra, se añade esa parte a la línea devuelta y se conserva el contenido posterior como resto.
6. Si no se encuentra, se añade todo el bloque y se continúa leyendo.
7. Si `read()` devuelve cero y no se ha acumulado ningún carácter, se libera la memoria y se devuelve `NULL`.
8. Si `read()` devuelve `-1` o falla una reserva de memoria, se libera la memoria temporal y se devuelve `NULL`.

Este algoritmo se ha seleccionado porque cumple directamente el requisito de no leer el archivo completo antes de devolver una línea. Su memoria de trabajo es proporcional a la longitud de la línea y el tamaño del buffer de lectura es configurable. Además, guardar el resto evita perder los datos ya leídos y permite que la siguiente llamada empiece exactamente donde terminó la anterior.

En la versión bonus, el resto se almacena asociado al descriptor, lo que conserva el estado de cada archivo cuando se intercalan lecturas. La implementación no utiliza `lseek()` y no depende de variables globales.

## Comportamiento esperado

- Una línea terminada en `\n` se devuelve incluyendo ese carácter.
- Una última línea que llega al final del archivo sin `\n` se devuelve con su contenido disponible; la siguiente llamada devuelve `NULL`.
- Un archivo vacío devuelve `NULL` desde la primera llamada.
- Un descriptor inválido, un error de `read()` o un error de memoria deben producir `NULL`.
- Deben funcionar líneas cortas, líneas vacías, líneas de más de 2000 caracteres y cualquier `BUFFER_SIZE` positivo permitido por la evaluación.

## Recursos

- `man 2 read`: documentación de la llamada al sistema utilizada para leer datos.
- `man 2 open`: apertura de archivos y obtención de descriptores.
- `man 2 close`: cierre de descriptores.
- `man 3 malloc`: reserva dinámica de memoria.
- `man 3 free`: liberación de memoria.
- [GNU C Library - Low-Level I/O](https://www.gnu.org/software/libc/manual/html_node/I_002fO-Overview.html): visión general de la entrada y salida de bajo nivel en C.
- [POSIX.1-2017 - read](https://pubs.opengroup.org/onlinepubs/9699919799/functions/read.html): especificación de `read()`.
- El enunciado `es.subject.pdf` incluido en este repositorio: requisitos oficiales del ejercicio.

### Uso de inteligencia artificial

Se ha utilizado inteligencia artificial como apoyo documental para:

- Revisar la estructura y el propósito de los archivos del proyecto.
- Organizar y redactar este README en relación con los requisitos de 42.
- Explicar el algoritmo de lectura incremental y preparar ejemplos de compilación y ejecución.

La IA no sustituye la comprensión ni la validación del código: la implementación debe comprobarse compilando con distintos valores de `BUFFER_SIZE` y ejecutando pruebas sobre archivos, `stdin`, líneas vacías, líneas cortas y líneas largas.
