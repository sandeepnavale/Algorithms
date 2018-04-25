
# Count occurance of element in list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))
test2 = [1, 11, 1, 1111, 1, 2, 3, 4, 666, 6, 6, 6, 6, 6]
print(max(set(test2), key=test2.count))
