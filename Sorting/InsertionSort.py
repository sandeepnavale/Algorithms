import unittest

def InsertionSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        count = 0
        while key < a[j] and j>=0:
            a[j+1] = a[j]
            count += 1
            j -= 1
        print(count)

        a[j+1] = key

a = [2,1,3,1,2]
InsertionSort(a)
print(a)


class Test(unittest.TestCase):
    def test1(self):
        a = [2, 1, 3, 1, 2]
        InsertionSort(a)
        self.assertEqual(a,[1, 1, 2, 2, 3])

    def test2(self):
        a = [1, 1, 1, 1, 2]
        InsertionSort(a)
        self.assertEqual(a, [1, 1, 1, 1, 2])


if __name__ == '__main__':
    unittest.main()
