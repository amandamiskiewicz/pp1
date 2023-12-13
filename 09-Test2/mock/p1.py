'''(p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) 
have a value of 10 each. The other cards have the value indicated by the card number. 
Create a function f(player1,player2) that returns true if the first player has cards of the same or higher value, 
and false otherwise. Example:
f("AJ972","AQT72")  False
f("9532","K8")  True
'''
def f(player1,player2):
    sum1=0
    for i in player1:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            sum1=sum1+10
        else:
            sum1=sum1+int(i)
    sum2=0
    for i in player2:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            sum2=sum2+10
        else:
            sum2=sum2+int(i)
    if sum1>=sum2:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))