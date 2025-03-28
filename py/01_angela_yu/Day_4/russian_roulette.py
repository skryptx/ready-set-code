from random import randint, choice

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[randint(0,4)])
print(choice(friends))

list_rand = []

for i in range(1, 7):
    list_rand.append(randint(0, 9))

print(list_rand)
