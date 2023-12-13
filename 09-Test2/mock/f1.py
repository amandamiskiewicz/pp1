def f1(a):
    res=0
    for num in a:
        if num%2==0 and num>8:
            res+=1
    return res

if __name__=="__main__":
    print(f1([13,7,4,16,3,12,8]))