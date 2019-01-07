import heapq


class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.queue = []
        heapq.heapify(self.queue)
        for i, n in enumerate(nums):
            if i < k:
                heapq.heappush(self.queue, n)
            elif n > self.queue[0]:
                heapq.heappop(self.queue)
                heapq.heappush(self.queue, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if not self.queue or len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
        elif val > self.queue[0]:
            heapq.heappop(self.queue)
            heapq.heappush(self.queue, val)
        return self.queue[0]
