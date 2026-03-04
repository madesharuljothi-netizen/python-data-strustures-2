x = ()
print(x)

x = (1, 2, 3)
print(x)

x = (1, "Hello", 3.4)
print(x)

x = ("mouse", [8, 4, 6], (1, 2, 3))
print(x)

x = ('p', 'e', 'r', 'm', 'i', 't')
print(x[0])
print(x[5])

x = ("mouse", [8, 4, 6,], (1, 2, 3))

print(x[0][3])
print(x[1][1])


print("sliced :", x[1:4])

for letter in (x):
    print("Hello", letter)