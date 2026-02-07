friends = ["Dave", "Carol", "Bob", "Alice",]

for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i] + ",", end=" ")


print()  

friends.append("Eve")         

friends.remove("Carol")

friends.sort()

print("Sorted list:")
for name in friends:
    print(name)
