a=int(input())
b=int(input())
c=int(input())
n=int(input())
def task(a,b,c,n):
    arr=[a,b,c]
    count=0
    for i1 in arr:
        for i2 in arr:
            for i3 in arr:
                z=i3*100+i2*10+i1
                if z>=100 and z<=n:
                    count+=1
    return count
    
print(task(a,b,c,n))
