input = open(__file__.rstrip('solution.py') + 'input.txt').read()
rucksacks = input.split('\n')
def priority(type):
    return ord(type) - ord('a') + 1 if type.islower() else ord(type) - ord('A') + 27

print(sum(priority(list(set(items[:len(items) // 2]) & set(items[len(items) // 2:]))[0]) for items in rucksacks))
print(sum(priority(list(set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2]))[0]) for i in range(0, len(rucksacks), 3)))