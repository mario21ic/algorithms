#!/usr/bin/env python

#number = input("Ingrese nro A")
numberA = "5678"
numberB = "1234"
n_filas = len(numberA)

def multiplicar(A, B, C = 0):
    rpta = int(A) * int(B)
    lleva = 0
    if len(str(rpta)) >= 2:
        lleva = int(str(rpta)[0])
        digitoB = int(str(rpta)[1]) + C
        if len(str(digitoB)) >= 2:
            digitoB = int(str(digitoB)[1])
            lleva += + int(str(digitoB)[0])
    return lleva, digitoB

# n = 4*8
# print(n)

# n = 4*7
# print(n)
# if len(str(n)) >= 2:
#     m = str(n)[0]
#     print(int(m))
#     print(str(n)[1] + o)

print(multiplicar(4, 8, 0))
print(multiplicar(4, 7, 3))
print(multiplicar(4, 6, 3))
print(multiplicar(4, 5, 2))
# for b in numberB:
#     print(b)
#     for a in numberA:
#         b = 