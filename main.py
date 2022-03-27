import os.path

directory = "C:\\tmp\\"
filename = "decorator_logs.txt"
filepath = os.path.join(directory, filename)

# Directory is created if it doesn't exist already
if not os.path.isdir(directory):
    os.mkdir(directory)


# Declaring the decorator function
def log_message(function):
    """Takes a function and writes the function's return value in decorator_logs.txt on a new line """

    def write_function(*args, **kwargs):
        result = function(*args, **kwargs)
        file = open(filepath, "a")
        file.write(result + "\n")
        file.close()

        # Confirmation message is written to console
        print("Content has successfully been written to the /tmp/decorator_logs.txt file")

    return write_function


# Decorator function being used with example functions
@log_message
def hello():
    return "Hello world"


@log_message
def message(msg=""):
    return f"Message: {msg}"


# Function calls
hello()
message(msg="This is a test message")
