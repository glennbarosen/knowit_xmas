def readFile(filename):
    f = open(filename, "r")
    return f.read()


# matrix search from GeeksforGeeks
class GFG:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    # This function searches in all 8-direction
    # from point(row, col) in grid[][]
    def search2D(self, grid, row, col, word):

        # If first character of word doesn't match
        # with the given starting point in grid.
        if grid[row][col] != word[0]:
            return False

        # Search word in all 8 directions
        # starting from (row, col)
        for x, y in self.dir:

            # Initialize starting point
            # for current direction
            rd, cd = row + x, col + y
            flag = True

            # First character is already checked,
            # match remaining characters
            for k in range(1, len(word)):

                # If out of bound or not matched, break
                if (0 <= rd < self.R and 0 <= cd < self.C
                        and word[k] == grid[rd][cd]):

                    # Moving in particular direction
                    rd += x
                    cd += y
                else:
                    flag = False
                    break

            # If all character matched, then
            # value of flag must be false
            if flag:
                return True
        return False

    # Searches given word in a given matrix
    # in all 8 directions
    def patternSearch(self, grid, word, accWords):

        # Rows and columns in given grid
        self.R = len(grid)
        self.C = len(grid[0])

        # Consider every point as starting point
        # and search given word
        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    accWords.append(word)


if __name__ == '__main__':
    accWords = []
    missingWords = []

    words = readFile("words.txt").split("\n")
    dir = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1],
           [0, -1]]
    grid = readFile("matrix.txt").split("\n")
    gfg = GFG()
    for i in words:
        gfg.patternSearch(grid, i, accWords)

for word in words:
    if word not in accWords:
        missingWords.append(word)

print(len(accWords))
print(len(words))
print(missingWords)
