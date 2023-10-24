# Validate Binary Tree Nodes


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        indegree = [0] * n

        for u in range(n):
            for child in (leftChild[u], rightChild[u]):
                if child != -1: indegree[child] += 1    

        
        q = [u for u in range(n) if not indegree[u]]

        print(q)

        if len(q) != 1: return False

        vis = [False] * n
        vis[q[0]] = True

        for u in q:
            for v in (leftChild[u], rightChild[u]):
                if v == -1: continue
                if vis[v]: return False
                vis[v] = True
                q.append(v)
        

        return all(vis)
        