class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def calculateGain(a,b):
            return ((a+1)/(b+1))-(a/b)
        maxHeap=[]
        for a,b in classes:
            gain=calculateGain(a,b)
            heapq.heappush(maxHeap,(-gain,a,b))
        for _ in range(extraStudents):
            cg,a,b=heapq.heappop(maxHeap)
            heapq.heappush(maxHeap,(-calculateGain(a+1,b+1),a+1,b+1))
        total_pass_ratio=0
        while maxHeap:
            _,a,b=heapq.heappop(maxHeap)
            total_pass_ratio+=a/b
        return total_pass_ratio/len(classes)
