import math

def Cfunction(A,B):
    symDif=A.symmetric_difference(B)
  #  print(symDif)
    dif=A.difference(B)
 #   print(dif)
    return symDif.intersection(dif)
A={1,2,"ee","ww","c","d"}
B={4,"a","b","tt",1,3}
C=Cfunction(A,B)
U = {1,2,3,4,"a","b","c","d","ee","tt","ww"}
print("Перша множина А: ", A)
print("Друга множина В: ", B)
if C==U:
    print("Розв'язок функції - U: ", U)
else:
    print("Множина С(розв'язок ф-ї): ", C)



