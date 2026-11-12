# Fly-in — Drones are interesting

## 1. Objetivo del proyecto

Desarrollar en **Python un sistema de planificación y simulación de rutas para múltiples drones** que deben desplazarse desde una zona de inicio (`start_hub`) hasta una zona de destino (`end_hub`).

El escenario está representado mediante un grafo:
    - Los nodos representan zonas (`hubs`).
	- Las aristas representan conexiones entre zonas.
    - Cada zona y conexión puede tener restricciones de capacidad y movimiento.    

El objetivo principal es conseguir que **todos los drones lleguen al destino utilizando el menor número posible de turnos de simulación**, respetando todas las restricciones.

El proyecto debe incluir:
    1. Un parser para interpretar los archivos de mapas.
    2. Un algoritmo de búsqueda y planificación de rutas.
    3. Un motor de simulación de movimientos.
    4. Un sistema de representación visual.
    5. Una salida de texto con los movimientos de cada turno.

---

## 2. Restricciones técnicas generales

- Lenguaje: Python 3.10 o superior.
    
- Programación completamente orientada a objetos.
    
- No se pueden utilizar bibliotecas que implementen lógica de grafos, como `networkx` o `graphlib`.
    
- El código debe ser completamente tipado (_type-safe_).
    
- Es obligatorio utilizar `flake8` y `mypy`.
    
- Todas las funciones y clases deben incluir docstrings siguiendo PEP 257.
    
- Se deben gestionar correctamente las excepciones y evitar que el programa termine inesperadamente.
    
- Los recursos deben gestionarse correctamente, utilizando context managers cuando corresponda.
    

### Herramientas recomendadas

- `pytest` o `unittest` para pruebas.
    
- `venv` o `conda` para entornos virtuales.
    
- `.gitignore` para excluir archivos temporales de Python.
    

---

## 3. Formato de los archivos de entrada

El programa recibirá archivos que describen mapas de zonas y conexiones.

### 3.1. Número de drones

La primera línea debe indicar el número de drones:

```
nb_drones: 5
```

Debe ser un entero positivo. El programa debe poder gestionar cualquier número de drones.

### 3.2. Definición de zonas

Existen tres tipos de definiciones:

```
start_hub: <name> <x> <y> [metadata]
end_hub: <name> <x> <y> [metadata]
hub: <name> <x> <y> [metadata]
```

Ejemplo:

```
start_hub: hub 0 0 [color=green]
end_hub: goal 10 10 [color=yellow]
hub: roof1 3 4 [zone=restricted color=red]
hub: corridorA 4 3 [zone=priority color=green max_drones=2]
```

Cada zona contiene:

- Nombre único.
    
- Coordenadas `x` e `y`, que siempre serán enteros.
    
- Metadatos opcionales.
    

Siempre habrá exactamente una zona de inicio y una de destino.

### 3.3. Metadatos de las zonas

Los metadatos se escriben entre corchetes y pueden aparecer en cualquier orden.

|Metadato|Descripción|Valor predeterminado|
|---|---|---|
|`zone`|Tipo de zona|`normal`|
|`color`|Color para la representación visual|`none`|
|`max_drones`|Capacidad máxima de drones|`1`|

### 3.4. Tipos de zonas

|Tipo|Coste de movimiento|Comportamiento|
|---|---|---|
|`normal`|1 turno|Zona estándar|
|`restricted`|2 turnos|Zona restringida o peligrosa|
|`priority`|1 turno|Debe tener preferencia en la búsqueda de rutas|
|`blocked`|Inaccesible|No se puede entrar ni atravesar|

Las zonas `priority` tienen el mismo coste que las normales, pero deben priorizarse en los algoritmos de búsqueda.

Los colores son opcionales. Se aceptan cadenas de una sola palabra sin una lista cerrada de colores. Cuando se especifiquen, deben utilizarse para proporcionar representación visual mediante terminal o interfaz gráfica.

### 3.5. Definición de conexiones

Las conexiones se representan así:

```
connection: <name1>-<name2> [metadata]
```

Ejemplo:

```
connection: hub-roof1
connection: corridorA-tunnelB [max_link_capacity=2]
```

Características:

- Las conexiones son bidireccionales.
    
- Los nombres de las zonas no pueden contener guiones (`-`) ni espacios.
    
- Solo pueden conectar zonas definidas previamente.
    
- No puede existir una conexión duplicada, aunque esté escrita en sentido inverso.
    
- La capacidad máxima predeterminada de una conexión es `1`.
    

El metadato disponible es:

|Metadato|Descripción|Valor predeterminado|
|---|---|---|
|`max_link_capacity`|Número máximo de drones que pueden atravesar simultáneamente la conexión|`1`|

### 3.6. Comentarios

Las líneas que comienzan por `#` deben ignorarse.

---

## 4. Requisitos del parser

El parser debe validar todos los archivos de entrada.

Debe comprobar:

1. La primera línea contiene `nb_drones` con un entero positivo.
    
2. Existe exactamente un `start_hub`.
    
3. Existe exactamente un `end_hub`.
    
4. Los nombres de las zonas son únicos.
    
5. Las coordenadas son enteros válidos.
    
6. Los nombres de zonas no contienen espacios ni guiones.
    
7. Las conexiones solo hacen referencia a zonas previamente definidas.
    
8. No existen conexiones duplicadas.
    
9. Los metadatos tienen una sintaxis válida.
    
10. Los tipos de zona pertenecen a:
    
    - `normal`
        
    - `blocked`
        
    - `restricted`
        
    - `priority`
        
11. Las capacidades `max_drones` y `max_link_capacity` son enteros positivos.
    

**Excepción importante:** `max_drones` se ignora en las zonas de inicio y destino. Estas zonas no tienen límite de capacidad, aunque el archivo incluya ese metadato.

Cualquier error de parsing debe detener el procesamiento y mostrar un mensaje claro que indique la línea y la causa del error.

---

## 5. Requisitos del algoritmo de búsqueda de rutas

El algoritmo debe conseguir que todos los drones lleguen al destino con el menor número posible de turnos.

Debe contemplar:

- Distribuir los drones entre diferentes rutas.
    
- Permitir que varios drones se muevan simultáneamente.
    
- Gestionar esperas estratégicas cuando no sea posible avanzar.
    
- Evitar conflictos entre drones.
    
- Evitar bloqueos o _deadlocks_.
    
- Tener en cuenta las longitudes de las rutas y los costes de movimiento.
    
- Considerar las capacidades de las zonas y las conexiones.
    
- Adaptarse a diferentes topologías y tipos de zonas.
    

No basta con encontrar el camino más corto para un único dron. Hay que planificar el movimiento de toda la flota, teniendo en cuenta que los drones compiten por los mismos recursos.

---

## 6. Reglas de ocupación de zonas

Por defecto, una zona puede contener como máximo un dron en un mismo turno.

Sin embargo, existen excepciones:

- Una zona con `max_drones=N` puede contener hasta N drones simultáneamente.
    
- La zona de inicio puede contener todos los drones al principio.
    
- La zona de destino puede recibir todos los drones, sin límite.
    

Reglas adicionales:

1. Dos drones no pueden entrar en una misma zona durante el mismo turno si se supera su capacidad.
    
2. Un dron no puede entrar en una zona que exceda su capacidad máxima.
    
3. Una conexión limita el número de drones que pueden atravesarla simultáneamente mediante `max_link_capacity`.
    
4. Los drones pueden moverse simultáneamente siempre que se respeten todas las capacidades.
    
5. Los drones que abandonan una zona liberan su espacio durante ese mismo turno.
    

Por tanto, el motor de simulación debe evaluar las salidas y entradas de cada turno de forma coherente para no bloquear movimientos que sí serían posibles.

---

## 7. Mecánica de movimiento y turnos

La simulación funciona mediante turnos discretos.

En cada turno, cada dron puede:

- Desplazarse a una zona adyacente conectada, si existe capacidad.
    
- Permanecer en su posición actual.
    
- Atravesar una conexión hacia una zona restringida.
    

### Costes de movimiento

|Destino|Duración|
|---|---|
|Zona normal|1 turno|
|Zona priority|1 turno|
|Zona restricted|2 turnos|
|Zona blocked|Movimiento prohibido|

### Movimiento hacia zonas restricted

Este movimiento tiene una particularidad importante:

1. El dron entra en la conexión hacia la zona restringida.
    
2. Permanece en tránsito durante el tiempo correspondiente.
    
3. Debe alcanzar la zona de destino en el siguiente turno.
    
4. No puede esperar en la conexión a que se libere espacio en la zona de destino.
    

Durante el tránsito, el dron ocupa la conexión.

El sistema debe garantizar que todos los movimientos sean válidos y que las capacidades se respeten en cada turno.

---

## 8. Formato de salida de la simulación

La simulación debe mostrar los movimientos de los drones turno a turno.

Cada turno se representa mediante una línea de texto.

Formato de cada movimiento:

```
D<ID>-<zone>
```

O, cuando el dron está atravesando una conexión hacia una zona restringida:

```
D<ID>-<connection>
```

Los movimientos que ocurren durante un mismo turno se separan mediante espacios.

Los drones que no se mueven no aparecen en esa línea.

### Ejemplo

```
D1-roof1 D2-corridorA
D1-roof2 D2-tunnelB
D1-goal D2-goal
```

Reglas:

- Cada dron tiene un identificador único (`D1`, `D2`, etc.).
    
- Los drones que llegan al destino se consideran entregados.
    
- Una vez entregados, dejan de aparecer en la simulación.
    
- La simulación termina cuando todos los drones han llegado al destino.
    

---

## 9. Sistema de representación visual

La implementación debe proporcionar información visual de la simulación.

Se permite cualquiera de estas opciones:

1. Representación en terminal con colores, mostrando los movimientos de los drones y el estado de las zonas.
    
2. Interfaz gráfica que muestre el grafo y las posiciones de los drones.
    
3. Ambas opciones.
    

Cuando los archivos de entrada incluyen colores, deben utilizarse para proporcionar información visual.

La representación debe facilitar la comprensión de:

- La estructura del mapa.
    
- Las posiciones de los drones.
    
- Los movimientos realizados.
    
- El estado de las zonas.
    

---

## 10. Sistema de puntuación y rendimiento

El criterio principal de evaluación es el número total de turnos necesarios para llevar todos los drones al destino.

**Cuantos menos turnos, mejor puntuación.**

La simulación debe respetar todas las reglas de movimiento, ocupación y capacidad.

Como criterios secundarios pueden considerarse:

- Drones desplazados por turno.
    
- Número medio de turnos por dron.
    
- Coste total de las rutas.
    
- Calidad de la representación visual.
    
- Calidad del código.
    

### Objetivos de rendimiento

|Dificultad|Objetivo|
|---|---|
|Fácil|Menos de 10 turnos|
|Media|Entre 10 y 30 turnos|
|Difícil|Menos de 60 turnos|

### Objetivos concretos de los mapas de prueba

|Mapa|Drones|Objetivo|
|---|---|---|
|Linear path|2|≤ 6 turnos|
|Simple fork|4|≤ 8 turnos|
|Basic capacity|4|≤ 6 turnos|
|Dead end trap|5|≤ 12 turnos|
|Circular loop|6|≤ 15 turnos|
|Priority puzzle|5|≤ 12 turnos|
|Maze nightmare|8|≤ 30 turnos|
|Capacity hell|12|≤ 35 turnos|
|Ultimate challenge|15|≤ 45 turnos|

### Challenger map (opcional)

Existe un mapa adicional llamado `The Impossible Dream`:

- 25 drones.
    
- Récord de referencia: 45 turnos.
    
- Su resolución y la superación del récord son completamente opcionales y no afectan a la nota.
    

---

## 11. Makefile obligatorio

El proyecto debe incluir un `Makefile` con las siguientes reglas:

|Regla|Función|
|---|---|
|`install`|Instalar las dependencias del proyecto.|
|`run`|Ejecutar el programa principal.|
|`debug`|Ejecutar el programa utilizando el debugger de Python, por ejemplo `pdb`.|
|`clean`|Eliminar archivos temporales y cachés.|
|`lint`|Ejecutar flake8 y mypy con los parámetros obligatorios.|
|`lint-strict`|Ejecutar flake8 y mypy en modo estricto (opcional).|

El comando obligatorio de `lint` debe ejecutar:

```
flake8 .
```

```
mypy . \
    --warn-return-any \
    --warn-unused-ignores \
    --ignore-missing-imports \
    --disallow-untyped-defs \
    --check-untyped-defs
```

La regla opcional `lint-strict` debe ejecutar:

```
flake8 .
mypy . --strict
```

---

## 12. README.md obligatorio

Debe existir un archivo `README.md` en la raíz del repositorio.

**El README debe estar escrito en inglés.**

La primera línea debe estar en cursiva y tener exactamente esta estructura:

```
*This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].*
```

Debe incluir como mínimo las siguientes secciones:

### Description

Explicación del proyecto, sus objetivos y una descripción general de su funcionamiento.

### Instructions

Información necesaria para instalar, ejecutar y utilizar el programa.

### Resources

Referencias utilizadas:

- Documentación.
    
- Artículos.
    
- Tutoriales.
    
- Otras fuentes relevantes.
    

También debe describir cómo se ha utilizado la IA, indicando qué tareas y partes del proyecto se han trabajado con ella.

### Requisitos adicionales del README

Además de las secciones anteriores, debe incluir:

1. **Algorithm choices and implementation strategy:** explicación detallada de los algoritmos elegidos y de cómo se han implementado.
    
2. **Visual representation:** documentación de las características visuales y cómo mejoran la experiencia de usuario.
    
3. **Example input and expected output:** ejemplos claros de entradas y sus salidas esperadas.
    

---

## 13. Entrega y estructura del repositorio

Todos los archivos del proyecto deben estar en la raíz del repositorio Git.

El repositorio debe contener una simulación completamente funcional escrita en Python.

Debe incluir:

- Un parser del formato de entrada.
    
- Un motor de simulación que respete las reglas de movimiento y las restricciones de las zonas.
    
- Uno o varios algoritmos de búsqueda de rutas capaces de minimizar los turnos.
    
- Un sistema de representación visual (terminal con colores y/o interfaz gráfica).
    
- Una salida de terminal o log que respete el formato especificado.
    

**Importante:** los mapas utilizados durante la evaluación pueden ser diferentes de los proporcionados en el enunciado. No se deben codificar soluciones específicas para los mapas de ejemplo.

El trabajo que esté dentro del repositorio será el que se evalúe.

Durante la evaluación:

- Debes poder explicar tu código y tus decisiones.
    
- Pueden pedirte que escribas o modifiques código.
    
- Pueden solicitar una pequeña modificación funcional en pocos minutos.
    
- Debes conocer suficientemente bien tu implementación para realizar esos cambios.
    

---

## 14. Bonus (opcional)

Los bonus solamente se evaluarán si todos los requisitos obligatorios están cumplidos.

El enunciado contempla:

- Conseguir exactamente o mejorar todos los objetivos de rendimiento de los mapas proporcionados.
    
- Resolver el mapa `The Impossible Dream` y superar el récord de referencia de 45 turnos.
    

No son necesarios para aprobar.

---

## 15. Checklist final de entrega

### Código y arquitectura

- Python 3.10 o superior.
    
- Programación completamente orientada a objetos.
    
- Sin bibliotecas externas de lógica de grafos.
    
- Código correctamente tipado.
    
- Todas las clases y funciones documentadas con docstrings.
    
- Gestión adecuada de errores y recursos.
    

### Funcionalidad

- Parser de mapas completo.
    
- Validación de todas las reglas de entrada.
    
- Gestión de zonas y conexiones.
    
- Algoritmo de búsqueda de rutas.
    
- Distribución de drones entre rutas.
    
- Simulación de movimientos simultáneos.
    
- Gestión de capacidades de zonas y conexiones.
    
- Gestión de zonas restringidas de dos turnos.
    
- Prevención de conflictos y bloqueos.
    
- Finalización cuando todos los drones llegan al destino.
    
- Salida de movimientos con el formato exigido.
    
- Representación visual funcional.
    

### Calidad y herramientas

- Makefile con `install`, `run`, `debug`, `clean` y `lint`.
    
- `flake8` sin errores.
    
- `mypy` sin errores.
    
- `.gitignore`.
    
- Pruebas de casos normales y extremos.
    

### Documentación

- README.md en inglés.
    
- Primera línea con el formato obligatorio.
    
- Sección Description.
    
- Sección Instructions.
    
- Sección Resources.
    
- Explicación detallada del algoritmo.
    
- Documentación de la representación visual.
    
- Ejemplos de entrada y salida.
    
- Descripción del uso de IA.
    

### Entrega y evaluación

    - Todos los archivos necesarios dentro del repositorio.
    - Código funcional y ejecutable.
    - Sin depender de mapas concretos.
    - Preparado para explicar la implementación.
    - Preparado para realizar pequeñas modificaciones durante la evaluación.

---

## 16. Resumen del objetivo real

El proyecto no consiste simplemente en encontrar el camino más corto entre dos nodos.

Consiste en desarrollar un **planificador de tráfico para una flota de drones**, capaz de:

    1. Interpretar un mapa representado mediante un grafo.
    2. Encontrar rutas teniendo en cuenta los costes de las zonas.
    3. Distribuir los drones entre las rutas disponibles.
    4. Coordinar sus movimientos simultáneos.
    5. Gestionar las capacidades de las zonas y conexiones.
    6. Evitar colisiones, bloqueos y esperas innecesarias.
    7. Minimizar el número total de turnos.
    8. Mostrar visualmente cómo evoluciona la simulación.

La parte algorítmica más importante es la planificación conjunta de los drones: no basta con calcular una ruta óptima individualmente, hay que encontrar una estrategia eficiente para que toda la flota pueda llegar al destino.