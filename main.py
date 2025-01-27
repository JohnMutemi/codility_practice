# fibonacci series and it's reverse array
def fibonacci(n):
    fib=[0,1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
        
    return fib[:][::-1]

print(fibonacci(10))


# Print numbers from 1 to n. For multiples of 3, print "Fizz", for multiples of 5 print "Buzz", and for multiples of both, print "FizzBuzz".

def fizz_buzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

print(fizz_buzz(15))

# A simple calculator program
def calculator():
    print('Simple Calculator')
    print('Operations: +, -, *, /')
    while True:
        try:
            num1=float(input('Enter first number:'))
            operator=input('Enter an operation:')
            num2=float(input('Enter second number:'))
            
            if operator=='+':
                print (f"Result:{num1+num2}")
            elif operator=='-':
                
                print (f"Result: {num1 - num2}")
            elif operator=='*':
                print (f"Result: {num1 * num2}")
            elif operator=='/':
                if num2==0:
                    print('Error. Division by zero')
            else:
                print('Enter a valid operator')
        except ValueError:
             print("Invalid input. Please enter numbers only.")
           
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            
            break
calculator()            


# Given an array of integers, find the smallest positive integer not in the array.
def missing_integer(arr):
    i=1
    while i in arr:
        i+=1
    return i

# print the reverse of a string

def reverse_string(s):
    return s[::-1]
print(reverse_string('hello'))


# check anagrams
def are_anagrams(s1, s2):
    return sorted(s1)==sorted(s2)
print(are_anagrams('silent', 'listen'))

# remove vowels in a string

def remove_vowels(s):
    vowels='aeiouAEIOU'
    return ''.join(c for c in s if c not in vowels)


# check if a number is prime

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, (n**0.5)+ 1):
        if n%i==0:
            return False
        return True

# the second largest number in an array

def second_largest(num):
    unique_nums=list(set(num))
    unique_nums.sort()
    return unique_nums[-2] if len(unique_nums)>1 else None
print(second_largest([4,2,5,6]))

# Find all pairs in an array that sum to a target value

def pair_sum(nums, target):
    seen, result = set(), []
    for num in nums:
        complement = target - num
        if complement in seen:
            result.append((num, complement))
        seen.add(num)
    return result
print(pair_sum([2, 7, 11, 15], 9))  # Output: [(7, 2)]

# Move all zeros to the end of the array
def move_zeros(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros
print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

# Merge overlapping intervals in an array
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]

# find the equilibrium index of an array
def equilibrium_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1
print(equilibrium_index([1, 7, 3, 6, 5, 6]))  # Output: 3


# Reverse a string without affecting special characters
def reverse_string(s):
    chars = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return ''.join(chars)
print(reverse_string("a,b$c"))  # Output: "c,b$a"

# count vowels and consonants
def count_vowels_consonants(s):
    vowels='aeiouAEIOU'
    v_count=sum(1 for char in s if char in vowels)
    c_count=sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count


# Find the longest palindrome substring in a string
def longest_palindrome(s):
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    longest = ""
    for i in range(len(s)):
        odd_pal = expand_center(i, i)
        even_pal = expand_center(i, i+1)
        longest = max(longest, odd_pal, even_pal, key=len)
    return longest
print(longest_palindrome("babad"))  # Output: "bab" or "aba"

# Find the square root of a number using binary search
def square_root(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(square_root(16))  # Output: 4

# calculate grades
def calculate_grade(marks):
    if marks > 80:
        return "A"
    elif marks > 70:
        return "B"
    elif marks > 60:
        return "C"
    elif marks > 50:
        return "D"
    elif marks >= 0:
        return "F"
    else:
        return "Invalid marks"

# Test the function
marks = int(input("Enter the marks: "))
grade = calculate_grade(marks)
print(f"The grade for {marks} marks is: {grade}")

# Counting from 0 to 10 using a While Loop
counter=0
while counter<=10:
    print(counter)
    counter+=1

# reverse
# Using for loop to count from 10 to 0
for i in range(10, -1, -1):  # Start at 10, end at 0, step -1 (decrement)
    print(i)
