a="10100101010"

numb1=int(input())
numb2 = int(input())
num1=set(str(numb1))
num2=set(str(numb2))
super_set = {"2", "3", "4", "5", "6", "7", "8", "9"}
la = 0
k=0
for la in super_set:
    set_of_sets=la
    if la in num1 or num2:
        k=True
        print(k)
        break
    else:
        ch = input("Хочете продовжити гру - натисніть 1")
        if ch == "1":
            continue
        else:
            break