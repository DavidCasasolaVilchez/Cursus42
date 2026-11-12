.PHONY: run clean install debug lint lint-strict re
.SILENT:

#? run
NAME = fly_in.py
VENV = venv
PYTHON = $(VENV)/bin/python3
PYTHON_FLAG = -m
MAP ?= maps/challenger/01_the_impossible_dream.txt

#? EASY
E1 = maps/easy/01_linear_path.txt
E2 = maps/easy/02_simple_fork.txt
E3 = maps/easy/03_basic_capacity.txt

#? MEDIUM
M1 = maps/medium/01_dead_end_trap.txt
M2 = maps/medium/02_circular_loop.txt
M3 = maps/medium/03_priority_puzzle.txt

#? HARD
H1 = maps/hard/01_maze_nightmare.txt
H2 = maps/hard/02_capacity_hell.txt
H3 = maps/hard/03_ultimate_challenge.txt

#? CHALLENGER
C1 = maps/challenger/01_the_impossible_dream.txt

#? install
PIP = pip
INSTALL = install
FREEZE = freeze
REQUIREMENTS_FILE = requirements.txt
DEPENDENCES = mypy flake8 pudb

#? lint
MYPY = mypy
MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
FLAKE8 = flake8
STRICT = --strict
FILES = Models/*.py Utils/*.py fly_in.py

#? debug
DEBUG = pudb

#? format
CLEAR = clear
ECHO = echo

#? clean
RM = rm
RMFLAGS = -rf


install: $(VENV)/bin/activate
	$(PYTHON) $(PYTHON_FLAG) $(PIP) $(INSTALL) $(DEPENDENCES)
	$(PYTHON) $(PYTHON_FLAG) $(PIP) $(FREEZE) > $(REQUIREMENTS_FILE)
	$(CLEAR)


run: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(MAP)

#? EASY

run_e1: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(E1)

run_e2: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(E2)

run_e3: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(E3)

#? MEDIUM

run_m1: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(M1)

run_m2: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(M2)

run_m3: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(M3)

#? HARD

run_h1: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(H1)

run_h2: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(H2)

run_h3: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(H3)

#? CHALLENGER

run_c1: $(VENV)/bin/activate install
	$(PYTHON) $(NAME) $(C1)


debug: $(VENV)/bin/activate install
	$(PYTHON) $(PYTHON_FLAG) $(DEBUG) $(NAME)


lint: $(VENV)/bin/activate install
	$(ECHO) "###? MYPY ###"
	$(PYTHON) $(PYTHON_FLAG) $(MYPY) $(FILES) $(MYPY_FLAGS)
	$(ECHO) "###? FLAKE8 ###"
	$(PYTHON) $(PYTHON_FLAG) $(FLAKE8) $(FILES)


lint-strict: $(VENV)/bin/activate install
	$(ECHO) "###? MYPY ###"
	$(PYTHON) $(PYTHON_FLAG) $(MYPY) $(FILES) $(MYPY_FLAGS) $(STRICT)
	$(ECHO) "###? FLAKE8 ###"
	$(PYTHON) $(PYTHON_FLAG) $(FLAKE8) $(FILES)


$(VENV)/bin/activate:
	python3 $(PYTHON_FLAG) venv $(VENV)


clean:
	find . -type d -name '__pycache__' -prune -exec $(RM) $(RMFLAGS) -- {} +
	find . -type d -name '.mypy_cache' -prune -exec $(RM) $(RMFLAGS) -- {} +
	$(RM) $(RMFLAGS) $(VENV)


re: clean run