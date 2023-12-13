def f4(d):
    sum=0
    for value in d.values():
        for num in value:
            if num>=5 and num<=10:
                sum+=num
    return sum



if __name__=="__main__":
    print(f4({"arr1":[2,6,5],"arr2":[7,1],"arr3":[2,9,8,1]}))