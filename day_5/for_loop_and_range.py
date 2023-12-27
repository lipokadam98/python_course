# this is the same as a for loop in js or java for example
# for(int i = 0; i < 10; i++){}
# The range also has a third parameter where we can specify the steps
for i in range(0, 100, 2):
    print(i)

total = 0
for i in range(1, 101):
    total += i

print(total)
