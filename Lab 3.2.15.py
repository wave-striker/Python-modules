c0 = int(input("Please enter any number other than 1: "))
steps = 0
while c0 != 1:
    print(c0)
    if c0 %2 == 0:
        c0//= 2
        steps += 1

    else:
        c0 = (3 * c0) + 1
        steps += 1

print(c0)
print("Steps take: ", steps)
