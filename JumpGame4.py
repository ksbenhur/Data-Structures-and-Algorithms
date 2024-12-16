from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n<=1:
            return 0
        if arr[0]==arr[n-1]:
            return 1
        
        visited=set()
        q=collections.deque()
        mp=collections.defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)
        q.append(0)
        visited.add(0)

        def bfs():
            min_jumps=0
            while q:
                for _ in range(len(q)):
                    idx=q.popleft()

                    if idx==n-1:
                        return min_jumps
                    
                    next=idx+1
                    prev=idx-1
                    same_val=mp[arr[idx]]

                    if next not in visited:
                        q.append(next)
                        visited.add(next)

                    if prev>=0 and prev not in visited:
                        q.append(prev)
                        visited.add(prev)
                    
                    if same_val:
                        for i in same_val:
                            if i not in visited:
                                q.append(i)
                                visited.add(i)
                        del mp[arr[idx]]
                min_jumps+=1
            return min_jumps

        return bfs()
        
        
          
        
