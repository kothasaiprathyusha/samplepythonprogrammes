n=int(input())
target=int(input())
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
          sum=i+j+k
        if(sum==target):
          print(i,j,k)
      