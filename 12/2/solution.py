from collections import defaultdict

def run(lines):
	pipes = defaultdict(list)
	for line in lines:
		line = line.strip()
		pid, children = line.split(' <-> ')
		children = children.split(', ')
		children = [int(c) for c in children]
		pipes[int(pid)] = children

	assignment = {}
	for pid in pipes.keys():
		if assignment.get(pid):
			continue
		contains = {}
		to_expand = [pid]
		while len(to_expand) > 0:
			curr = to_expand.pop(0)
			if contains.get(curr):
				continue
			contains[curr] = True
			assignment[curr] = pid
			to_expand += pipes[curr]

	return len(set(assignment.values()))

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

