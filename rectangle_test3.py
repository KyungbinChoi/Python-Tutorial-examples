import rectangle

r = rectangle.Rectangle(5,4)
print("The first rectangle:")
print(r)
s = rectangle.Rectangle(4,4)
print("The second rectangle:")
print(s)
q = rectangle.Rectangle(5,4)
print("The third rectangle:")
print(q)

print("The diagram of the first rectangle is %0.2f " %r.diagonal())


if r==s:
    print("The first and the second rectangles are same")
else:
    print("The first and the second rectangles are different")

if r==q:
    print("The first and the third rectangles are same")
else:
    print("The first and the third rectangles are different")
