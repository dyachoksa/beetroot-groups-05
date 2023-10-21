import random

index = 0

# Variant A
list_1 = random.sample(range(1, 101), 10)
list_2 = random.sample(range(1, 101), 10)

# Variant B
list_1 = []
i = 0
while i < 10:
    list_1.append(random.randint(1, 100))
    i += 1

list_2 = []
i = 0
while i < 10:
    list_2.append(random.randint(1, 100))
    i += 1

list_3 = []

while index < 10:
    if list_1[index] in list_2:
        list_3.append(list_1[index])
    index += 1

print(list_1)
print(list_2)
print(list_3)
