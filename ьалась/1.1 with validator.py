
import re
def valid(numbers):
    return bool (re.match('\d',numbers))
def get_count(numb):
    number=input(numb)
    while not valid(number):
        number=input(numb)
    return int(number)
def program():
    flw = get_count("Введіть кількість пелюсток ")
    if flw % 2:
        return 'Любить'
    else:
        return'Не любить'

print("Неділько Дарина Вікторівна \n Лабораторна робота №1 \n Варіант 14 \n Завдання №1. Знаходження кількості днів ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print( program() )
        repetition=input("Wanna play again - press 1")

