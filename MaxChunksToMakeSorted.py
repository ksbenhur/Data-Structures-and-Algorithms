class Solution:
    def maxChunksToSorted(self, arr):
        s=deque()
        for i in range(len(arr)):
            if not s or arr[i]>s[-1]:
                s.append(arr[i])
            else:
                top=s[-1]
                while s and arr[i]<s[-1]:
                    s.pop()
                s.append(top)
        return len(s)
