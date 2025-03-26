user_input = input("Enter a list of integers separated by spaces: ")

numbers = list(map(int, user_input.split()))


print("a) Total number of items:", len(numbers))


print("b) Last item in the list:", numbers[-1])


print("c) Reversed list:", numbers[::-1])


print("d) List contains 5:", 5 in numbers)


print("e) Number of 5s in the list:", numbers.count(5))


if len(numbers) > 2:
    trimmed = numbers[1:-1]  # удаляем первый и последний
    trimmed.sort()
    print("f) Sorted list without first and last items:", trimmed)
else:
    print("f) Not enough items to trim and sort.")
