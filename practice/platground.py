def add(*args):
    for n in args:
        print(n)

add(3, 5, 6, 7, 8)

def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])

def calculate2(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(add=5, multiple=10)

calculate2(2, add=3, multiply=5)