def outer_func(y):
    x=2
    def inner_func():
        return x + y
    x=x+2
    y=2
    return inner_func

results = outer_func(3)
print(results()) 

 # This will print 5