from Ex_3 import *
#Ex 3



#Ex 1
def your_function(*args,**kwargs):
    suma = 0
    while suma == 0:
        for i in args:
            try:
                if i == int(i):
                    suma = suma + i
            except ValueError :
                pass
            except TypeError:
                pass
        for j in kwargs:
            try:
                 if j == int(j):
                    suma = suma + j
            except ValueError:
                pass
            except TypeError:
                 pass




        return suma

print(your_function(1,5,-3,"abc",[12,56,"cad"]))


#Ex2
Number = input("Enter a number: ")
try:
    Int = int(Number)
    print(Number)
except ValueError as e:
    print(0)