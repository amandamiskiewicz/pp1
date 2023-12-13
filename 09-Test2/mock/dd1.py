def f(c):
    cards = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    c=list(c)
    for card in cards:
        if card not in c:
            return card
        
if __name__=="__main__":
    print(f("2345678TQKAJ"))