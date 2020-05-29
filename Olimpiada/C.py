



def rec_sum(N, sum, i=3):
    if (N - 2 * i) <= 0:
        return sum
    n = N - i * 2
    for j in range(1, n + 1):
        sum += j
        for k in range(1, j):
            sum += k
    return rec_sum(N, sum, i + 1)

N = int(input())
sum = N - 1
for i in range(1, N - 3):
    sum += i
print(rec_sum(N, sum))