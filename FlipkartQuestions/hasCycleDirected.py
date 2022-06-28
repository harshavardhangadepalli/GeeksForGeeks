#User function Template for python3
flag = False
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        global flag
        flag = False
        def recursion(node,visited):
            if node in s:
                visited[node] = False
                return
            global flag
            if flag==True:
                # this is the condition where a cycle exists
                # we need to break everything
                return
            for child_node in adj[node]:
                # visit the child, mark as visited
                #if the child is already visited, this means that there is a cycle
                if visited[child_node] == True:
                    # print("yay")
                    # print(child_node)
                    # print("yay")
                    flag = True
                    break
                visited[child_node] = True
                recursion(child_node,visited)
                visited[child_node] = False
            s.add(node)
            visited[node] = False
            return
        visited = [False for _ in range(V)]
        s = set()
        for i in range(V):
            visited[i] = True
            recursion(i,visited)
            visited[i] = False
            if flag==True:
                return True
        return False


print(Solution().isCyclic(6,
    [
        [],
        [2],
        [4],
        [1],
        [0],
        [3]
    ]
    ))