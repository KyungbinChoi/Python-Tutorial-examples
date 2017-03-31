count = 0
sum = 0
total = 0

num = int(input())
min = num
max = num

while num > 0:
    count += 1
    total += num
    if num < min:
        min = num
    if num > max:
        max = num
    print("Enter a nonnegative number")
    num=int(input())

if count > 0 :
    print(min)
    print(max)
    print(total/count)

