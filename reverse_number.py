N=int(input())
s=0
while N>0:
   r=N%10
   s=s*10+r
   N=N//10
print(s)
