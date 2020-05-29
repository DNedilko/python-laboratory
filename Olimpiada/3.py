def shell(list):
    inc = len(list) // 2
    while inc:
        for i, el in enumerate(list):
            while i >= inc and int(list[i - inc]) > int(el):
                list[i] = list[i - inc]
                i -= inc
            list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list


def insertion(list):
    for i in range(len(list)):
        j = i - 1
        elem = int(list[i])
        while int(list[j]) > elem and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = elem
    return list

list=input("Enter the list separated by spaces").split()
choise=int(input("Choose an option shell sort(2) or insertion sort(1)"))
if choise is 2:
    print(shell(list))
else:
    print(insertion(list))