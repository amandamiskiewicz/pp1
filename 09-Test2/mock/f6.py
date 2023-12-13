import csv
def f6(g,n1,n2):
    res=0
    with open("data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["gender"]=="Female" and int(row["children"])>=1 and int(row["children"])<=3:
                res+=1
    return res


if __name__=="__main__":
    print(f6("Female",1,3))