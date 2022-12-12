input = open(__file__.rstrip('solution.py') + 'input.txt').read()
crates, steps = [lines.split('\n') for lines in input.split('\n\n')]
stacks = [[line[i] for line in (plane[1::4] for plane in crates[:-1]) if line[i].strip()][::-1] for i in range(int(crates[-1][-2]))]
steps = [[int(num) for num in step.split(' ')[1::2]] for step in steps]

stackscp = [stack[:] for stack in stacks]
for amount, frm, to in steps:
    stackscp[to - 1].extend(stackscp[frm - 1][-amount:][::-1])
    del stackscp[frm - 1][-amount:]
print(''.join([stack[-1] for stack in stackscp]))

stackscp = [stack[:] for stack in stacks]
for amount, frm, to in steps:
    stackscp[to - 1].extend(stackscp[frm - 1][-amount:])
    del stackscp[frm - 1][-amount:]
print(''.join([stack[-1] for stack in stackscp]))