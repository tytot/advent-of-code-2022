from itertools import accumulate, chain
from math import prod

input = open(__file__.rstrip('solution.py') + 'input.txt').read()
forest = [[int(height) for height in row] for row in input.split('\n')]
foresttrans = list(zip(*forest))

def visiblespots(trees):
    maxat = list(accumulate((height for _, height in trees), max))
    return (trees[i][0] for i in range(len(maxat)) if i == 0 or maxat[i] > maxat[i - 1])
visible = set(chain(((j, i) for j in range(len(forest)) for i in chain(visiblespots(list(enumerate(forest[j]))), visiblespots(list(enumerate(forest[j]))[::-1]))),
                    ((i, j) for j in range(len(foresttrans)) for i in chain(visiblespots(list(enumerate(foresttrans[j]))), visiblespots(list(enumerate(foresttrans[j]))[::-1])))))
print(len(visible))


def scenicscore(y, x):
    sectors = [(((y, i) for i in range(x - 1, -1, -1)), (y, 0)), (((y, i) for i in range(x + 1, len(foresttrans))), (y, len(foresttrans) - 1)),
               (((j, x) for j in range(y - 1, -1, -1)), (0, x)), (((j, x) for j in range(y + 1, len(forest))), (len(forest) - 1, x))]
    spots = [next(((j, i) for j, i in sector if forest[j][i] >= forest[y][x]), edge) for sector, edge in sectors]
    return prod(abs(y - j) + abs(x - i) - (1 if forest[j][i] > forest[y][x] else 0) for j, i in spots)
print(max(scenicscore(j, i) for j in range(len(forest)) for i in range(len(foresttrans))))