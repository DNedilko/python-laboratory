
import sys
import  re


def RangeN(N):
    N=int(N)
    if N>0 and N<31:
        return N
    else:
        N=input("Введіть кількість центрів кілець правильно, в діапазоні від 1 до 30")
        return RangeN(N)
def xyEntry(cord):
    pattern = '^(-?\d*)\s(-?\d*)$'
    while not re.match(pattern, cord):
        cord = input("Кординати введені не правильно, вводьте через пробіл два значення")
        return xyEntry(cord)
    return cord

def RangeXY(cord):
    cord=xyEntry(cord)
    xy= cord.split(' ')
    x = int(xy[0])
    y=int(xy[1])

    if (x>-1000 and x<1000) and (y>-1000 and y<1000):
        return x,y
    else:
        cord=input("Введіть координати правильно, в діапазоні від -1000 до 1000")
        return RangeXY(cord)



N=RangeN(input('Введіть кількість центрів кіл'))
Circles=[]
for i in range(0,N):
    xy=RangeXY(input("Введіть кординати Х та У для {} точки".format(i+1)))
    Circles.append(xy)
diameter=200000
for i in Circles:
    for l in Circles:
        if i==l:
            break
        else:
            length=(l[0]-i[0])**2+(l[1]-i[1])**2
            if length<diameter:
                diameter=length

print("Діаметр в квадраті = ", diameter)

exit(1)