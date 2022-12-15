input = open(__file__.rstrip('solution.py') + 'input.txt').read()
path = []
sizes = {}
for line in input.split('\n'):
    match line.split(' '):
        case '$', 'cd', '..':
            del path[-1]
        case '$', 'cd', directory:
            path.append(directory)
        case ['$', 'ls'] | ['dir', _]:
            pass
        case size, _:
            for i in range(len(path)):
                fullpath = f"/{'/'.join(path[1:i + 1])}"
                sizes[fullpath] = sizes.get(fullpath, 0) + int(size)

print(sum(size for size in sizes.values() if size <= 100000))

threshold = sizes['/'] - 40000000
print(min(size for size in sizes.values() if size >= threshold))
