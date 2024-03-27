
def causeError():
    try:
        return 1/0
    except Exception as e:
        return e


causeError()

x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


