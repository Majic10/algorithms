def common_longest_substring(first_string, second_string):
    first_list_substrings = first_string.split()
    second_list_substrings = second_string.split()
    longest_substring = ""
    common_substring = ""
    for word in first_list_substrings:
        if len(word) > len(longest_substring):
            longest_substring = word

        for substring in second_list_substrings:
            if len(substring) == len(longest_substring) and substring in first_string:
                common_substring = substring

    return common_substring


string_1 = "Python programming is popular for web development."
string_2 = "Web development with Python is in high demand."


# print(common_longest_substring(string_1, string_2))


def find_missing_number(list1, list2):
    missing_number = 0
    for number in list1:
        if number not in list2:
            missing_number = number

    return missing_number


my_list1 = [1, 2, 3, 4, 5]
my_list2 = [3, 1, 5, 2]


# print(find_missing_number(my_list1, my_list2))


def largest_continuous_sum(numbers):
    max_sum = numbers[0]
    current_sum = 0
    for num in numbers:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


array1 = [1, 2, -1, 3, 4, 10, 10, -1, -10]


# print(largest_continuous_sum(array1))


def longest_palindromic_substring(string2):
    substrings_list = string2.split()
    palindromes_list = []
    longest_palindrome = ""

    for substring in substrings_list:
        if substring == substring[::-1]:
            palindromes_list.append(substring)

    for palindrome in palindromes_list:
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

    return longest_palindrome


string_3 = "madam arora teaches malayalam and programming languages."


# print(longest_palindromic_substring(string_3))


def sum_multiples(passed_number):
    sum_result = 0
    for number in range(1, passed_number + 1):
        if number % 3 == 0 or number % 5 == 0:
            sum_result += number

    return sum_result


test_number = 15


# print(sum_multiples(test_number))


def get_missing_number(numbers_list):
    missing_number = 0
    for number in range(numbers_list[0], numbers_list[-1] + 1):
        if number not in numbers_list:
            missing_number = number

    return missing_number


test_list = [1, 2, 3, 4, 6, 7, 8, 9]


# print(get_missing_number(test_list))


def generate_fibonacci_sequence(number):
    fibonacci_sequence = [0, 1]
    first_number = 0
    second_number = 1
    for i in range(2, number + 1):
        first_number += second_number
        fibonacci_sequence.append(first_number)

    return fibonacci_sequence


test_num = 5  # [0, 1, 1, 2, 3, 5]


# print(generate_fibonacci_sequence(test_num))


def filter_prime_numbers(my_number):
    prime_numbers = []
    for i in range(2, my_number + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


test_my_number = 12


# print(filter_prime_numbers(test_my_number))


def string_compression(my_string):
    characters = {}
    for char in my_string:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    compressed_string = ""
    for char, count in characters.items():
        compressed_string += char + str(count)

    return compressed_string


# print(string_compression("aaabbccc"))


def find_two_numbers_sum(array2, target):
    pair_numbers = []
    length = len(array2)
    for i in range(length):
        base_num = array2[i]
        for j in range(i + 1, length):
            comparison_num = array2[j]
            if base_num + comparison_num == target:
                pair_numbers.append((base_num, comparison_num))

    return pair_numbers


array_2 = [11, 15, 2, 7]
target_sum = 17


# print(find_two_numbers_sum(array_2, target_sum))


def sum_between_min_and_max(numbers):
    if len(numbers) <= 2:
        return 0

    min_index = max_index = 0
    min_number = max_number = numbers[0]

    for index, number in enumerate(numbers):
        if number > max_number:
            max_index = index
            max_number = number
        if number < min_number:
            min_index = index
            min_number = number

    return sum(numbers[min_index + 1:max_index])


numbers_list = [4, 2, 6, 9, 3, 16, 5]

sum_result = sum_between_min_and_max(numbers_list)


# print(sum_result)


def max_profit(prices):
    lowest_price = prices[0]
    highest_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        elif price - lowest_price > highest_profit:
            highest_profit = price - lowest_price

        if highest_profit < 0:
            return 0
    return highest_profit


prices_example = [7, 1, 5, 3, 6, 4]

profit = max_profit(prices_example)


# print(profit)


def calculate_max_profit(prices):
    lowest_price = prices[0]
    profit_max = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price

        if price > lowest_price:
            profit_max += price - lowest_price

    return profit_max


prices_example = [7, 1, 5, 3, 6, 4]


# print(calculate_max_profit(prices_example))


# 1. Write a program that asks the user for the distance (in meters) and time (in seconds) of a journey,
# then calculates and outputs the average speed using a function.


def calculate_average_speed(distance, time):
    speed = distance * 3.6 / time
    return speed


distance_meters = 16000
time_seconds = 5000
speed_km = (calculate_average_speed(distance_meters, time_seconds))


# print(f" Your speed is approximately: {speed_km} km/h")


# 2. Create a Morse code translator that takes in a string with alphanumeric characters in lower or upper case and
# # outputs the corresponding Morse code.

def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
        'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    user_input = text.upper()
    translation = []
    for letter in user_input:
        for key, code in morse_code_dict.items():
            if letter == key:
                translation.append(code)

    return translation


test_string = "code"


# print(text_to_morse(test_string))


# 4. Write a program that takes in a list of integers and returns the second-largest number in the list.


def find_2nd_largest_num(my_list):
    largest_num = my_list[0]
    second_largest_num = my_list[0]
    for num in my_list[1:]:
        if num > largest_num:
            largest_num = second_largest_num
            second_largest_num = num
    return second_largest_num


test_list1 = [1, 4, 7, 9, 34, 879, 234]  # 234


# print(find_2nd_largest_num(test_list1))


# 5. Write a program that takes in a string and outputs the number of vowels in the string.


def calculate_number_vowels(text3):
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_vowels = 0
    for letter in text3:
        if letter in vowels:
            number_vowels += 1

    if number_vowels == 0:
        return None

    return number_vowels


text_3 = "MacBook Pro"  # 4
number_of_vowels = calculate_number_vowels(text_3)


# print(f"Number of vowels found in this text is: {number_of_vowels}")


# Write a program that takes in two strings and returns True if they are anagrams of each other
# (i.e., they contain the same letters in a different order).


def are_anagrams(string4, string5):
    if len(string4) != len(string5):
        return False

    for char in string4:
        if char not in string5:
            return False

    return True


string_4 = "silent"
string_5 = "lentis"


# print(are_anagrams(string_4, string_5))


# Write a program that takes in a list of integers and returns True if there are any duplicates in the list.


def are_there_duplicates(list3):
    counter = []
    for num in list3:
        if num not in counter:
            counter.append(num)
        elif num in counter:
            return True

    return False


list_3 = [2, 4, 6, 4, 9, 0, 1]


# print(are_there_duplicates(list_3))


def have_common_integers(list4, list5):
    for num in list4:
        if num in list5:
            return True

    return False


list_4 = [2, 4, 6, 4, 9, 0, 1]
list_5 = [1, 1, 5, 4, 10, 30, 1]


# print(have_common_integers(list_4, list_5))


# Write a function that takes in a string and returns the first non-repeated character in the string1


def first_non_repeated_char(string6):
    for char in string6:
        if string6.count(char) == 1:
            return char
    return ""


string_6 = "exceptional"


# print(first_non_repeated_char(string_6))


def selection_sort(list6):
    for i in range(len(list6)):
        min_index = i
        for j in range(i + 1, len(list6)):
            if list6[j] < list6[min_index]:
                min_index = j

        list6[i], list6[min_index] = list6[min_index], list6[i]

    print(list6)


list_6 = [3, 5, 1, 0, 2, 6, 7]
# print(list_6)


# selection_sort(list_6)


def bubble_sort(arr2):
    n = len(arr2)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr2[j] > arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    return arr2


arr_2 = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr_2))



