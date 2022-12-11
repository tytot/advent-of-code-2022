input = open(__file__.rstrip('solution.py') + 'input.txt').read()
rounds = [(ord(strategy[0]) - ord('A'), ord(strategy[1]) - ord('X')) for strategy in
          (round.split(' ') for round in input.split('\n'))]
print(sum(b + 1 + 3 * ((((b - a) % 3) + 1) % 3) for a, b in rounds))
print(sum(((a + b - 1) % 3) + 1 + 3 * b for a, b in rounds))
