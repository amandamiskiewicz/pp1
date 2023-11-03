def month(n):
    if n==1:
        return "styczeń"
    elif n==2:
        return "luty"
    elif n==3:
        return "marzec"
    elif n==4:
        return "kwiecien"
    elif n==5:
        return "maj"
    elif n==6:
        return "czerwiec"
    elif n==7:
        return "lipiec"
    elif n==8:
        return "sierpien"
    elif n==9:
        return "wrzesien"
    elif n==10:
        return "pazdziernik"
    elif n==11:
        return "listopad"
    elif n==12:
        return "grudzien"
    
if __name__=="__main__":
    print(month(1))
    print(month(9))