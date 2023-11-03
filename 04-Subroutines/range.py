def check_range(x,y,z):
    for i in range(x,y+1):
        if i==z:
            return True
    else:
        return False
        
if __name__=="__main__":
    print(check_range(2,6,5))
    print(check_range(2,10,9))
