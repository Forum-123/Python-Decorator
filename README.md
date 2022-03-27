## Python Decorator

### Purpose

A Python decorator that takes whatever the decorated function returns, and writes it to a file in a new line. 

For this problem, it is assumed the decorated functions always return a string.

The decorator is called `log_message` and writes to the file `C:/tmp/decorator_logs.txt`.

### Usage

1. In the terminal, use the command `python main.py` to launch the Python script.
- A `decorator_logs.txt` file in the `C:/tmp` directory will be created.
- This file will contain the outputs from the functions that use the decorator written in the `main.py` script.
- There will be a confirmation message returned in the terminal for every example function run successfully.