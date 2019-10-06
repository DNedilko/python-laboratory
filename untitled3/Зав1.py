while True:
    try:
        line = str(input("Введіть стрічку"))
        ll=line.count("o")+line.count("y")+line.count("a")+line.count("i")+line.count("e")+line.count("O")+line.count("Y")+line.count("A")+line.count("I")+line.count("E")
        print(ll)
        letter=1
        fine=1
        for letter in ["o", "a", "y", "i", "Y", "A", "I", "E" ]:
            line = line.replace(letter , "*")

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
