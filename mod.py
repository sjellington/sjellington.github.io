"""Presents a list of functions designed to help with the execution of number-theoretical problems."""

def enter() -> None:
    print("")

def convert(value: int) -> str:
    """Converts numbers to cardinal form."""

    value = str(value)
    cardinal: str = ""

    if (len(value) > 1) and (value[len(value) - 2] == "1"):
        cardinal = "th"
    else:
        if value[len(value) - 1] == "1":
            cardinal = "st"
        elif value[len(value) - 1] == "2":
            cardinal = "nd"
        elif value[len(value) - 1] == "3":
            cardinal = "rd"
        else:
            cardinal = "th"

    result: str = value + cardinal

    return result

def number_of_zeroes(factorial: str) -> int:
    """Determines the number of zeroes at the end of very large factorials."""
    # the greatest integer function
    # Legendre Formula

    new_fact: str = ""

    for letter in factorial:
        if letter != "!":
            new_fact += letter
    
    large_num: int = int(new_fact)
    enter()

    print(f"The number of zeroes in which {large_num}! terminates is related to the infinite sum from k=1 of the greatest integer function of {large_num} divided by 5 to the kth power, and to infinite sum from k=1 of the greatest integer function of {large_num} divided by 2 to the kth power.")
    enter()

    power: int = 1
    five_pow: int = 0

    while ((large_num)//(5**power)) != 0:
        print(f"[1000/5^{power}] = {(large_num)//(5**power)}")
        five_pow += (large_num)//(5**power)
        power += 1
    print(f"[1000/5^{power}] = {(large_num)//(5**power)}")
    enter()
    print(f"It appears from our analysis that {large_num}! contains a factor of 5 to the {convert(five_pow)} power.")
    enter()

    power = 1
    two_pow: int = 0

    while ((large_num)//(2**power)) != 0:
        print(f"[1000/2^{power}] = {(large_num)//(2**power)}")
        two_pow += (large_num)//(2**power)
        power += 1
    print(f"[1000/2^{power}] = {(large_num)//(2**power)}")
    print("...")
    enter()

    print(f"It appears that {large_num} also has a factor of 2 to the {convert(two_pow)} power.")
    enter()

    high_pow: int = 0
    
    if five_pow > two_pow:
        high_pow = two_pow
    else:
        high_pow = five_pow
    
    print(f"Since powers of ten require powers of both 5 and 2 to be present, we can conclude that {large_num}! terminates in {high_pow} zeroes.")
    
    return high_pow

def highest_power(factorial: str, divisor: int) -> int:
    enter()
    """Determines the highest power of a divisor present within a large factorial."""
    # the greatest integer function
    # the Legendre Formula

    new_fact: str = ""

    for letter in factorial:
        if letter != "!":
            new_fact += letter

    large_num: int = int(new_fact)

    print(f"The highest power of {divisor} present in {large_num}! is given by the infinite sum from k=1 of [{large_num}/{divisor}^k].")
    enter()

    two_pow: int = 1
    high_pow: int = 0

    while (large_num)//(divisor**two_pow) != 0:
        print(f"[1000/5^{two_pow}] = {(large_num)//(divisor**two_pow)}")
        high_pow += (large_num)//(divisor**two_pow)
        two_pow += 1
    print(f"[1000/5^{two_pow}] = {(large_num)//(divisor**two_pow)}")
    print("...")
    enter()

    print(f"The highest power of {divisor} present in {large_num}! is {high_pow}.")

    return high_pow

def prime_fact(num: int) -> dict:
    """Returns the prime factorization of a number as a dict with primes as keys and powers as values."""

    enter()
    print(f"{num} =")
    enter()

    small_num: int = 2
    result: dict[int, int] = {}


    while small_num <= num:
        if (num % small_num) == 0:
            result[small_num] = 0
        while (num % small_num) == 0:
            result[small_num] += 1
            num /= small_num
        small_num += 1
    
    for prime in result:
        print(f"{prime}^{result[prime]}")
    enter()
    
    return result

def tau(num: int) -> int:

    fact: dict[int, int] = prime_fact(num)
    result: int = 1

    for prime in fact:
        result *= (fact[prime] + 1)

    print(f"tau of {num} is {result}")

    return result

def sigma(num: int) -> int:
    enter()

    fact: dict[int, int] = prime_fact(num)
    result: int = 1

    for prime in fact:
        result *= ((prime**fact[prime] - 1))/(prime - 1)
    
    print(f"sigma of {num} is {int(result)}")
    
    return int(result)

def mu(num: int) -> int:
    enter()

    result: int = 0
    fact: dict[int, int] = prime_fact(num)

    if num == 1:
        result = 1
    else:
        for prime in fact:
            if fact[prime] >= 2:
                result = 0
            else:
                r: int = 0
                for prime in fact:
                    r += 1
                result = (-1)**r
    
    print(f"mu of {num} is {result}")
    enter()

    return result

def phi(num: int) -> int:

    result: int = 0
    consider_num: int = 1

    while consider_num < num:
        if gcd(num, consider_num) == 1:
            result += 1
        consider_num += 1
    
    print(result)
    return result

def d_of(num: int) -> list[int]:
    result: list[int] = []
    potential: int = 1

    while potential <= num:
        if num % potential == 0:
            result.append(potential)
        potential += 1
    
    print(result)
    return result

def is_prime(num: int) -> bool:
    consider_num: int = 1
    factors: int = 0
    result: bool = True
    while consider_num <= num:
        if num % consider_num == 0:
            factors += 1
        consider_num += 1
    if factors == 2:
        return result
    else:
        factors = False
        return factors
    
def rsa_alg(plaintext: str) -> str:

    plaintext = plaintext.strip(" ")
    plaintext = plaintext.upper()

    ciphertext: str = ""

    for char in plaintext:
        if (0 <= (ord(char) - 65)) and ((ord(char) - 65) <= 9):
            ciphertext += str(0)
            ciphertext += str((ord(char) - 65))
        else:
            ciphertext += str((ord(char) - 65))

    print(ciphertext)
        