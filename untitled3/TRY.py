numb1=str(input())
numb2=str(input())
ln1 = len(numb1)
ln2 = len(numb2)
comparison=str()
if ln1<ln2:
    numb1 =   numb1+(ln2 - ln1) * "0"
elif ln2< ln1:
    numb2 =   numb2+(ln1 - ln2) * "0"
#print(numb1, numb2)
for index in range(0, len(numb2)):
    #print(index)
    if numb1[index] == numb2[index]:
        comparison= comparison+"="
    else:
        comparison= comparison+"*"
print(comparison)

        def compare(numb1, numb2):
            ln1 = len(numb1)
            ln2 = len(numb2)
            if ln1 < ln2:
                numb1 = (ln2 - ln1) * "0" + numb1
            elif ln2 < ln1:
                numb2 = (ln1 - ln2) * "0" + numb2


        for index in (0, len(numb2)):
            if numb1[index] == numb2[index]:
                print("=")
            else:
                print("*")
    print(compare())