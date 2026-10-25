*Este proyecto ha sido creado como parte del currículo de 42 por DavidCasasolaVilchez.*

# Codexion

## Descripción

Codexion es un proyecto de concurrencia escrito en C con POSIX Threads. Varios
coders trabajan en paralelo y compiten por dongles compartidos: para compilar,
cada coder necesita adquirir sus dos dongles vecinos. El programa modela las
fases de compilación, depuración y refactorización, y termina cuando todos los
coders completan el número de compilaciones solicitado o cuando uno de ellos se
agota (*burns out*).

El objetivo principal es practicar:

- creación, coordinación y finalización de hilos;
- exclusión mutua y comunicación entre hilos;
- diseño de colas concurrentes;
- planificación `FIFO` y `EDF`;
- prevención de interbloqueos (*deadlocks*);
- detección de agotamiento usando medidas de tiempo;
- liberación ordenada de memoria y recursos POSIX.

El proyecto se encuentra en [`Milestone_03/codexion/`](./Milestone_03/codexion/).
El directorio [`Milestone_03/codexion/filo_dam/`](./Milestone_03/codexion/filo_dam/)
contiene además una implementación Java relacionada con el problema de los
filósofos, útil para comparar el modelo de concurrencia de Java con
`pthread`.

## Características principales

- Creación de todos los coders solicitados por línea de comandos.
- Un hilo POSIX independiente por coder.
- Un hilo monitor que comprueba el burnout.
- Colas independientes de peticiones por dongle.
- Copias independientes de cada petición para evitar dobles liberaciones.
- Planificación `FIFO` (*First In, First Out*).
- Planificación `EDF` (*Earliest Deadline First*).
- Espera con `pthread_cond_t` en lugar de espera activa.
- Serialización de la salida mediante un mutex de logging.
- Finalización centralizada desde el hilo principal.
- Limpieza comprobable con Valgrind.

## Instrucciones

### Requisitos

Se necesita un entorno POSIX con:

- compilador C (`cc` o `clang`);
- biblioteca POSIX Threads;
- `make` opcional;
- Valgrind opcional para las pruebas de memoria.

### Compilación

El `Makefile` de `Milestone_03/codexion/` todavía no contiene reglas de
compilación completas. Desde el directorio del proyecto se puede compilar
directamente con:

```bash
cd Milestone_03/codexion
cc -Wall -Wextra -Werror -pthread coders/*.c -o a.out
```

La opción `-pthread` es necesaria tanto para compilar como para enlazar el
programa con POSIX Threads.

### Ejecución

```bash
./a.out number_of_coders time_to_burnout time_to_compile \
time_to_debug time_to_refactor number_of_compiles_required \
dongle_cooldown scheduler
```

Ejemplo:

```bash
./a.out 8 120000 10000 8000 5000 4 2000 edf
```

Todos los tiempos se expresan en milisegundos.

### Argumentos

| Posición | Nombre | Descripción |
|---:|---|---|
| 1 | `number_of_coders` | Número de coders que se crearán. Debe ser al menos 2. |
| 2 | `time_to_burnout` | Tiempo máximo permitido desde la última compilación. |
| 3 | `time_to_compile` | Duración de la compilación. |
| 4 | `time_to_debug` | Duración de la depuración. |
| 5 | `time_to_refactor` | Duración de la refactorización. |
| 6 | `number_of_compiles_required` | Compilaciones necesarias por coder. |
| 7 | `dongle_cooldown` | Tiempo de enfriamiento de los dongles. |
| 8 | `scheduler` | `fifo` o `edf`. |

Los valores numéricos deben ser positivos. El planificador se escribe en
minúsculas.

### Salida

Cada acción se imprime con el formato:

```text
<timestamp> <coder_id> <action>
```

Ejemplo:

```text
148283 5 has taken a dongle
148284 5 has taken a dongle
148285 5 is compiling
```

Las acciones posibles son:

- `has taken a dongle`;
- `is compiling`;
- `is debugging`;
- `is refactoring`;
- `burned out`.

### Verificación con Valgrind

```bash
cd Milestone_03/codexion
valgrind \
    --leak-check=full \
    --show-leak-kinds=all \
    --track-origins=yes \
    ./a.out 4 120000 1000 500 500 2 100 edf
```

Para que el comando falle si Valgrind encuentra errores:

```bash
valgrind \
    --leak-check=full \
    --error-exitcode=1 \
    ./a.out 4 120000 1000 500 500 2 100 edf
```

Para investigar carreras y bloqueos puede utilizarse Helgrind:

```bash
valgrind --tool=helgrind ./a.out 4 120000 1000 500 500 2 100 edf
```

## Blocking cases handled

### Interbloqueo y condiciones de Coffman

El caso más peligroso es el de dos coders que conservan un dongle y esperan
indefinidamente el segundo. La implementación evita esa situación haciendo que
la decisión de adquirir los dos dongles se tome bajo un único
`scheduler_mutex`. Un coder solo pasa a poseer ambos recursos si:

1. es la primera petición válida en las dos colas;
2. los dos dongles están libres;
3. la operación puede marcar ambos dongles como ocupados de forma indivisible.

Al no adquirir un dongle y bloquearse después intentando adquirir el otro, se
evita la espera circular clásica del problema de los filósofos. También se
reduce la posibilidad de mantener recursos mientras se espera a otro recurso,
una de las condiciones de Coffman que permite el deadlock.

La implementación no depende de que unos coders bloqueen de izquierda a derecha
y otros de derecha a izquierda. La selección se hace de manera coordinada por
el planificador.

### Espera activa

Un bucle que comprueba continuamente una cola consumiría CPU y podría quedarse
ejecutándose sin recibir una notificación. Los coders esperan mediante
`pthread_cond_wait()` y el planificador utiliza
`pthread_cond_broadcast()` cuando:

- se inserta una petición;
- se libera un par de dongles;
- se solicita la finalización.

La condición siempre se comprueba dentro de un `while`, porque despertarse no
garantiza que el recurso siga disponible.

### Inanición (*starvation*)

Las colas mantienen un orden explícito. `FIFO` da prioridad a la petición más
antigua y evita que una petición anterior sea adelantada indefinidamente por
peticiones nuevas. `EDF` da prioridad a la fecha límite más cercana, que es la
política requerida para reducir el riesgo de burnout, aunque una carga
continua de peticiones con fechas límite más cercanas puede posponer otras
peticiones. Por tanto, `FIFO` ofrece una propiedad de justicia más directa;
`EDF` prioriza las urgencias y no constituye por sí solo una prueba formal de
ausencia de inanición.

### Cooldown

Después de usar los dongles, el coder espera el tiempo de cooldown antes de
marcarlos como disponibles. Durante ese intervalo los dongles siguen marcados
como ocupados, por lo que otro coder no puede adquirirlos prematuramente.

El estado de disponibilidad se cambia bajo `scheduler_mutex`, y después se
ejecuta `pthread_cond_broadcast()` para notificar a los coders que esperan.

### Detección precisa del agotamiento

El monitor compara el instante actual con el instante de inicio de la última
compilación de cada coder. El cálculo tiene en cuenta segundos y microsegundos,
no solamente `tv_usec`, evitando resultados negativos cuando el reloj pasa de
un segundo al siguiente.

El monitor establece el estado global de finalización bajo el mutex del
planificador y despierta todos los coders bloqueados. Los coders comprueban ese
estado antes de continuar a la siguiente fase.

### Finalización normal

Cuando todos los coders alcanzan `number_of_compiles_required`, el estado global
se marca como terminado y se notifica la condición. El hilo principal espera
al monitor y después hace `pthread_join()` de cada coder antes de liberar los
arrays, las colas y los dongles.

### Serialización del log

Todos los mensajes pasan por el mutex `display`. Esto evita que dos hilos
escriban simultáneamente y mezclen partes de sus líneas.

### Liberación y errores de memoria

El contexto global no se libera desde los coders ni desde el monitor. El hilo
principal es el propietario de la limpieza final. Los coders se esperan antes
de liberar los dongles y las colas, y cada dongle posee sus propias copias de
las peticiones.

Esta política evita:

- `double free`;
- uso después de `free`;
- liberar `t_cx` mientras otro hilo lo usa;
- destruir un mutex todavía utilizado por otro hilo;
- hacer `pthread_join()` desde el propio hilo.

## Thread synchronization mechanisms

### `pthread_mutex_t`

El proyecto utiliza varios mutexes con responsabilidades separadas:

#### `scheduler_mutex`

Protege el estado compartido del planificador:

- `cx->end`;
- `heap->requests`;
- `heap->size`;
- estado `busy` de los dongles;
- contadores de compilación;
- actualización del instante de última compilación;
- inserción, ordenación y eliminación de peticiones.

Ejemplo conceptual de acceso seguro:

```c
pthread_mutex_lock(&cx->scheduler_mutex);
heap->requests[heap->size++] = request;
reorder_heap(dongle);
pthread_cond_broadcast(&cx->scheduler_changed);
pthread_mutex_unlock(&cx->scheduler_mutex);
```

Sin ese mutex, dos coders podrían leer el mismo `heap->size`, escribir en la
misma posición o eliminar la misma petición.

#### `display`

Protege las llamadas a `printf()`:

```c
pthread_mutex_lock(&cx->display);
printf("%lld %d %s\n", timestamp, id, action);
pthread_mutex_unlock(&cx->display);
```

Esto garantiza una comunicación legible y thread-safe con la persona que
ejecuta el programa.

#### Mutexes de dongle

Cada `t_dongles` conserva un `pthread_mutex_t` propio. La decisión de
planificación se coordina globalmente para adquirir los dos recursos de manera
atómica desde el punto de vista lógico; el campo `busy` representa su
disponibilidad dentro de esa decisión.

### `pthread_cond_t`

`scheduler_changed` es una variable de condición asociada a
`scheduler_mutex`. Se utiliza para que los coders puedan dormir mientras no
pueden adquirir sus dos dongles:

```c
pthread_mutex_lock(&cx->scheduler_mutex);
while (!can_acquire(coder, cx) && !cx->end)
    pthread_cond_wait(&cx->scheduler_changed,
        &cx->scheduler_mutex);
pthread_mutex_unlock(&cx->scheduler_mutex);
```

Cuando cambia una condición relevante, el hilo que realiza el cambio notifica:

```c
pthread_cond_broadcast(&cx->scheduler_changed);
```

El `broadcast` es importante porque varios coders pueden estar esperando
distintos pares de dongles. Cada uno despierta y vuelve a comprobar su propia
condición bajo el mutex.

### Implementación personalizada de eventos

El proyecto no utiliza una clase o estructura de eventos personalizada. El
mecanismo equivalente a un evento está implementado con la pareja POSIX
`pthread_mutex_t` + `pthread_cond_t`:

- el mutex protege el estado que describe el evento;
- la condición permite dormir hasta que ese estado cambie;
- `pthread_cond_broadcast()` comunica el cambio a los hilos interesados.

La señal de finalización se representa actualmente mediante `cx->end`, siempre
leído y escrito bajo `scheduler_mutex`. Esto evita una carrera entre el monitor
y los coders.

### Comunicación entre coders y monitor

El monitor observa el progreso de los coders y puede detectar que uno ha
superado su tiempo de burnout. Para comunicar la decisión:

1. el monitor adquiere `scheduler_mutex`;
2. establece `cx->end = 1`;
3. ejecuta `pthread_cond_broadcast()`;
4. libera el mutex;
5. termina;
6. el hilo principal hace `join` y comienza la limpieza.

Los coders que estaban esperando en `pthread_cond_wait()` se despiertan,
comprueban `cx->end` y salen sin acceder a estructuras que ya hayan sido
liberadas. Este orden es equivalente al patrón `synchronized` +
`wait/notifyAll` de Java.

## Relación con Java

La equivalencia conceptual entre los mecanismos utilizados es:

| Java | POSIX Threads |
|---|---|
| `Thread` | `pthread_t` |
| `start()` | `pthread_create()` |
| `join()` | `pthread_join()` |
| `synchronized` | `pthread_mutex_lock()` / `pthread_mutex_unlock()` |
| `wait()` | `pthread_cond_wait()` |
| `notifyAll()` | `pthread_cond_broadcast()` |
| gestión automática del objeto | `malloc()` / `free()` manuales |

En ambos casos, `wait` solo debe utilizarse dentro de una condición que se
comprueba en un bucle. La diferencia principal es que en C la memoria, la
inicialización de mutexes y la destrucción de recursos son responsabilidad
explícita de la aplicación.

## Organización del código

| Archivo | Responsabilidad |
|---|---|
| [`main.c`](./Milestone_03/codexion/coders/main.c) | Inicialización, creación del monitor y limpieza final |
| [`codexion.h`](./Milestone_03/codexion/coders/codexion.h) | Estructuras, enumeraciones y prototipos |
| [`args_utils.c`](./Milestone_03/codexion/coders/args_utils.c) | Validación de argumentos y planificador |
| [`coder_thread.c`](./Milestone_03/codexion/coders/coder_thread.c) | Creación y ciclo de vida de coders |
| [`coder_thread_utils.c`](./Milestone_03/codexion/coders/coder_thread_utils.c) | Compilación, fases de trabajo y peticiones |
| [`dongle_utils.c`](./Milestone_03/codexion/coders/dongle_utils.c) | Adquisición y liberación coordinada |
| [`dongle_utils2.c`](./Milestone_03/codexion/coders/dongle_utils2.c) | Creación de dongles y colas |
| [`heap_utils.c`](./Milestone_03/codexion/coders/heap_utils.c) | Ordenación y eliminación de peticiones |
| [`monitor_thread.c`](./Milestone_03/codexion/coders/monitor_thread.c) | Detección de burnout |
| [`displayer_utils.c`](./Milestone_03/codexion/coders/displayer_utils.c) | Logging serializado |
| [`exit_utils.c`](./Milestone_03/codexion/coders/exit_utils.c) | `join` y liberación de recursos |

## Recursos

### Documentación oficial

- [POSIX Threads — The Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html):
  referencia de `pthread_create`, `pthread_join` y el ciclo de vida de hilos.
- [POSIX `pthread_mutex_lock`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html):
  semántica de mutexes y exclusión mutua.
- [POSIX `pthread_cond_wait`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html):
  espera condicional y asociación entre condiciones y mutexes.
- [POSIX `pthread_cond_broadcast`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html):
  notificación de varios hilos que esperan.
- [Linux man-pages — `pthreads(7)`](https://man7.org/linux/man-pages/man7/pthreads.7.html):
  visión general de la API de hilos POSIX en Linux.
- [Valgrind Memcheck](https://valgrind.org/docs/manual/mc-manual.html):
  detección de accesos inválidos, dobles liberaciones y fugas.
- [Valgrind Helgrind](https://valgrind.org/docs/manual/hg-manual.html):
  análisis de problemas de sincronización y carreras.

### Conceptos clásicos

- [The Little Book of Semaphores](https://greenteapress.com/wp/semaphores/),
  Allen B. Downey: problemas clásicos de sincronización.
- [Dining Philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem):
  referencia conceptual para recursos compartidos e interbloqueos.
- [Operating Systems: Three Easy Pieces — Concurrency](https://pages.cs.wisc.edu/~remzi/OSTEP/):
  mutexes, condiciones, hilos y problemas clásicos de concurrencia.

### Uso de IA

Se ha utilizado IA como apoyo técnico durante el desarrollo y la
documentación del proyecto, especialmente para:

- analizar trazas de Valgrind;
- localizar causas de `Invalid read`, `Invalid free` y `double free`;
- razonar sobre deadlocks y condiciones de Coffman;
- revisar el orden de `pthread_join()` y la liberación de memoria;
- comparar `pthread_mutex_t` y `pthread_cond_t` con `synchronized`, `wait()` y
  `notifyAll()` de Java;
- proponer pruebas de ejecución, Valgrind y Helgrind;
- redactar y estructurar este README.

La IA se ha utilizado como herramienta de explicación, revisión y apoyo a la
depuración. Las decisiones finales, la integración en el código y la
verificación mediante compilación y ejecución corresponden al autor del
proyecto.

## Limitaciones conocidas y mejoras futuras

- `int_checker()` utiliza actualmente `atoi()`; una versión más robusta debería
  usar `strtoll()` y validar overflow y caracteres sobrantes.
- Para medir duraciones sería preferible `clock_gettime(CLOCK_MONOTONIC, ...)`
  frente a `gettimeofday()`.
- El `Makefile` debería incluir objetivos `all`, `clean`, `fclean` y `re`.
- Todas las llamadas a la API pthread deberían comprobar y reportar sus
  códigos de retorno.
- EDF prioriza fechas límite y no ofrece por sí solo una garantía formal de
  ausencia de inanición.
- La implementación de eventos está basada en la primitiva POSIX
  `pthread_cond_t`; no existe todavía una abstracción `event` propia.

## Licencia

No se ha definido una licencia pública específica para este repositorio.
