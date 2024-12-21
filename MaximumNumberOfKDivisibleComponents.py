class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        # Helper function for DFS
        def dfs(node, parent):
            subtree_sum = values[node]  # Start with the value of the current node
            components = 0
        
            for neighbor in tree[node]:
                if neighbor != parent:
                    child_sum, child_components = dfs(neighbor, node)
                    if child_sum % k == 0:
                        components += child_components + 1  # Valid split
                    else:
                        subtree_sum += child_sum
                        components += child_components

            return subtree_sum, components

        # Perform DFS starting from node 0
        total_sum, max_components = dfs(0, -1)

        # Check if the total tree can form another component
        if total_sum % k == 0:
            max_components += 1

        return max_components
