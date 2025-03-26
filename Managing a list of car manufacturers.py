
manufacturers = [
    "Toyota", "Ford", "Volkswagen", "BMW", "Chevrolet",
    "Audi", "Nissan", "Kia", "Honda", "Mazda"
]

sorted_copy = manufacturers.copy()

print("c) Reversed copy of the list:")
print(sorted_copy[::-1])

sorted_copy.sort()
print("\nd) Sorted copy and original list:")
print("Sorted copy:", sorted_copy)
print("Original list:", manufacturers)


group_a_h = [m for m in sorted_copy if m[0].upper() >= 'A' and m[0].upper() <= 'H']
group_i_q = [m for m in sorted_copy if m[0].upper() >= 'I' and m[0].upper() <= 'Q']
group_r_z = [m for m in sorted_copy if m[0].upper() >= 'R' and m[0].upper() <= 'Z']


print("\nGrouped manufacturers:")
print(f"A–H:\t{group_a_h}")
print(f"I–Q:\t{group_i_q}")
print(f"R–Z:\t{group_r_z}")
