import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)

for line in lines:
    number = int(line.strip())
    factors = factorize(number)
    if len(factors) >= 2:
        p, q = factors[0], factors[1]
        print(f"{number}={p}*{q}")

