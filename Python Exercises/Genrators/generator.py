n=int(input())
def square():
    i = 1
    while True:
        yield i * i
        i += 1
for j in square():
    if j > n*n:
        break
    print(j)