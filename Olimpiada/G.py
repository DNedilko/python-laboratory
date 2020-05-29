
def prog(N,T,line2,sum,p=1):
    if T>0:
        if p-1>=0:
            if int(line2[p-1])>int(line2[p+1]):
                sum+=int(line2[p-1])
                return prog(N,T-1,line2,sum,p-1)
            elif int(line2[p-1])<=int(line2[p+1]):
                sum+=int(line2[p+1])
                return prog(N,T-1,line2,sum,p+1)
        else:
            return prog(N, T, line2, sum, p + 1)
    else:
        return sum

def prog1(N,T,line2,sum,p=1):
    if T>0:
        if p-1>=0:
            if int(line2[p-1])>int(line2[p+1]):
                sum+=int(line2[p-1])
                return prog(N,T-1,line2,sum,p-1)
            elif int(line2[p-1])<=int(line2[p+1]):
                sum+=int(line2[p+1])
                return prog(N,T-1,line2,sum,p+1)
        else:
            return prog(N, T, line2, sum, p + 1)
    else:
        return sum


line1=input().split()
line2=input().split()
N=int(line1[0])
T=int(line1[1])
sum=int(line2[0])+int(line2[1])
maximum=max(line2)
print(maximum)
m=0


for elem in range(0,len(line2)):
    if line2[elem] == maximum:
        m=elem
if m>=T:
    sumall = prog(N, T - 1, line2, sum)

else:
    sumall= prog1(N,T-1,line2,sum)
print(sumall)