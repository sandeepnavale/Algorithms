class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class ASingleton(metaclass = Singleton):
    # __metaclass__ = Singleton  THIS don't work in python 
    pass 

a = ASingleton()
b = ASingleton()

print(a is b)
print(a.__class__.__name__, b.__class__.__name__)

class BSingleton(metaclass = Singleton):
    # __metaclass__ = Singleton this don;t work in Python 3
    pass

c = BSingleton()
d = BSingleton()

print(c.__class__.__name__, d.__class__.__name__)
print(id(a)==id(b),id(c)==id(d))
print(id(a),id(b),id(c),id(d))
