

def NSD(num1,num2):
    list=[]
    list.append(num1)
    list.append(num2)
    list_of_val=[]
    for nsd in range(1,int(min(list)+1)):
        count = 0
        for element in list:
            element=int(element)
            if element %nsd==0:
                count+=1
            if count ==len(list):
                list_of_val.append(nsd)
    return max(list_of_val)


def NSK(num1,num2):
    multiply=num1*num2
    nsd=NSD(num1,num2)
    nsk=multiply/nsd
    return nsk

def Final_length(num1,list,n=1):
        if n>=len(list):
            return num1
        else:
            num2 = int(list[n])
            nsk = NSK(num1, num2)

            return Final_length(nsk, list, n + 1)


list_of_drums=input().split()
num1=int(list_of_drums[0])
length_of_the_song=Final_length(num1,list_of_drums)
print(length_of_the_song)
