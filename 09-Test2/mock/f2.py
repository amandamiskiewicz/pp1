def f2(a1,a2):
    sum1=0
    for num1 in a1:
        if num1>9 and num1<100:
            sum1+=1
    sum2=0
    for num2 in a2:
        if num2>9 and num2<100:
            sum2+=1
    if sum1==sum2:
        return True
    else: 
        return False
    
if __name__=="__main__":
    print(f2([23,7,16,34],[1,18,79,20,6,111]))
