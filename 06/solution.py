input = open(__file__.rstrip('solution.py') + 'input.txt').read()
print(next(i for i in range(4, len(input) + 1) if len(set(input[i - 4:i])) == 4))
print(next(i for i in range(14, len(input) + 1) if len(set(input[i - 14:i])) == 14))