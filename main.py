def maximal_in_array(array):
    if not array:
        return None

    temp_max = array[0]

    for number in array:
        if temp_max < number:
            temp_max = number

    return temp_max


def average(array):
    if not array:
        return None
    total = 0
    length = 0
    for num in array:
        total += num
        length += 1

    return total / length


def is_palindrome(string):
    if len(string) == 0:
        return None

    if string.lower()[::-1] == string.lower()[:]:
        return True
    else:
        return False


def common_elements(first_array, second_array):
    if len(first_array) == 0 or len(second_array) == 0:
        return None

    common = [number for number in first_array if number in second_array]
    return common


def fast_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]

    return fast_sort(left) + [pivot] + fast_sort(right)


def two_to_one(first: str, second: str) -> str:
    if len(first) == 0 or len(second) == 0:
        return 'None'

    return first.capitalize() + second.lower()


def count_vowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count


def change(word, replace):
    new_word = ''

    for letter in word:
        if letter == ' ':
            new_word += replace
        else:
            new_word += letter

    return new_word


def find_smallest_largest_strings(strings):
    if not strings:
        return None, None

    smallest = largest = strings[0]

    for string in strings:

        if len(string) < len(smallest):
            smallest = string

        elif len(string) > len(largest):
            largest = string

    return smallest, largest


array = [3, 7, 1, 9, 4, 6]
print("Maximal value in the array:", maximal_in_array(array))

numbers = [2, 4, 6, 8, 10]
print("Average of numbers:", average(numbers))

word = "racecar"
print("Is the word a palindrome?", is_palindrome(word))

first_array = [1, 2, 3, 4, 5]
second_array = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(first_array, second_array))

unsorted_array = [8, 3, 1, 7, 6, 4]
print("Fast sorted array:", fast_sort(unsorted_array))

first_string = "Hello"
second_string = "WORLD"
print("Combined string:", two_to_one(first_string, second_string))

text = "Hello, how are you?"
print("Vowel count:", count_vowels(text))

input_word = "Replace spaces"
replacement = "-"
print("Changed word:", change(input_word, replacement))

strings = ["apple", "banana", "cherry", "date", "elderberry"]
smallest, largest = find_smallest_largest_strings(strings)
print("Smallest string:", smallest)
print("Largest string:", largest)
