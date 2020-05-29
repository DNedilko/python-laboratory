import os


def valid_N(N):
    N=int(N)
    if N>=0 and N<=1000:
        return int(N)
    else:
        N=input("Введіть число N наново, воно не належить діапазону від 0 до 1000")
        return valid_N(N)

N=valid_N(input("Введіть число на основі якого будуть відбуватися розрахунки"))
print("N={}".format(N))
sum=0
# print(N)
i=0
while True:
    i+=1
    FS=N*i
    Text=str(FS)
    list_of_elements=[]
    for k in range(0,len(Text)):
        list_of_elements.append(Text[k])
    sum=0
    for z in list_of_elements:
        z=int(z)
        sum+=z
        if sum==N:
            print("Число яке утворює додаванням цифр це {} ".format(FS))
            exit(0)
