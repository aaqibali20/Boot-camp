class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        N, M = len(matrix), len(matrix[0])
        result = []

        for d in range(N + M - 1):
            temp = []
            r = 0 if d < M else d - M + 1
            c = d if d < M else M - 1

            while r < N and c >= 0:
                temp.append(matrix[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)

        return result