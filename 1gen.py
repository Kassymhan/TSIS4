def generator(n):
    for i in range(n):
        yield i * i

n = int(input())

x = generator(n)
for i in x:
    print(i)