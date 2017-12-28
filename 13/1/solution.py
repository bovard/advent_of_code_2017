def run(lines):
	scanners = {}
	scanner_pos = {}
	scanner_down = {}
	for line in lines:
		scanner, depth = line.split(": ")
		scanner = int(scanner)
		scanners[scanner] = int(depth)
		scanner_pos[scanner] = 0
		scanner_down[scanner] = True
	last = max(scanners.keys())

	score = 0
	idx = 0
	while idx <= last:
		if scanner_pos.get(idx) == 0:
			score += idx * scanners[idx]
		for k in scanners.keys():
			if scanner_pos[k] == scanners[k] - 1:
				scanner_down[k] = False
			elif scanner_pos[k] == 0:
				scanner_down[k] = True
			if scanner_down[k]:
				scanner_pos[k] += 1
			else:
				scanner_pos[k] -= 1
		idx += 1

	return score

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

