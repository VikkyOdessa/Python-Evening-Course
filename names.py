names = ["Alice", "Bob", "Charlie"]


print("c) Full list:", names)

names.append("Diana")
names.insert(1, "Eve")
print("d) After adding two names:", names)


print("e) All names except the last:")
print(names[0])
print(names[1])
print(names[2])
print(names[3])  


last_index = len(names) - 1
print("f) Last name using len():", names[last_index])

names[-2] = "Frank"
print("g) After changing second to last name:", names)

print(f"h) The list has {len(names)} names. The first name is {names[0]}.")

removed_name = names.pop(2)

print(f"j) Removed: {removed_name}. Remaining names: {names}")

last_name = names[-1]
names.remove(last_name)
print(f"k) Removed with remove(): {last_name}. Remaining list: {names}")

del names


