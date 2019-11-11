
import re
def valid(numbers):
    return bool (re.match('\d',numbers))
def get_count(numb):
    number=input(numb)
    while not valid(number):
        number=input(numb)
    return float(number)
def program():
    x = get_count("Enter your x")
    lal = - x ** 3 + 9
    lol = -3 / (x + 1)
    if x<=13:
       return "-х ^ 3 + 9 = "+ str(- x ** 3 + 9)
    else:
        return "-3 / (x + 1) = " + str(-3 / (x + 1))

print("Неділько Дарина Вікторівна \n Лабораторна робота №1 \n Варіант 14 \n Завдання №3. Розв&#39;язування рівнянь за певної умови(х): якщо х<=13, то виконується рівність -х^3+9, якщо ж х>13, то виконується рівність -3/(x+1) ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print( program() )
        repetition=input("Wanna play again - press 1")

