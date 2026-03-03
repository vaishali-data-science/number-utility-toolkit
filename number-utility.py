num = int(input('Enter a number:'))

# checking if the number is even or odd
if num % 2 == 0:
    print(num, 'is an even number.')
else:
    print(num, 'is an odd number.')

# checking if the number is prime
if num <= 1:
    print(num, 'is not a prime number.')
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')

# calculating the factorial of the number

if num < 0:
    print('Error: Factorial is not defined for negative numbers.')
elif num == 0 or num == 1:
    print('Factorial of', num, 'is 1.')
else:
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    print('Factorial of', num, 'is', factorial)

# checking if the number is armstrong or not
num_str = str(num)
str_digits = len(num_str)
armstrong_sum = sum(int(digit)**str_digits for digit in num_str)
if num == armstrong_sum:
    print(num, 'is an armstrong number.')
else:
    print(num, 'is not an armstrong number.')

# checking if the number is palindrome or not
if num_str == num_str[::-1]:
    print(num, 'is a palindrome number.')
else:
    print(num, 'is not a palindrome number.')


