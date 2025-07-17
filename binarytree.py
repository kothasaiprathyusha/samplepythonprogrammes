class TreeNode:
    def __init__(self,val):
        self.data=val  
        self.left=None
        self.right=None
def create_btree(arr,i,n):
         if i<n:
            return None
         root=TreeNode(arr[i-1])
         root.left=create_btree(arr,2*i,n)
         root.right=create_btree(arr,2*i+1,n)
         return root
def preorder(root):
    if root is None:
          return 
    print(root.data,end="")
    preorder(root.left)
    preorder(root.right)
arr=list(map(int,input().split(",")))
binarytree=create_btree(arr,1,len(arr))
preorder(binarytree)     