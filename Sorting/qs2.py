
import unittest


def qs(a):
    if (len(a) <= 1):
        return a
    ls, pi, rs = parition(a)
    return qs(ls)+[pi]+qs(rs)


def parition(a):
    pivot, rest = a[0], a[1:]
    ls = [x for x in rest if x < pivot]
    rs = [y for y in rest if y > pivot]
    return ls, pivot, rs


class testQS(unittest.TestCase):
    def testQS1(self):
        result = qs([1, 3, 55, 6, 2])
        self.assertEqual(result, [1, 2, 3, 6, 55])

    def testQS2(self):
        result = qs([111, 3, 1, 55, 222])
        self.assertEqual(result, [1, 3, 55, 111, 222])


# test quick sort
if __name__ == '__main__':
    unittest.main()
