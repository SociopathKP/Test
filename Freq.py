l=list(map(int,input().split())
f={}
for i in l:
  if i in f:
    f[i]+=1
  else:
    f[i]=1
