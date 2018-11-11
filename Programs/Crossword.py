def copy(mat):  # function for making copy of list of lists
    return [[elem for elem in row] for row in mat]


def output(grid):  # print list of lists as grid
    for row in grid:
        print(*row, sep="")


def solve(grid, words):  # recursive function to place words in grid
    if words:  # try to insert words if there are words to insert
        word = words.pop()  # take one word
        for x in range(len(grid)):  # first iterate over grid rows
            # j represents the number of letters in word that we were able to match in the blank
            row, j = grid[x], 0
            for i in range(len(row)):
                # if whole word match is found stop searching
                if row[i] == "+" and j == len(word):
                    break
                # keep matching '-' or letters to letters in words
                elif row[i] == "-" or row[i] == word[j]:
                    if j == 0:
                        begin = i  # maybe the beginning of a match so mark it
                    j += 1  # current letter of word matched so try next
                else:
                    j = 0  # current letter is a mismatch so reset all previous letter matches
            if j == len(word):  # if match is found place the word and try further
                new_grid = copy(grid)
                new_grid[x][begin:begin+j] = word  # fill the word in the row
                # if further matches could not be made, sol will be None
                sol = solve(new_grid, words[:])
                if sol:
                    return sol  # if all matches were made sol is the answer

        for x in range(len(grid[0])):  # iterate over columns
            row = [line[x] for line in grid]  # represent the column as a list
            j = 0  # j represents the number of letters in word that we were able to match in the blank
            for i in range(len(row)):  # iterate over each character in the column
                # if a whole word match is found stop searching
                if row[i] == "+" and j == len(word):
                    break
                # keep matching '-' or letters to letters in words
                elif row[i] == "-" or row[i] == word[j]:
                    if j == 0:
                        begin = i  # maybe the beginning of a match so mark it
                    j += 1  # current letter of word matched so try next
                else:
                    j = 0  # current letter is a mismatch so reset all previous letter matches
            if j == len(word):  # if match is found place the word and try further
                new_grid = copy(grid)
                for i, ch in enumerate(word):  # fill the word in the column
                    new_grid[begin+i][x] = ch
                # if further matches could not be made, sol will be None
                sol = solve(new_grid, words[:])
                if sol:
                    return sol  # if all matches were made sol is the answer
        return None  # if no match was found, return None
    return grid  # if there are no words left to fill, return the grid


# grid = [[ch for ch in input()] for i in range(10)]
s1 = """+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++"""

grid = s1.split('\n')
# words = input().split(';')
wordsTest = 'LONDON;DELHI;ICELAND;ANKARA'
words = wordsTest.split(';')
output(solve(grid, words))
