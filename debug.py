#!/usr/bin/python
a,b,c,d = 10,20,30,40
def funA():
    a,b,c = 100,200,300
    print(a,b,c,d, "funA")
    def funB():
        a,b = 1000,2000
        print(a,b,c,d, "funB")
        def funC():
            a = 10000
            print(a,b,c,d, "funC")
        funC()
    funB()
funA()

print(a,b,c,d, "inMain")
