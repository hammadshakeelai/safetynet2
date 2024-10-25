def divide_with_remainder_and_decimals(dividend, divisor, precision=10):
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")# Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1 # Work with absolute values to simplify the logic
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    remainder = dividend # Integer division using repeated subtraction
    while remainder >= divisor:
        remainder -= divisor
        quotient += 1 # If there's no precision required for decimals, return now
    if precision == 0:
        return sign * quotient, remainder # Now calculate the decimal part
    decimal_part = []
    for _ in range(precision):
        remainder *= 10
        digit = 0
        while remainder >= divisor:
            remainder -= divisor
            digit += 1
        decimal_part.append(str(digit)) # Combine the quotient with the decimal part
    decimal_result = float(f"{quotient}." + ''.join(decimal_part))
    return sign * decimal_result# Example usage:
dividend = int(input("enter number:  "))
divisor = int(input("enter dividing number:  "))
result = divide_with_remainder_and_decimals(dividend, divisor)
print(f"The result of dividing {dividend} by {divisor} is approximately {result}.")
