import sys

class LCS:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.m = len(X)
        self.n = len(Y)
        self.L = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]

    def compute_lcs(self):
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                if self.X[i-1] == self.Y[j-1]:
                    self.L[i][j] = self.L[i-1][j-1] + 1
                else:
                    self.L[i][j] = max(self.L[i-1][j], self.L[i][j-1])
        return self.L

    def get_lcs(self):
        self.compute_lcs()
        index = self.L[self.m][self.n]
        lcs = [""] * (index+1)
        i = self.m
        j = self.n
        while i > 0 and j > 0:
            if self.X[i-1] == self.Y[j-1]:
                lcs[index-1] = self.X[i-1]
                i -= 1
                j -= 1
                index -= 1
            elif self.L[i-1][j] > self.L[i][j-1]:
                i -= 1
            else:
                j -= 1
        return "".join(lcs)

for line in sys.stdin:
    if line.strip() != "":
        X, Y = line.strip().split(";")
        lcs = LCS(X, Y)
        print(lcs.get_lcs(), end="")