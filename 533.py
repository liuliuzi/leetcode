import collections
class Solution(object):
    def findLonelyPixel(self, picture,N):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows, cols = [0] * len(picture),  [0] * len(picture[0])
        lookup = collections.defaultdict(int)
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
            lookup[tuple(picture[i])] += 1

        result = 0
        for i in range(len(picture)):
            if rows[i] == N and lookup[tuple(picture[i])] == N:
                for j in range(len(picture[0])):
                    result += picture[i][j] == 'B' and cols[j] == N
        return result