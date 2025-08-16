
#Problem No.1 
array_items = [128, 256, 64, 32, 16, 8, 4, 2]
sum = 0 
for index in array_items:
    sum += index
print("Total sum of array items:", sum)

#Problem No.2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)
print("Array after appending a new item:", numbers)

#Problem No.3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(1, 1.5)  # Inserting before the second element
print("Array after inserting a new item before the second element:", numbers)

#Problem No.4
numbers = [5, 4, 3, 2, 1]
numbers.reverse()
print("Array after reversing the order of items:", numbers)

#Problem No.5
numbers = [5, 4, 3, 2, 1]
numbers_length = len(numbers)
print("Length of the array:", numbers_length)