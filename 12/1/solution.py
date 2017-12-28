from collections import defaultdict

def run(lines):
	pipes = defaultdict(list)
	for line in lines:
		line = line.strip()
		pid, children = line.split(' <-> ')
		children = children.split(', ')
		children = [int(c) for c in children]
		pipes[int(pid)] = children

	contains = {}
	to_expand = [0]
	while len(to_expand) > 0:
		curr = to_expand.pop(0)
		if contains.get(curr):
			continue
		contains[curr] = True
		to_expand += pipes[curr]

	return len(contains.keys())

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

