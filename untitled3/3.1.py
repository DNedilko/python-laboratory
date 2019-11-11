def get_parameters():
    leters=input("Введіть символи, які ви хочете замінити")
    symbol=input("Введіть спеціальний символ на якиm ви хочете замінити символи "+ leters)
    line=input("Введіть стрічку у якій ви хочете замінити ці слова")
    return leters, symbol , line
def get_line_with_symbol(massive):
    leters=massive[0]
    symbol=massive[1]
    line=massive[2]
    linereplaced=line.replace(leters, symbol)
    return linereplaced, symbol
def get_symbols_counted(massive):
    linereplaced=massive[0]
    symbols=massive[1]
    amount=str(linereplaced.count(symbols))
    return ("У стрічці'"+ linereplaced + "' "+ amount + " символів '"+ symbols+"'")
print(get_symbols_counted(get_line_with_symbol(get_parameters())))