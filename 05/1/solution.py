
def run(lines):
	checksum = 0 
	lines = [int(l) for l in lines]

	end = len(lines)
	idx = 0
	steps = 0
	while True:
		steps += 1
		curr = lines[idx]
		lines[idx] += 1
		idx += curr
		if idx < 0 or idx >= end:
			return steps

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

