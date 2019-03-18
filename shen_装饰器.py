import time
def print_time(t):
    def wrapper(*args, **kwargs):
        print("Time:", time.ctime())
        return t(*args, **kwargs)
    return wrapper

# @print_time
def say_hello():
    print("hello python")
# say_hello()
say_hello2 = print_time(say_hello)
say_hello2()

