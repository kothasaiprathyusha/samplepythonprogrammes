
arr=([4,7,8],[7,9,2],[3,6,8])
trans=[]
for i in arr:
    for j in arr:
        arr[i],arr[j]=arr[j],arr[i]
        trans=arr[i],arr[j]
print(trans)  
