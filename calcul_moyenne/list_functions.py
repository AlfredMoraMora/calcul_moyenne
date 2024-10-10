# 1. append() - Adds an element at the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
# fruits = ['apple', 'banana', 'cherry', 'orange']


# 2. extend() - Adds multiple elements (from an iterable) to the end of the list.
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
# numbers = [1, 2, 3, 4, 5, 6]


# 3. insert() - Inserts an element at a specific position.
colors = ['red', 'green', 'blue']
colors.insert(1, 'yellow')  # Inserts 'yellow' at index 1
# colors = ['red', 'yellow', 'green', 'blue']


# 4. remove() - Removes the first occurrence of the specified value.
animals = ['cat', 'dog', 'bird', 'dog']
animals.remove('dog')  # Removes the first 'dog'
# animals = ['cat', 'bird', 'dog']


# 5. pop() - Removes and returns the element at the specified position (or the last element if no index is specified).
names = ['John', 'Jane', 'Jim']
popped_name = names.pop()  # Removes and returns the last element ('Jim')
# names = ['John', 'Jane']
# popped_name = 'Jim'

# With index
first_name = names.pop(0)  # Removes and returns the element at index 0 ('John')
# names = ['Jane']
# first_name = 'John'


# 6. clear() - Removes all elements from the list.
items = ['book', 'pen', 'pencil']
items.clear()
# items = []


# 7. index() - Returns the index of the first occurrence of the specified value.
cities = ['New York', 'Paris', 'Tokyo']
city_index = cities.index('Paris')
# city_index = 1


# 8. count() - Returns the number of occurrences of the specified value.
numbers = [1, 2, 2, 3, 2, 4]
count_twos = numbers.count(2)
# count_twos = 3


# 9. sort() - Sorts the list in ascending order by default. Can be reversed with the `reverse=True` flag.
numbers = [4, 2, 9, 1, 5]
numbers.sort()  # Sorts in ascending order
# numbers = [1, 2, 4, 5, 9]

# Sorting in descending order
numbers.sort(reverse=True)
# numbers = [9, 5, 4, 2, 1]


# 10. reverse() - Reverses the order of elements in the list.
letters = ['a', 'b', 'c', 'd']
letters.reverse()
# letters = ['d', 'c', 'b', 'a']


# 11. copy() - Returns a shallow copy of the list.
original_list = [1, 2, 3]
copied_list = original_list.copy()
# copied_list = [1, 2, 3]

# Modifying original_list won't affect copied_list
original_list.append(4)
# original_list = [1, 2, 3, 4]
# copied_list = [1, 2, 3]


# 12. len() - Returns the number of elements in the list.
fruits = ['apple', 'banana', 'cherry']
num_fruits = len(fruits)
# num_fruits = 3


# 13. sum() - Returns the sum of all numeric elements in the list.
numbers = [1, 2, 3, 4]
total_sum = sum(numbers)
# total_sum = 10


# 14. min() - Returns the smallest element in the list.
numbers = [10, 3, 6, 1]
smallest_number = min(numbers)
# smallest_number = 1


# 15. max() - Returns the largest element in the list.
numbers = [10, 3, 6, 1]
largest_number = max(numbers)
# largest_number = 10

# Sorting alphabetically (A to Z)
fruits = ['banana', 'apple', 'cherry', 'date']
fruits.sort()
# fruits = ['apple', 'banana', 'cherry', 'date']

# Sorting in reverse alphabetical order (Z to A)
fruits.sort(reverse=True)
# fruits = ['date', 'cherry', 'banana', 'apple']

# Case-insensitive sorting (A to Z)
fruits = ['Banana', 'apple', 'Cherry', 'date']
fruits.sort(key=str.lower)
# fruits = ['apple', 'Banana', 'Cherry', 'date']