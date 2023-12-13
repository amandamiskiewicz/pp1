def f(arr2D):
    sum=0
    for i in range(0,len(arr2D)):
        if arr2D[i][0]>0 and arr2D[i][1]>0:
            sum+=1
    return sum

print(f([[1,4],[8,5],[-2,3]]))