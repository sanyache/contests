def isPowerOfThree( n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 == 0:
        return isPowerOfThree(n // 3)
    return False

print(isPowerOfThree(27))