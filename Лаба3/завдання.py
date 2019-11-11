while True:
    try:
        line = str(input("Введіть стрічку"))
        letter=1
        for letter in ["o", "a", "y", "i", "Y", "A", "I", "E", "O", "e" ]:
            line = line.replace(letter , "*")
        print(line.count("*"))
        print(line)
        ch = input("Хочете продовжити гру - натисніть 1")
        if ch == "1":
            continue
        else:
            break
    except ValueError:
            print("Введіть текст наново")
    except SyntaxError:
            print("Введіть текст наново")
    except IndexError:
        print("Введіть текст наново")
    except TypeError:
            print("Введіть текст наново")
