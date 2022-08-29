#!/usr/bin/env python3

import collections
point = collections.namedtuple('Point',['x','y'])
x1 = point(3,4)
print(x1)
x1 = point(4,4)
print(x1)
print(dir(collections))
