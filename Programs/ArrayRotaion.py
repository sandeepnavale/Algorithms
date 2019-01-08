
import unittest
class Test(unittest.TestCase):
    def testArrayRotation1(self):
        a = [1, 2, 3, 4, 5]
        res =  arrayRotation(a, 2)
        self.assertAlmostEqual(res,[4, 5, 1, 2, 3])

    def testArrayRotation2(self):
        a = []
        res =  arrayRotation(a, 2)
        self.assertAlmostEqual(res,[])

    def testArrayRotation3(self):
        a = [1,2,3,4,5,6,7,8,9,10]
        res =  arrayRotation(a, 5)
        # print(res)
        self.assertAlmostEqual(res,[6, 7, 8, 9, 10, 1, 2, 3, 4, 5])

def arrayRotation(a,n):
    if len(a)>2:
        for i in range(n):
            ele = a.pop()
            a.insert(0,ele)
    return a



if __name__ == '__main__':
    unittest.main()