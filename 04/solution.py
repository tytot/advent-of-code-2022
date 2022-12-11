input = open(__file__.rstrip('solution.py') + 'input.txt').read()
assignments = [[int(id) for range in assignment.split(',') for id in range.split('-')] for assignment in input.split('\n')]
print(len([assignment for assignment in assignments if (assignment[0] <= assignment[2] and assignment[1] >= assignment[3]) or (assignment[0] >= assignment[2] and assignment[1] <= assignment[3])]))
print(len([assignment for assignment in assignments if (assignment[0] <= assignment[3] and assignment[1] >= assignment[2]) or (assignment[2] <= assignment[1] and assignment[3] >= assignment[0])]))