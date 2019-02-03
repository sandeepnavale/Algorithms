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
        # print(count)

        a[j+1] = key

# a = [2,1,3,1,2]
# InsertionSort(a)
# print(a)

def insertionSort2(seq):
    for i in range(1,len(seq)):
        j = i
        while j>0 and seq[j-1] < seq[j]:
            seq[j-1],seq[j] = seq[j],seq[j-1]
            j -= 1
    # print(seq)

# a = [2,1,3,1,2]
import ipdb; ipdb.set_trace()
a = [5,1,4,6,2,7,1,1]
insertionSort2(a)
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

    def test3(self):
        a = [7, 6, 5, 4, 2, 1, 1, 1]
        insertionSort2(a)
        self.assertEqual(a, 
        [7, 6, 5, 4, 2, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
