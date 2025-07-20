'''init=int(input())
last=int(input())
for i in range(init,last+1):
    n=i
    res=0
    while n>0:
        rem=n%10
        res=res+rem
        n=n//10
        
    if res%2==0:
        print(i) '''   


min=int(input())
n=list(map(int,input().split()))
l=len(n)
counted=set()
for i in range(0,l):
    if n[i] not in counted:
        count=0
        for j in range(l):
            if n[i]==n[j]:
               count=count+1
        print(counted.add(n[i]))       
    

        
