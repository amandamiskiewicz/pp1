def f(card_number):
    mask=card_number[:2]+10*"*"+card_number[-4:]
    return mask

if __name__=="__main__":
    print(f("1234567890123456"))
