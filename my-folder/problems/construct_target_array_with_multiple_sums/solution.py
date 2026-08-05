import heapq
class Solution(object):
    def isPossible(self, target):
        minHeap = [-n for n in target]
        heapq.heapify(minHeap)
        x = sum(target)
        while minHeap[0] != -1:
            a = -heapq.heappop(minHeap)
            rest = x - a
            if rest == 1: return True
            if rest <= 0 or a <= rest or rest == 0: return False
            prev = a % rest
            if prev == 0: return False
            x -= a
            x += prev
            heapq.heappush(minHeap, -prev)
        return True
        
        