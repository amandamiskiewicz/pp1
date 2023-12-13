import re
def f3(t):
    res=0
    find = re.findall(r'\b[0-9]+\b', t)
    for num in find:
        if len(num)==2 or len(num)==3:
            res=res+int(num)
    return res

if __name__=="__main__":
    print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1024, a take 8"))