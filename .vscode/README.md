

# Introduction

This is a skeleton Python project structure that will help you start solving the problem right away.

## Tools available to you

- Python 3
- pip — Python package manager
- unittest — Python's built-in unit testing framework

## Structure

- **`main.py`** — This is where you should write your solution. It contains the main application/driver code.
- **`test_sample.py`** — Contains sample unit tests. You can add additional test files as required.
- **`run.sh`** — Compiles/checks and runs your solution against the provided command-line inputs.
- **`run_unittests.sh`** — Runs all unit tests in the project.

## How to run your solution

Use the provided `run.sh` script to run your solution against custom inputs.

```bash
./run.sh '<input 1>' '<input 2>'
```

For example:

```bash
./run.sh 'PLACE_ORDER 101 Apple 5' 'TOTAL_COST 101'
```

Each complete input command should be wrapped in single quotes.

## Checking for correctness

You can click the **Test My Code** button from the interview application.

This will run your solution against preconfigured test inputs and display the output.

You can also test your solution locally using `run.sh`:

```bash
./run.sh '<input 1>' '<input 2>'
```

For example:

```bash
./run.sh 'PASSENGER ADULT 2' 'TOTAL_COST'
```

## How to run unit tests

- Everything required to run and write unit tests has already been configured.
- Run:

```bash
./run_unittests.sh
```

- The script will discover and execute the unit tests in the project.
- Test files should follow Python's test naming convention:

```text
test_*.py
```

For example:

```text
test_sample.py
test_cart.py
test_order.py
```

You can also run the tests directly using Python:

```bash
python3 -m unittest discover
```

## Scripts available to you

You can run the following commands from the terminal:

- `./run.sh '<input 1>' '<input 2>'` — Runs your solution against the provided inputs.
- `./run_unittests.sh` — Runs all unit tests.

