import time

def calculate_prime_factors(n):
    """Calculates the prime factors of a number."""
    factors = []
    divisor = 2
    while divisor <= n:
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


def inefficient_fibonacci(n):
    """Calculates the Fibonacci sequence inefficiently."""
    if n <= 1:
        return n
    else:
        return inefficient_fibonacci(n - 1) + inefficient_fibonacci(n - 2)


def poorly_documented_function(x, y):
    # Adds two numbers
    sum_result = x + y
    # Multiplies two numbers
    product_result = x * y
    return sum_result, product_result


def duplicate_code_example(nums):
    """Returns a list of squared even numbers and cubed odd numbers from a list."""
    squares = []
    cubes = []
    
    for num in nums:
        if num % 2 == 0:
            squares.append(num ** 2)
        else:
            cubes.append(num ** 3)

    even_squares = []
    odd_cubes = []
    
    for num in nums:
        if num % 2 == 0:
            even_squares.append(num ** 2)
        else:
            odd_cubes.append(num ** 3)

    return squares, cubes, even_squares, odd_cubes


def main():
    start_time = time.time()

    # Prime factor calculation with a large number
    number = 600851475143
    print(f"Prime factors of {number}: {calculate_prime_factors(number)}")

    # Inefficient Fibonacci calculation
    print(f"Fibonacci of 30: {inefficient_fibonacci(30)}")

    # Poorly documented function usage
    print(poorly_documented_function(10, 5))

    # Duplicate code example
    nums = [i for i in range(1, 20)]
    print(duplicate_code_example(nums))

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()

