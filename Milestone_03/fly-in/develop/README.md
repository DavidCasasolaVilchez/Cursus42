*This project has been created as part of the 42 curriculum by dcasasol.*

# Fly-in

## Description

Fly-in is a Python 3.10 project that simulates a fleet of drones travelling
through a network of connected zones. The program parses a textual map,
constructs the corresponding graph, finds routes from a start hub to an end
hub, and schedules drone movements while considering zone types, zone
capacities, connection capacities, and simultaneous movement.

The main goal is to deliver every drone to the destination in as few
simulation turns as possible. The project is based on the Fly-in subject,
whose central challenge is to combine graph traversal with capacity-aware
turn scheduling.

The implementation is organised into:

- `Models/`: zones, connections, drones, routes, networks, and execution;
- `Utils/`: parsing, path selection, movement, colours, enums, and exceptions;
- `maps/`: sample maps grouped by difficulty;
- `fly_in.py`: the application entry point;
- `Makefile`: installation, execution, debugging, linting, and cleaning tasks.

## Features

- Parsing of `nb_drones`, `start_hub`, `end_hub`, `hub`, and `connection`
  declarations.
- Optional zone metadata:
  `zone`, `color`, and `max_drones`.
- Optional connection metadata:
  `max_link_capacity`.
- Normal, restricted, priority, and blocked zone types.
- Connections linked to both endpoint zones in the network model.
- Capacity-aware movement of several drones during the same turn.
- Route selection that considers movement cost, congestion, and priority zones.
- Coloured terminal feedback for zone and drone activity.
- Easy, medium, hard, and challenger example maps.

## Algorithm and implementation strategy

### Map parsing

`NetworkParser` reads a map file with a context manager and converts each
declaration into domain objects. Zones store their coordinates, type, colour,
and maximum occupancy. Connections store their endpoints and their maximum
number of simultaneous drones.

After parsing, the network validates the number of drones, zone names,
coordinates, capacities, and connection endpoints. Connections are then linked
to both endpoint zones so that each zone knows about its incident connections.

### Route selection

The path-selection routine explores candidate routes without using an external
graph library. A route keeps its visited zones, accumulated weight, and
priority score. Candidate routes are ordered by:

1. total estimated weight;
2. preference for priority zones when weights are equal.

Blocked zones are excluded from candidate routes, and cycles are avoided by
checking whether a zone is already present in the current route. The route
weight includes the movement cost of the destination zone and congestion
information from waiting drones and occupied zones.

### Turn scheduling

The execution loop advances the simulation one turn at a time. For each drone
that has not reached the end hub, it selects a route and attempts to move to
the next zone. A movement is accepted only when:

- the destination zone has available capacity, unless it is the end hub;
- the connection has available capacity;
- the destination is not blocked.

When a movement cannot be performed, the drone is placed in a waiting
collection and can be considered on a later turn. The simulation stops after
all drones have reached the end hub. If a complete turn makes no progress, the
execution raises an explicit runtime error instead of looping forever.

Restricted zones have a movement cost of two turns. Priority zones have a
movement cost of one turn and receive a preference during route comparison.
The `Dron` and `Connection` models retain the state needed to represent drones
moving through the network.

## Visual representation

The simulation prints each movement to the terminal and uses ANSI colours
when a map provides a `color` attribute. This makes it possible to distinguish
zones and movement events while following the simulation. Zones without a
recognised colour use the default terminal colour, and the colour helper also
supports a rainbow display for uncoloured visual information.

The visual output is useful during peer evaluation because it exposes:

- the order in which drones are scheduled;
- the route selected for each drone;
- congestion at shared zones and connections;
- the moment at which drones reach the destination.

## Instructions

### Requirements

- Python 3.10 or later;
- `make`;
- `pip`;
- a terminal capable of displaying ANSI colour sequences.

The project dependencies are listed in `requirements.txt`. Development
dependencies include `mypy`, `flake8`, and `pudb`.

### Installation

From this directory:

```bash
make install
```

This creates the local `venv` virtual environment, installs the development
dependencies, and refreshes `requirements.txt`.

Alternatively, the main program can be run with an already available Python
environment:

```bash
python3 -m venv venv
./venv/bin/python -m pip install -r requirements.txt
```

### Execution

The default entry point runs the challenger map configured in
`fly_in.py`:

```bash
make run
```

To run another map, execute the entry point from this directory and update the
map path in `fly_in.py`, or import `NetworkParser` and `Execution` from a
small Python driver:

```python
from Models.Execution import Execution
from Utils.NetworkParser import NetworkParser

parser = NetworkParser("maps/easy /01_linear_path.txt")
parser.parse_file()
Execution(parser.network).run()
```

The available Makefile targets are:

```text
make install       Install project dependencies
make run           Run the default simulation
make debug         Run the program with pudb
make lint          Run flake8 and the required mypy checks
make lint-strict   Run flake8 and mypy --strict
make clean         Remove caches and the virtual environment
make re            Clean and run again
```

### Static checks

The required checks can be run with:

```bash
make lint
```

The project uses the following mypy flags in the regular lint target:

```text
--warn-return-any
--warn-unused-ignores
--ignore-missing-imports
--disallow-untyped-defs
--check-untyped-defs
```

## Map format

A map is a plain-text file. Comments begin with `#` and are ignored.

```text
nb_drones: 2
start_hub: start 0 0 [color=green]
end_hub: goal 3 0 [color=yellow]
hub: corridor 1 0 [zone=priority color=blue max_drones=2]
hub: landing 2 0 [zone=normal]
connection: start-corridor [max_link_capacity=2]
connection: corridor-landing
connection: landing-goal
```

The supported zone types are:

- `normal`: one-turn movement, the default;
- `restricted`: two-turn movement;
- `priority`: one-turn movement and a path-selection preference;
- `blocked`: inaccessible to drones.

`max_drones` limits occupancy of regular zones. The start and end hubs are
special: all drones may begin at the start hub, and any number of drones may
arrive at the end hub. `max_link_capacity` limits the number of drones that
can use a connection simultaneously.

## Example input and expected output

For the map above, the simulation may produce the following logical movement
output:

```text
D1-corridor D2-corridor
D1-landing D2-landing
D1-goal D2-goal
```

Each line represents one simulation turn. A drone that waits is omitted from
that line. The terminal implementation also displays turn labels and colour
escape sequences to make the simulation easier to follow interactively.

The repository includes ready-to-run examples:

```text
maps/easy /01_linear_path.txt
maps/easy /02_simple_fork.txt
maps/easy /03_basic_capacity.txt
maps/medium/01_dead_end_trap.txt
maps/medium/02_circular_loop.txt
maps/medium/03_priority_puzzle.txt
maps/hard/01_maze_nightmare.txt
maps/hard/02_capacity_hell.txt
maps/hard/03_ultimate_challenge.txt
maps/challenger/01_the_impossible_dream.txt
```

## Resources

### Classic references

- [Python documentation: Classes](https://docs.python.org/3/tutorial/classes.html)
  — object-oriented modelling in Python.
- [Python documentation: Regular expressions](https://docs.python.org/3/library/re.html)
  — parsing the map syntax.
- [Python documentation: `enum`](https://docs.python.org/3/library/enum.html)
  — representing zone types.
- [Python documentation: `typing`](https://docs.python.org/3/library/typing.html)
  — type annotations used throughout the project.
- [Python documentation: `venv`](https://docs.python.org/3/library/venv.html)
  — isolated development environments.
- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
  — static type checking.
- [Flake8 documentation](https://flake8.pycqa.org/en/latest/)
  — Python style and linting checks.
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
  — background for weighted shortest-path problems.
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
  — background for graph exploration.

### AI usage

AI was used as a development and review aid, not as a replacement for
understanding the implementation. It helped with:

- checking the Fly-in subject requirements against the project structure;
- identifying edge cases for map parsing, capacities, cycles, and restricted
  zones;
- suggesting test scenarios for route selection and turn scheduling;
- reviewing Makefile commands, typing checks, and documentation structure;
- drafting and proofreading this README.

The final algorithm, data model, parser behaviour, and simulation decisions
were reviewed against the source code and tested locally by the project
author. The project author remains responsible for explaining and defending
all submitted code during peer evaluation.
