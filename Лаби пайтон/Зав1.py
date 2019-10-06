while True:
    try:
        line = list(input("Введіть стрічку"))
        ltrs2fnd=('o','y','e','i','a')
        print(line.count(ltrs2fnd))
    except ValueError:
            print("Введіть підходяще число")
    except SyntaxError:
            print("Введіть підходяще число")
    except IndexError:
        print("Введіть підходяще число")