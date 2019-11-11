def compare (numb1, numb2):
            numb1t=str(numb1)
            numb2t = str(numb2)
            if numb1t or numb2t == []:
                ln1 = len(numb1t)
                ln2 = len(numb2t)
                comparison=str()
            if ln1<ln2:
                    numb1t =(ln2 - ln1) * "0"+ numb1t
            elif ln2< ln1:
                    numb2t = (ln1 - ln2) * "0" +numb2t
            for index in range(0, len(numb2t)):
                if numb1t[index] == numb2t[index]:
                    comparison= comparison+"="
                else:
                    comparison= comparison+"*"
            return(comparison)

while True:
    try:

        numb1=int(input("Введіть перше двійкове число"))
        numb2 = int(input("Введіть друге двійкове число"))
        num1=str(numb1)
        num2=str(numb2)
        a=compare(numb1,numb2)
        if ("1"and "0") in (num1 and num2):
            print(a)
            print("відстань" , a.count("*"))
        else:
            ch = input("Введено невірні символи. Хочете продовжити гру - натисніть 1")
            if ch == "1":
                continue
            else:
                break
        ch = input("Хочете продовжити гру - натисніть 1")
        if ch == "1":
            continue
        else:
            break
    except ValueError:
        print("Введіть число наново")
    except SyntaxError:
        print("Введіть число наново")
    except IndexError:
        print("Введіть число наново")
    except TypeError:
        print("Введіть число наново")


