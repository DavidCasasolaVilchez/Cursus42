`Este proyecto ha sido creado como parte del currículo de 42 por dcasasol`

# Codexion

Implementación en C de un sistema concurrente en el que varios **coders** compiten por dos **dongles** compartidos para poder compilar. El proyecto sirve para practicar:

- creación y coordinación de hilos POSIX;
- exclusión mutua con `pthread_mutex_t`;
- espera eficiente con `pthread_cond_t`;
- planificación de peticiones `FIFO` y `EDF`;
- detección de agotamiento (*burnout*);
- finalización ordenada de hilos;
- gestión manual de memoria;
- prevención de *deadlocks*, accesos inválidos y *double free*.

El comportamiento está inspirado en el problema clásico de los filósofos comensales: cada coder necesita dos recursos compartidos, y una mala estrategia de adquisición puede dejar a todos los hilos bloqueados.

---

## Índice

1. [Descripción del problema](#descripción-del-problema)
2. [Requisitos](#requisitos)
3. [Estructura del proyecto](#estructura-del-proyecto)
4. [Compilación](#compilación)
5. [Ejecución](#ejecución)
6. [Argumentos](#argumentos)
7. [Ejemplo](#ejemplo)
8. [Ciclo de vida](#ciclo-de-vida)
9. [Arquitectura concurrente](#arquitectura-concurrente)
10. [Colas de peticiones](#colas-de-peticiones)
11. [Planificación FIFO y EDF](#planificación-fifo-y-edf)
12. [Estados de un coder](#estados-de-un-coder)
13. [Finalización y burnout](#finalización-y-burnout)
14. [Gestión de memoria](#gestión-de-memoria)
15. [Equivalencias con Java](#equivalencias-con-java)
16. [Valgrind y depuración](#valgrind-y-depuración)
17. [Problemas típicos](#problemas-típicos)
18. [Limitaciones y mejoras pendientes](#limitaciones-y-mejoras-pendientes)
19. [Blocking cases handled](#blocking-cases-handled)
20. [Thread synchronization mechanisms](#thread-synchronization-mechanisms)
21. [Recursos](#recursos)

---

## Descripción del problema

El programa recibe una configuración y crea varios coders que se ejecutan en paralelo.

Cada coder:

1. solicita sus dos dongles vecinos;
2. espera a ser la siguiente petición válida según el planificador;
3. adquiere ambos dongles;
4. compila;
5. libera los dongles;
6. espera el tiempo de enfriamiento;
7. depura;
8. refactoriza;
9. vuelve a solicitar los dongles.

La ejecución termina cuando ocurre una de estas situaciones:

- un coder supera su tiempo máximo sin completar una compilación y se quema;
- todos los coders alcanzan el número de compilaciones requerido.

El hilo principal espera la terminación del monitor y, posteriormente, la terminación de todos los coders antes de liberar la memoria.

---

## Requisitos

El proyecto necesita:

- Linux o un sistema POSIX;
- compilador C compatible con `pthread`;
- biblioteca POSIX Threads;
- Valgrind para las comprobaciones opcionales de memoria.

Comprobación rápida del entorno:

```bash
cc --version
valgrind --version
```

---

## Estructura del proyecto

```text
codexion/
├── README.md
├── Makefile
├── a.out
├── coders/
│   ├── args_utils.c
│   ├── coder_thread.c
│   ├── coder_thread_utils.c
│   ├── codexion.h
│   ├── displayer_utils.c
│   ├── dongle_utils.c
│   ├── dongle_utils2.c
│   ├── exit_utils.c
│   ├── heap_utils.c
│   ├── main.c
│   ├── memory_utils.c
│   └── monitor_thread.c
└── filo_dam/
    ├── Cena.java
    ├── Filosofo.java
    ├── Lanzador.java
    └── Palillo.java
```

### Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.c` | Entrada del programa, inicialización del contexto y espera de finalización |
| `codexion.h` | Estructuras, enumeraciones y prototipos compartidos |
| `args_utils.c` | Validación básica de argumentos y selección del planificador |
| `coder_thread.c` | Creación y ejecución de los hilos de los coders |
| `coder_thread_utils.c` | Compilación, depuración, refactorización y creación de peticiones |
| `dongle_utils.c` | Adquisición y liberación coordinada de dongles |
| `dongle_utils2.c` | Creación e inicialización de dongles y sus colas |
| `heap_utils.c` | Ordenación y eliminación de peticiones |
| `monitor_thread.c` | Vigilancia de burnout y señal de finalización |
| `displayer_utils.c` | Impresión sincronizada de acciones |
| `exit_utils.c` | Espera y liberación ordenada de recursos |
| `memory_utils.c` | Implementación local de `ft_calloc` |
| `filo_dam/` | Implementación Java de apoyo para comparar los modelos de concurrencia |

---


# Instrucciones

## Compilación

El `Makefile` actual no contiene reglas de compilación completas. Por tanto, el comando recomendado es:

```bash
cd codexion
cc -Wall -Wextra -Werror -pthread coders/*.c -o a.out
```

La opción `-pthread` es necesaria porque el programa usa la API POSIX Threads.

Para una compilación más detallada:

```bash
cc -Wall -Wextra -Werror -pedantic -pthread coders/*.c -o a.out
```

> Si el compilador de tu sistema rechaza alguna advertencia adicional de `-pedantic`, utiliza el primer comando.

---

## Ejecución

La sintaxis es:

```bash
./a.out number_of_coders time_to_burnout time_to_compile \
time_to_debug time_to_refactor number_of_compiles_required \
dongle_cooldown scheduler
```

Ejemplo:

```bash
./a.out 8 120000 10000 8000 5000 4 2000 edf
```

Los tiempos se expresan en **milisegundos**.

---

## Argumentos

| Posición | Nombre | Descripción | Unidad |
|---:|---|---|---|
| `1` | `number_of_coders` | Número de coders que se crearán | cantidad |
| `2` | `time_to_burnout` | Tiempo máximo desde el inicio de la última compilación | ms |
| `3` | `time_to_compile` | Duración de una compilación | ms |
| `4` | `time_to_debug` | Duración de la fase de depuración | ms |
| `5` | `time_to_refactor` | Duración de la fase de refactorización | ms |
| `6` | `number_of_compiles_required` | Compilaciones necesarias por coder | cantidad |
| `7` | `dongle_cooldown` | Tiempo de enfriamiento tras usar los dongles | ms |
| `8` | `scheduler` | Algoritmo de planificación: `fifo` o `edf` | texto |

### Restricciones actuales

- deben proporcionarse exactamente ocho argumentos además del nombre del ejecutable;
- todos los valores numéricos deben ser positivos;
- debe haber al menos dos coders;
- el planificador debe ser `fifo` o `edf`;
- el nombre del planificador se espera en minúsculas.

Si los argumentos no son válidos, el programa imprime:

```text
Invalid arguments
```

---

## Ejemplo

```bash
./a.out 4 120000 1000 500 500 2 100 edf
```

Una salida posible es:

```text
12345 1 has taken a dongle
12346 1 has taken a dongle
12347 1 is compiling
13450 1 is debugging
13960 1 is refactoring
...
```

El primer número es el tiempo transcurrido en microsegundos desde el inicio del
programa, calculado al emitir el mensaje. El segundo es el identificador del
coder.

Las acciones posibles son:

- `has taken a dongle`
- `is compiling`
- `is debugging`
- `is refactoring`
- `burned out`

---

## Ciclo de vida

La inicialización se realiza en este orden:

```text
main
 ├── reserva y pone a cero t_cx
 ├── inicializa mutex de salida
 ├── inicializa mutex y condición del planificador
 ├── valida argumentos
 ├── crea dongles y colas
 ├── crea coders
 └── crea el monitor
```

Durante la ejecución:

```text
monitor ────────────────┐
                       │
coder 1 ────────────────┤
coder 2 ────────────────┤── trabajan concurrentemente
coder N ────────────────┘
```

Al terminar:

```text
monitor establece end = 1
        ↓
despierta a los coders bloqueados
        ↓
main hace join del monitor
        ↓
main hace join de todos los coders
        ↓
se liberan coders, colas y dongles
        ↓
se destruyen mutexes y condición
```

La regla fundamental es:

> Los hilos de trabajo no liberan el contexto global.  
> El hilo principal es el único responsable de la limpieza final.

---

## Arquitectura concurrente

### Contexto global: `t_cx`

`t_cx` contiene la configuración y los recursos compartidos:

- número de coders;
- tiempos de cada fase;
- array de dongles;
- array de coders;
- hilo monitor;
- mutex de salida;
- mutex del planificador;
- condición para avisar cambios;
- estado global de finalización;
- contadores de elementos creados.

### Coder: `t_coder`

Cada coder contiene:

- identificador;
- referencia al contexto global;
- índice del dongle izquierdo;
- índice del dongle derecho;
- hilo POSIX;
- número de compilaciones realizadas;
- instante de inicio de su última compilación.

### Dongle: `t_dongles`

Cada dongle contiene:

- algoritmo de planificación;
- su cola de peticiones;
- mutex propio;
- marca de ocupado/libre.

### Petición: `t_request`

Cada petición contiene:

- instante de llegada;
- fecha límite calculada;
- identificador del coder.

Cada dongle recibe una copia independiente de la petición. Esto evita que dos colas compartan el mismo puntero y lo liberen dos veces.

---

## Colas de peticiones

Cada coder necesita dos dongles. Por ello, cuando solicita recursos, se crean dos peticiones:

```text
petición para dongle izquierdo
petición para dongle derecho
```

Las peticiones se insertan bajo `scheduler_mutex` para que ningún hilo lea una cola mientras otro la está modificando.

### Inserción

La inserción:

1. coloca la petición al final de la cola;
2. incrementa `heap->size`;
3. reordena según el planificador;
4. despierta a los hilos que esperan.

### Eliminación

Cuando un coder obtiene ambos dongles:

1. se elimina la petición situada en la posición cero de cada cola;
2. se liberan las peticiones eliminadas;
3. se desplazan las peticiones restantes;
4. se reduce `heap->size`.

### Propiedad de memoria

El array de peticiones pertenece al heap del dongle. Cada `t_request` almacenado pertenece a una única cola. Esto permite que `free_heap()` libere cada petición una sola vez.

---

## Planificación FIFO y EDF

El argumento final selecciona el algoritmo:

### FIFO

`FIFO` significa *First In, First Out*. Se prioriza la petición que llegó antes:

```text
menor arrival → mayor prioridad
```

### EDF

`EDF` significa *Earliest Deadline First*. Se prioriza la petición con fecha límite más cercana:

```text
menor deadline → mayor prioridad
```

La reordenación se realiza en [`heap_utils.c`](./coders/heap_utils.c).

---

## Estados de un coder

El flujo lógico de cada coder es:

```text
REQUESTING
    ↓
WAITING
    ↓
USING_DONGLES
    ↓
COMPILING
    ↓
COOLDOWN
    ↓
DEBUGGING
    ↓
REFACTORING
    └── vuelve a REQUESTING
```

En la implementación actual estos estados no están representados mediante un `enum`; se corresponden con las funciones:

| Estado conceptual | Función |
|---|---|
| Solicitar | `try_take_dongles()` |
| Esperar | `take_dongles()` y `pthread_cond_wait()` |
| Adquirir | `take_dongles()` |
| Compilar | `compile()` |
| Liberar/enfriar | `leave_dongles()` |
| Depurar | `debbug()` |
| Refactorizar | `refractor()` |

---

## Finalización y burnout

El monitor revisa periódicamente el tiempo desde la última compilación de cada coder.

Si el tiempo supera `time_to_burnout`:

1. se imprime `burned out`;
2. se establece `cx->end = 1`;
3. se despiertan los coders que estén esperando;
4. el monitor termina;
5. los coders salen de sus bucles;
6. `main()` espera a todos los hilos.

Cuando todos los coders alcanzan `number_of_compiles_required`, también se establece `cx->end = 1` y se notifica la condición.

### Por qué se usa una condición

Un bucle como este sería incorrecto:

```c
while (!puedo_coger_los_dos)
	;
```

Ese código consume CPU y puede monopolizar el procesador. `pthread_cond_wait()` suspende el hilo hasta que una modificación de la cola pueda cambiar la condición.

Siempre se debe utilizar dentro de un `while`, no de un `if`, porque al despertar hay que volver a verificar la condición.

---

## Gestión de memoria

La liberación se hace en orden inverso a la dependencia:

```text
join de hilos
    ↓
liberar coders
    ↓
liberar peticiones y heaps
    ↓
liberar dongles
    ↓
liberar arrays
    ↓
destruir mutexes y condición
    ↓
liberar t_cx
```

Nunca se debe liberar `t_cx` mientras un hilo pueda seguir accediendo a él.

### Errores que se evitan

La arquitectura actual evita los siguientes errores habituales:

- `double free` de `t_cx`;
- liberar `cx` desde el monitor y volver a liberarlo desde `main`;
- acceder a dongles después de liberarlos;
- compartir el mismo `t_request *` entre dos heaps;
- hacer `pthread_join()` desde el propio hilo;
- liberar una cola mientras un coder la está utilizando.

---

## Equivalencias con Java

El directorio [`filo_dam/`](./filo_dam/) contiene una implementación Java relacionada con el problema de los filósofos.

La correspondencia entre ambos modelos es:

| Concepto | Java | C/Pthreads |
|---|---|---|
| Hilo | `Thread` | `pthread_t` |
| Ejecutar un hilo | `start()` | `pthread_create()` |
| Esperar un hilo | `join()` | `pthread_join()` |
| Exclusión mutua | `synchronized` | `pthread_mutex_lock()` / `unlock()` |
| Esperar una condición | `wait()` | `pthread_cond_wait()` |
| Despertar un hilo | `notify()` | `pthread_cond_signal()` |
| Despertar varios | `notifyAll()` | `pthread_cond_broadcast()` |
| Estado compartido | campo protegido/atómico | campo protegido por mutex |
| Liberación | gestionada por GC | manual con `free()` |

### Equivalencia conceptual

En Java:

```java
synchronized (scheduler) {
    while (!canAcquire(coder)) {
        scheduler.wait();
    }
    acquire(coder);
}
```

En C:

```c
pthread_mutex_lock(&cx->scheduler_mutex);
while (!can_acquire(coder, cx) && !cx->end)
	pthread_cond_wait(&cx->scheduler_changed,
		&cx->scheduler_mutex);
acquire(coder, cx);
pthread_mutex_unlock(&cx->scheduler_mutex);
```

La diferencia fundamental es que Java gestiona automáticamente la memoria de los objetos, mientras que en C hay que decidir:

- quién crea cada objeto;
- quién es su propietario;
- cuándo deja de ser accesible;
- quién lo libera;
- en qué orden se destruyen los recursos.

---

## Valgrind y depuración

### Comprobar errores de memoria

```bash
valgrind \
	--leak-check=full \
	--show-leak-kinds=all \
	--track-origins=yes \
	./a.out 4 120000 1000 500 500 2 100 edf
```

### Hacer que Valgrind falle si encuentra errores

```bash
valgrind \
	--leak-check=full \
	--error-exitcode=1 \
	./a.out 4 120000 1000 500 500 2 100 edf
```

### Helgrind

Para buscar problemas de sincronización:

```bash
valgrind \
	--tool=helgrind \
	./a.out 4 120000 1000 500 500 2 100 edf
```

### Sanitizers

Si el compilador lo permite:

```bash
cc -Wall -Wextra -Werror -pthread \
	-fsanitize=address,undefined \
	-g coders/*.c -o a.out
```

Para detectar carreras de datos puede probarse:

```bash
cc -Wall -Wextra -Werror -pthread \
	-fsanitize=thread \
	-g coders/*.c -o a.out
```

No todos los entornos permiten combinar simultáneamente todos los sanitizers.

---

## Problemas típicos

### El programa se queda bloqueado

Las causas más habituales son:

- adquirir dos mutexes en órdenes diferentes;
- no despertar a los hilos cuando cambia la cola;
- olvidar `pthread_cond_broadcast()` al terminar;
- esperar en una condición que nunca puede cumplirse;
- liberar un mutex que el hilo no posee;
- no hacer `join` de los hilos antes de liberar sus datos.

### Aparece `Invalid read`

Comprueba:

- que el objeto no se haya liberado antes;
- que el índice del array esté dentro de rango;
- que `requests[0]` no sea `NULL`;
- que el hilo no siga usando `cx` después de que `main` haya iniciado la limpieza.

### Aparece `Invalid free`

Comprueba:

- que cada asignación tenga una única liberación;
- que dos heaps no compartan el mismo `t_request *`;
- que `free_context()` solo se ejecute una vez;
- que no se libere memoria perteneciente a una estructura estática.

### Solo aparece un coder o faltan coders

Comprueba que el bucle de creación sea:

```c
while (i < cx->number_of_coders)
```

y no:

```c
while (i < cx->number_of_coders - 1)
```

---

## Limitaciones y mejoras pendientes

El proyecto es una implementación de aprendizaje y todavía puede mejorarse en varios puntos:

### Validación de argumentos

La validación actual utiliza `atoi()`. Para un programa más robusto debería usarse `strtoll()` y comprobar:

- overflow;
- caracteres sobrantes;
- valores fuera del rango permitido;
- errores de conversión.

### Reloj monotónico

Para medir duraciones sería preferible `clock_gettime(CLOCK_MONOTONIC, ...)` frente a `gettimeofday()`, porque el reloj de pared puede ser ajustado por el sistema.

### Makefile

El `Makefile` debería definir al menos:

- nombre del ejecutable;
- lista de fuentes;
- flags de compilación;
- objetivo `all`;
- objetivo `clean`;
- objetivo `fclean`;
- objetivo `re`.

### Manejo de errores de pthread

Todas las llamadas a:

- `pthread_create`;
- `pthread_join`;
- `pthread_mutex_init`;
- `pthread_mutex_lock`;
- `pthread_mutex_unlock`;
- `pthread_cond_wait`;
- `pthread_cond_broadcast`;

deberían comprobar su valor de retorno y tratar los errores de forma explícita.

### Estado formal del coder

Un `enum` de estados haría más fácil depurar el programa y verificar las transiciones de cada coder.

### Separación de responsabilidades

Las funciones de creación deberían devolver éxito o error y no liberar directamente el contexto global. La política recomendada es:

```text
crear → devolver error
main decide si limpia
main hace una única limpieza final
```

---

## Checklist de pruebas

### Argumentos

- [ ] Número incorrecto de argumentos.
- [ ] Coder menor que dos.
- [ ] Tiempo igual a cero.
- [ ] Scheduler desconocido.
- [ ] Scheduler en mayúsculas.

### Concurrencia

- [ ] Dos coders compitiendo por los mismos dongles.
- [ ] Muchos coders con dos dongles.
- [ ] `fifo`.
- [ ] `edf`.
- [ ] Cooldown mayor que el tiempo de compilación.

### Finalización

- [ ] Finalización por burnout.
- [ ] Finalización por número de compilaciones.
- [ ] Ningún coder continúa después de `burned out`.
- [ ] Todos los hilos terminan.
- [ ] `main` libera una sola vez.

### Memoria

- [ ] Sin `Invalid read`.
- [ ] Sin `Invalid write`.
- [ ] Sin `Invalid free`.
- [ ] Sin `double free`.
- [ ] Sin bloques definitivamente perdidos.

---

## Blocking cases handled

La solución considera los principales casos de bloqueo que aparecen cuando varios
coders compiten por dos dongles compartidos:

### Prevención de interbloqueos y condiciones de Coffman

- **Exclusión mutua:** los cambios en las colas, el estado `busy` y la bandera
  global `end` se realizan bajo `scheduler_mutex`.
- **Adquisición atómica de los dos recursos:** un coder solo retira sus dos
  peticiones de las colas y marca ambos dongles como ocupados dentro de la misma
  sección crítica. No conserva un dongle mientras espera el otro.
- **Espera circular:** al no adquirir primero un recurso y después bloquearse
  indefinidamente por el segundo, se rompe la condición de espera circular del
  problema de los filósofos.
- **Liberación:** los dongles se marcan como libres después del cooldown y se
  despierta a los hilos que pueden continuar.

El mutex del contexto serializa la decisión completa, por lo que dos coders no
pueden observar simultáneamente que los mismos dongles están disponibles y
adquirirlos ambos.

### Prevención de inanición

Las peticiones no se atienden mediante una espera ciega: cada cola se ordena por
`arrival` en `FIFO` o por `deadline` en `EDF`. Un coder solo continúa cuando su
petición está en la primera posición de **las dos** colas. Esto proporciona una
política explícita y evita que la competición dependa únicamente del orden en
que el sistema operativo despierte los hilos. `FIFO` ofrece la garantía más
directa contra esperas indefinidas por adelantamientos; `EDF` prioriza la
proximidad al burnout, aunque ninguna política de prioridad garantiza por sí
sola ausencia absoluta de inanición bajo cualquier configuración.

### Cooldown

Después de compilar, `leave_dongles()` espera `dongle_cooldown` antes de cambiar
`busy` a cero. Durante ese intervalo los dongles siguen reservados, se evita que
otro coder los use prematuramente y el despertar de los hilos se produce justo
después de la liberación lógica.

### Detección de agotamiento

El monitor comprueba periódicamente el tiempo transcurrido desde
`last_compile_start` de cada coder bajo `scheduler_mutex`. Si se supera
`time_to_burnout`, publica el evento `end`, emite el mensaje de burnout y
despierta a los coders bloqueados. Si todos los contadores de compilaciones
alcanzan `number_of_compiles_required`, cualquier coder puede activar la misma
señal global de finalización.

### Serialización del log

Cada mensaje se imprime bajo `cx->display`. Además, la marca temporal se obtiene
dentro de esa sección crítica, por lo que el orden de las líneas coincide con el
orden en que el programa entra al displayer, incluso cuando varios hilos llegan
simultáneamente a una transición de estado.

## Thread synchronization mechanisms

La implementación utiliza las primitivas POSIX siguientes:

### `pthread_mutex_t`

El contexto global contiene dos mutex con responsabilidades separadas:

- `display` protege la salida de terminal. Impide que dos coders o el monitor
  mezclen sus mensajes y protege también el resumen final.
- `scheduler_mutex` protege el estado compartido del planificador: colas de
  peticiones, contadores de compilación, marcas de tiempo de compilación,
  `busy`, `end` y la fase de arranque de los hilos.

Cada `t_dongles` también tiene un mutex propio, reservado para el recurso
individual. La implementación actual centraliza las operaciones de adquisición
en `scheduler_mutex`, de modo que la decisión de obtener ambos dongles es
atómica y no se mantiene un mutex de dongle mientras se espera otro.

Ejemplo de prevención de una condición de carrera:

```c
pthread_mutex_lock(&cx->scheduler_mutex);
while (!cx->end && (!request_is_first(left->heap, coder->id)
        || !request_is_first(right->heap, coder->id)
        || left->busy || right->busy))
    pthread_cond_wait(&cx->scheduler_changed, &cx->scheduler_mutex);
remove_from_heap(left);
remove_from_heap(right);
left->busy = 1;
right->busy = 1;
pthread_mutex_unlock(&cx->scheduler_mutex);
```

La comprobación y la actualización forman una sola operación protegida; ningún
otro hilo puede cambiar las colas o `busy` entre ambas.

### `pthread_cond_t`

`scheduler_changed` es una condición asociada a `scheduler_mutex`. Se utiliza
para que los coders duerman mientras no pueden adquirir sus dos dongles, en vez
de consumir CPU con un bucle activo. Se hace `pthread_cond_broadcast()` cuando:

- se insertan nuevas peticiones;
- se liberan los dongles después del cooldown;
- se alcanza el final normal o se detecta un burnout;
- los hilos quedan habilitados al terminar la inicialización.

Como exige POSIX, cada espera está dentro de un `while`: al despertar, el coder
vuelve a comprobar la condición real bajo el mutex. Así se gestionan tanto los
despertares espurios como la competición entre varios coders despertados.

### Comunicación segura entre coders y monitor

Los coders actualizan `last_compile_start`, sus contadores y el estado de
finalización bajo `scheduler_mutex`. El monitor lee esos datos bajo el mismo
mutex, decide si existe burnout y publica `end` también bajo ese mutex. Después
usa `pthread_cond_broadcast()` para que todos los coders bloqueados observen el
cambio y puedan salir sin quedar dormidos indefinidamente.

No existe una clase o estructura de “evento” personalizada: la combinación de
`pthread_cond_t`, `scheduler_mutex` y la bandera `end` proporciona el mecanismo
de evento utilizado por este proyecto.

## Recursos

Referencias clásicas y documentación consultada para el diseño y la
implementación:

- [POSIX Threads (`pthreads`) — The Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html):
  API y contratos de mutexes, condiciones, creación y unión de hilos.
- [Man page de `pthread_mutex_lock(3)](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3p.html):
  exclusión mutua y reglas de bloqueo.
- [Man page de `pthread_cond_wait(3)](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3.html):
  espera condicional asociada a un mutex y necesidad de revalidar el predicado.
- [The Linux Programming Interface, capítulos sobre POSIX threads](https://man7.org/tlpi/):
  referencia práctica sobre sincronización, condiciones de carrera y ciclo de
  vida de los hilos.
- E. W. Dijkstra, *Cooperating Sequential Processes* (1965): formulación
  clásica del problema de los filósofos y de la exclusión mutua.
- E. G. Coffman Jr., M. Elphick y A. Shoshani, *System Deadlocks* (1971):
  condiciones necesarias para los interbloqueos y estrategias para romperlas.
- [Valgrind Helgrind](https://valgrind.org/docs/manual/hg-manual.html):
  detección de condiciones de carrera y uso incorrecto de primitivas POSIX.

### Uso de IA

Se utilizó un asistente de IA como apoyo técnico, no como sustituto de la
verificación del código. En concreto, se empleó para:

- revisar la arquitectura de concurrencia de `coders/`, especialmente
  `coder_thread.c`, `dongle_utils.c`, `monitor_thread.c` y
  `displayer_utils.c`;
- analizar el desorden aparente de los mensajes y detectar el uso incompleto
  de `timeval` (`tv_usec` sin `tv_sec`) y de marcas capturadas antes de una
  espera;
- proponer y aplicar una corrección localizada en el cálculo de timestamps,
  la planificación `EDF` y la identificación del coder monitorizado;
- redactar y estructurar esta documentación sobre bloqueo, sincronización y
  referencias;
- revisar el diff y validar la compilación con
  `gcc -Wall -Wextra -Werror -pthread coders/*.c`.

Las decisiones finales se contrastaron con el código fuente y con una ejecución
de prueba; la responsabilidad de integrar, revisar y validar los cambios
pertenece al autor del proyecto.