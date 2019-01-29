class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        array = [0]
        tar = len(graph) - 1

        def find(level):
            for n in graph[level]:
                if n not in array:
                    array.append(n)
                    if n == tar:
                        res.append(array[:])
                    else:
                        find(n)
                    array.pop(-1)

        find(0)
        return res