def anagramcheck(s,t):
    return sorted(s)==sorted(t)
s=input()
t=input()
print(anagramcheck(s,t))
