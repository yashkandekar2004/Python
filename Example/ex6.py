# write a python program to access the function inside a function
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()