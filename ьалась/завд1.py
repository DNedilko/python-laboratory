
import re
def valid(numbers):
    return bool (re.match('\d',numbers))
def get_count(numb):
    number=input(numb)
    while not valid(number):
        number=input(numb)
    return int(number)
def program():
    a = get_count("Напишіть кількість тижнів ")
    b = get_count("Напишіть кількість місяців ")
    c = get_count("Напишіть кількість років ")
    return str(a*7+30*(c*12+b))
#def Repead(numb):
 #   repetition=input("Wanna play again - press 1")
  #  while not repetition==1:
   #     break
print("Неділько Дарина Вікторівна \n Лабораторна робота №1 \n Варіант 14 \n Завдання №1. Знаходження кількості днів ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print("усього ви витратили " + program() + " на виконання задачі")
        repetition=input("Wanna play again - press 1")