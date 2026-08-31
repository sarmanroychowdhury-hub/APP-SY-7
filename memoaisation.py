# Function to calculate the Fibonacci number using memoization
def fib(n, memo={}):
    # Base case: Fibonacci of 0 is 0 and Fibonacci of 1 is 1
    if n <= 1:
        return n

    # Check if the Fibonacci number is already calculated
    if n in memo:
        return memo[n]

    # Calculate Fibonacci number recursively and store it in memo
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    # Return the calculated Fibonacci number
    return memo[n]


# Take the number of terms from the user
n = int(input("Enter number: "))

# Print the first n Fibonacci numbers
for i in range(n):
    print(fib(i), end=" ")
