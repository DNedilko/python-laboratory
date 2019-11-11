def WordLength(s,n):
            try:
                list=(s.split())
                word=list[n-1]
                while 0<n<len(list)+1:
                    return (len(word))

            except ValueError:
                print("Помилка індексу")
            except SyntaxError:
                print("Помилка індексу")
            except IndexError:
                print("Помилка індексу")
            except TypeError:
                print("Помилка індексу")


while True:
    s = str(input("Введіть своє речення"))
    n = int(input("eВведіть номер слова довжину якого ви хочете отримати"))
    print(WordLength(s, n))
    ch = input("Хочете продовжити гру - натисніть 1")
    if ch == "1":
        continue
    else:
        break