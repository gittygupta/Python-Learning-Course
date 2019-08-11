
x = []
for _ in range(30):
    x.append(int(input()))

for i in range(30):
    print(str(x[i]), " + ", end = " ")
    if i is 29:
        print(" = ", end = " ")

print(sum(x))
