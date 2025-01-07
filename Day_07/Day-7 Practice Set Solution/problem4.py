# Check if a number is prime

# Input: A number provided by the user
num = int(input('Enter a number: '))

# Loop to check divisibility from 2 to num-1
for i in range(2, num):
    if num % i == 0:  # Check if the number is divisible by i
        print('Number is not prime')  # If divisible, it's not a prime
        break  # Exit the loop since we found a divisor
else:
    print('Number is prime')  # If no divisors were found, it's a prime
