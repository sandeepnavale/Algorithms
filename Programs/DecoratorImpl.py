from functools import wraps

# Decorators,
# Two types Function decorators & Class decorators.

# Class Decorator.
class DecoClass:
    def __init__(self,f):
        """ This is called before object initialization. ie. without f()"""
        self.func = f
        print(f'\t Initialized the {self.func.__name__} in decorator')

    def __call__(self, *args, **kwargs):
        print(f'Entering Class Decorator for {self.func.__name__}')
        self.func(*args, **kwargs)
        print(f'Exiting Class Decorator {self.func.__name__} \n')

@DecoClass
def f1(a):
    print(f'Inside f1 with argument {a}')

@DecoClass
def f2(a):
    print(f'Inside f2 with argument {a}')

# Uses Class decoration.
f1("Sandeep")
f1('NLS') # Note: __init__() is not called this time, only __call__()
f2('Sunny')


# Function decorators
def DecoFunc(f):
    wraps(f)
    def wrapperFunc(*args,**kwargs):
        print('Function Deco Wrapper Entry')
        res = f(*args,**kwargs)
        print('Function Deco Wrapper Exit \n')
        return res
    return wrapperFunc

@DecoFunc
def fun1(a):
    print(f'Executing fun1 with arg {a}')

def fun2(b):
    print(f'Executing fun2 with arg {b}')

fun1('Arg1')
fun2('No Deco')
print(f'{fun1.__name__} as its been decorated')
print(f'{fun2.__name__} as its NOT been decorated')



