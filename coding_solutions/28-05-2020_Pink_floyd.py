n=6
f=0
l=[1,4,9,5,7,8,9]
print(l)

for i in range(0,len(l)-1):
    if l[i]<=l[i+1]:
        f=1
    else:
        f=0
        break
if f==0:
    print('Pink is Happy')
else:
    print('Pink is Sad')
