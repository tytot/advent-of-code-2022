input = open(__file__.rstrip('solution.py') + 'input.txt').read()
path = []
sizes = {}
for line in input.split('\n'):
    if line == '$ cd ..':
        del path[-1]
    elif line.startswith('$ cd '):
        directory = line[5:]
        path.append(directory)
    elif not (line.startswith('$') or line.startswith('dir')):
        size = int(line.split(' ')[0])
        for i in range(len(path)):
            fullpath = f"/{'/'.join(path[1:i + 1])}"
            sizes[fullpath] = sizes.get(fullpath, 0) + size

print(sum(size for size in sizes.values() if size <= 100000))

threshold = sizes['/'] - 40000000
print(min(size for size in sizes.values() if size >= threshold))