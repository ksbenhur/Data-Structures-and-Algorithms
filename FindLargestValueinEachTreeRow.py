# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        tree=deque([root])
        res=[]
        while tree:
            cur_max=float("-inf")
            for _ in range(len(tree)):
                node=tree.popleft()
                cur_max=max(node.val,cur_max)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            res.append(cur_max)

        return res
