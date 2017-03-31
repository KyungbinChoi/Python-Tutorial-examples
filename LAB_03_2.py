#2-1번 문제
n=2
a=1
while n < 10:
    print( "{} times table".format(n),"="*8)
    while a <10:
        print("{} * {} = {}".format(n, a, n*a))
        a += 1
        if a == 10:
            a = 1
            n += 1
            break
print("="*8, "End", "="*8)


