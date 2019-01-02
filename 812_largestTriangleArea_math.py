class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def area(x1, y1, x2, y2, x3, y3):
            return (x1 * y2 + y1 * x3 + x2 * y3 - x1 * y3 - y1 * x2 - y2 * x3) / 2
        maxArea = 0
        length = len(points)
        for i in range(length):
            for j in range(length):
                if i != j:
                    for k in range(length):
                        if k != i and k != j:
                            maxArea = max(maxArea, area(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]))
        return maxArea