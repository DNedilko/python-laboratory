
def sum_litt(n,sumOfAll):
    if n<=0:

        return sumOfAll
    print("st",n)
    for i in range(1,n+1):
        print("i1", i)
        # sumOfAll+=i
        for z in range(1,i+1):
            print("z=",z)
            sumOfAll+=z

    return sum_litt(n-2,sumOfAll)


def SumAll(n):
    sumOfAll = 1+n

    for i in range(1,n-1):
        print("i2",i)
        sumOfAll+=i
        print("sumall",sumOfAll)
    print("sum !!!!",sumOfAll)
    fin=sum_litt(n-4,sumOfAll)
    print(fin)
    return fin


n=int(input("Введіть кількість драконів у шерензі"))
var=n*SumAll(n)
print(var)