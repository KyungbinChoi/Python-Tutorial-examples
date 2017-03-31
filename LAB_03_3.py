
#2-2번 문제
for i in range(2,10):
    print("{} times table".format(i),"="*8)
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j))
print("="*8, "End", "="*8)
