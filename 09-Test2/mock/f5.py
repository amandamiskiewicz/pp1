def f5(c):
    res=0
    with open("zad.txt") as file:
        for i in file:
            if c in i:
                res+=1
    return res


if __name__=="__main__":
    print(f5("m"))