# def print_numbers():
#     for i in range(1, 11):
#         print(i)

# print_numbers()

# ///////////ODD/////////////////////

# def odd_numbers():
#     for i in range(1, 21, 2):
#         print(i)

# odd_numbers()

# ///////////even/////////////////////

# def even_numbers():
#     numbers = []

#     for i in range(2, 21, 2):
#         numbers.append(i)

#     return numbers

# print(even_numbers())

# ==========================================
# PYTHON FUNCTIONS + LOOPS PRACTICE
# ==========================================

# 1. Print numbers from 1 to 10

def print_numbers():
    for i in range(1, 11):
        print(i)

print("Question 1")
print_numbers()


# ==========================================

# 2. Print numbers from 10 to 1

def reverse_numbers():
    for i in range(10, 0, -1):
        print(i)

print("\nQuestion 2")
reverse_numbers()


# ==========================================

# 3. Print even numbers

def even_numbers():
    for i in range(2, 21, 2):
        print(i)

print("\nQuestion 3")
even_numbers()


# ==========================================

# 4. Print odd numbers

def odd_numbers():
    for i in range(1, 21, 2):
        print(i)

print("\nQuestion 4")
odd_numbers()


# ==========================================

# 5. Multiplication table

def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

print("\nQuestion 5")
table(5)


# ==========================================

# 6. Sum from 1 to n

def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print("\nQuestion 6")
print(sum_numbers(5))


# ==========================================

# 7. Factorial

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print("\nQuestion 7")
print(factorial(5))


# ==========================================

# 8. Count vowels

def count_vowels(text):
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count += 1

    return count

print("\nQuestion 8")
print(count_vowels("Python"))


# ==========================================

# 9. Count characters

def count_characters(text):
    count = 0

    for letter in text:
        count += 1

    return count

print("\nQuestion 9")
print(count_characters("Hello"))


# ==========================================

# 10. Print list

def print_list(numbers):
    for num in numbers:
        print(num)

print("\nQuestion 10")
print_list([10, 20, 30, 40])


# ==========================================

# 11. Largest number

def largest(numbers):
    biggest = numbers[0]

    for num in numbers:
        if num > biggest:
            biggest = num

    return biggest

print("\nQuestion 11")
print(largest([5, 9, 2, 15, 7]))


# ==========================================

# 12. Smallest number

def smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

print("\nQuestion 12")
print(smallest([5, 9, 2, 15, 7]))


# ==========================================

# 13. Count positive numbers

def positive_count(numbers):
    count = 0

    for num in numbers:
        if num > 0:
            count += 1

    return count

print("\nQuestion 13")
print(positive_count([-2, 5, -8, 4, 6]))


# ==========================================

# 14. Count negative numbers

def negative_count(numbers):
    count = 0

    for num in numbers:
        if num < 0:
            count += 1

    return count

print("\nQuestion 14")
print(negative_count([-2, 5, -8, 4, 6]))


# ==========================================

# 15. Reverse a string

def reverse(text):
    result = ""

    for letter in text:
        result = letter + result

    return result

print("\nQuestion 15")
print(reverse("Python"))


# ==========================================

# 16. Check palindrome

def palindrome(text):
    reverse = ""

    for letter in text:
        reverse = letter + reverse

    return reverse == text

print("\nQuestion 16")
print(palindrome("madam"))


# ==========================================

# 17. Print star pattern

def stars(n):
    for i in range(1, n + 1):
        print("*" * i)

print("\nQuestion 17")
stars(5)


# ==========================================

# 18. Print squares

def squares(n):
    for i in range(1, n + 1):
        print(i * i)

print("\nQuestion 18")
squares(5)


# ==========================================

# 19. Average of a list

def average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)

print("\nQuestion 19")
print(average([10, 20, 30, 40]))


# ==========================================

# 20. Count even numbers in a list

def even_count(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count

print("\nQuestion 20")
print(even_count([1, 2, 3, 4, 5, 6, 8]))
