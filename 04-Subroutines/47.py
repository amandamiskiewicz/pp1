'''47.	Define a function f(text) that returns the given text with all characters separated by "-" 
(minus sign). Example:
f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
f("UE") returns "U-E"
f("x") returns "x"
f("") returns ""
'''

def f(text):
    txt=""
    for i in text:
        txt=txt+i+"-"
    return txt[:-1]

if __name__=="__main__":
    print(f("Univesity"))
    print(f("UE"))
    print(f("x"))
    print(f(""))