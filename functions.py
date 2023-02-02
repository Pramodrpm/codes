def O_func(x):
    def i_func(y):
        return x*y
    return i_func

my_func=O_func(2)
print(my_func(3))