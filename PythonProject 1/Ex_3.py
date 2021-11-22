def Suma_Numerelor(n):
    if n == 0:
        return 0
    return n + Suma_Numerelor(n-1)
print("Suma numerelor este ", Suma_Numerelor(7))
# -------------------------------------------------------
def Suma_Numerelor_Pare(p):
    suma = 0
    while suma == 0:
        for i in range(0, p+1,2):
            suma = suma + i
        return suma
print("Suma numerelor pare este: ",Suma_Numerelor_Pare(7))
#----------------------------------------------------
def Suma_Numerelor_Impare(im):
    suma = 0
    while suma == 0:
        for i in range(1, im+1,2):
            suma = suma + i
        return suma
print("Suma numerelor impare este: ",Suma_Numerelor_Impare(7))





