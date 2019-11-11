from random import randint
def valid(list):
    set1 = set(list)
    return bool(len(set1)==len(list))
def get(list):
    lisst=input(list)
    lis=lisst.split(" ")
    while not valid(lis):
        lisst = input(list)
        lis = lisst.split(" ")
    print("перший список", lis)
    return lis
def generate2list(list1):
    numbrOfElem=randint(len(list1),len(list1)+10)
    list2=[]
    for i in range(0,numbrOfElem):
        list2.append(list1[randint(0,len(list1)-1)])
    print("другий список",list2)
    return list2
def thethird(list1,list2):
    list3=[]
    for i in range(0, len(list2)):
        for j in range(0, len(list1)):
            if list1[j]==list2[i]:
                list3.append(j)
    return list3
def programe():
    list=get("Enter")
    return thethird(list, generate2list(list))

repetition=input("If you wanna play - press 1")
while repetition=="1":
        print(programe() )
        repetition=input("Wanna play again - press 1")