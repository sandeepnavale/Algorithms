class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class ASingleton(object):
    __metaclass__ = Singleton


a = ASingleton()
b = ASingleton()
import ipdb; ipdb.set_trace()

print(a is b)
print(a.__class__.__name__, b.__class__.__name__)

class BSingleton(object):
    __metaclass__ = Singleton

c = BSingleton()
d = BSingleton()

print(c.__class__.__name__, d.__class__.__name__)
print(id(a),id(b),id(c),id(d))
