#!/usr/bin/env python

#number = input("Ingrese nro A")
numberA = "5678"
numberB = "1234"
n_filas = len(numberA)

def multiplicar(A, B, C = 0):
    # print(A,B,C)
    rpta = (int(A) * int(B)) + C
    lleva = 0
    if len(str(rpta)) >= 2:
        digitoB = int(str(rpta)[1])
        lleva = int(str(rpta)[0])
        if len(str(digitoB)) >= 2:
            digitoB = int(str(digitoB)[1])
            lleva += int(str(digitoB)[0])
    else:
        digitoB = rpta
    return (digitoB, lleva)

# n = 4*8
# print(n)

# n = 4*7
# print(n)
# if len(str(n)) >= 2:
#     m = str(n)[0]
#     print(int(m))
#     print(str(n)[1] + o)

# b = "4"
# b = "3"
# b = "2"
# b = "1"
bx = 0
respuestas = []
for b in numberB[::-1]:
    sumatoria = ""
    lleva = 0
    ax = 0
    for a in numberA[::-1]:
        # print("a:", a)
        rpta, lleva = multiplicar(a, b, lleva)
        # print(f"rtpa {rpta} - lleva {lleva}")
        sumatoria = str(rpta) + sumatoria
        ax += 1
        if (ax == len(numberA)):
            # print("final")
            sumatoria = str(lleva) + sumatoria
        # print(sumatoria)
    # print(f"bx: {bx}")
    for x in range(bx):
        sumatoria = sumatoria + "0"
    # print(sumatoria, bx)
    respuestas.append(int(sumatoria))
    bx += 1

# print(respuestas)
final = 0
for x in respuestas:
    final = final + x

print(final)

# print(multiplicar(4, 8, 0))
# print(multiplicar(4, 7, 3))
# print(multiplicar(4, 6, 3))
# print(multiplicar(4, 5, 2))
