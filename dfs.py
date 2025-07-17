def depthfirstsearch(i,visited,adj,ans):
    visited[i]=1
    ans.append(i)
    for it in adj[i]:
        if(visited[it]==0):
            depthfirstsearch(it,visited,adj,ans)
def dfs(adj):
    v=len(adj)
    visited=[0]*v
    ans=[]
    for i in range(0,v):#for unconnected but also work for the conneced components
        if visited[i]==0:
            depthfirstsearch(i,visited,adj,ans)
    return ans        
adj=[[1,2],[0,3,4],[0,5,7],[1],[1],[2,6],[5,7],[2,6]]
print(dfs(adj))
