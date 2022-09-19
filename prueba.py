#  prueba 1 

def divi(a,b):
    if b == 0:
        print("Error no se puede dividir por 0")
    else:
        return a / b


a = int(input("digite el numero a dividir: "))
b = int(input("digite el divisor: "))

print(round(divi(a,b),2))

