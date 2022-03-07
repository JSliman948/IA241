"""
Lab 6: For, If, and Range
"""
#3.1
for i in range(6):
    print(i)
for i in range(6):
    if i != 3:
        print(i)
#3.2
result = 1
for i in range(1,6):
    print(i)
    result = result * i
print(result)
#3.3
result = 0
for i in range(1, 6):
    print(i)
    result = result + i
print(result)
#3.4
gamma = 1
for k in range(3,9):
    print(k)
    gamma = gamma * k
print(gamma)
#3.5
delta = 1
for j in range(4,9):
    print(j)
    delta = delta * j
print(delta)
#3.6
epsilon = 0
for word in "This is my sixth string".split():
    print(word)
    epsilon = epsilon + 1
print(epsilon)


