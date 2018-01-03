import functools


def rev(A, idx, l):
	size = len(A)
	old = A
	if idx + l > len(A):
		first = len(A) - idx
		rest = l - first
		r = A[idx:idx+first] + A[0:rest]
		r.reverse()
		A = r[first:] + A[rest:idx] + r[0:first]
	else:
		A = A[0:idx] + A[idx:idx + l][::-1] + A[idx+l:]
		assert size == len(A)
	return A


def run_circle(idx, skip, A, case):
	for l in case:
		A = rev(A, idx, l)
		idx += l + skip
		idx %= len(A)
		skip += 1

	return idx, skip, A

def knot_hash(case):
	nums = []
	for c in case:
		nums.append(ord(c))
	nums += [17, 31, 73, 47, 23]

	idx = 0
	skip = 0
	A = range(256)
	for _ in range(64):
		idx, skip, A = run_circle(idx, skip, A, nums)

	hexs = []
	for i in range(16):
		hexs.append(functools.reduce(lambda a, b: a ^ b, A[16*i:16*(i+1)]))

	result = ""
	for h in hexs:
		if h < 16:
			result += '0'
		result += str(hex(h))[2:]

	assert len(result) == 32

	return result


def _is_in_grid(i, j):
	if i < 0 or j < 0:
		return False
	if i > 127 or j > 127:
		return False
	return True


def run(case):
	grid = []
	for i in range(128):
		grid.append([0] * 128)
		knot = knot_hash("{}-{}".format(case, i))
		j = 0
		for c in knot:
			digits =  format(int(c, 16), "04b")
			for d in digits:
				grid[i][j] = d
				j += 1

	visited = {}
	regions = 0
	i, j = 0, 0
	while i < 127 or j < 127:
		if grid[i][j] == "1" and not visited.get((i, j)):
			to_visit = [(i,j)]
			regions += 1
			idx = 0
			while len(to_visit):
				curr = to_visit.pop(0)
				visited[curr] = True
				for di in (-1, 1):
					if _is_in_grid(curr[0]+di, curr[1]) and grid[curr[0]+di][curr[1]] == '1' and not visited.get((curr[0]+di,curr[1])):
						if (curr[0] + di, curr[1]) not in to_visit:
							to_visit.append((curr[0]+di,curr[1]))
				for dj in (-1, 1):
					if _is_in_grid(curr[0], curr[1]+dj) and grid[curr[0]][curr[1]+dj] == '1' and not visited.get((curr[0],curr[1]+dj)):
						if (curr[0], curr[1]+dj) not in to_visit:
							to_visit.append((curr[0],curr[1]+dj))

		j += 1
		if j > 127:
			i += 1
			j = 0
	return regions

if __name__ == "__main__":
	print run("hxtvlmkl")

