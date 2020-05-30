def right_rotate(l,n):
    result=[]
    for i in range(len(l)-n,len(l)):
        result.append(l[i])
    for j in range(0,len(l)-n):
        result.append(l[j])
    return result
k=int(input('enter a step to right rotate:'))
l=[1,2,3,4,5,6]
print(right_rotate(l,k))
