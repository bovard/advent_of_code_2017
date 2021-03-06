
def run(case):
	checksum = 0 
	depth = 0
	garbage = False
	score = 0
	bang = False
	for c in case:
		if bang:
			bang = False
			continue

		if not garbage:
			if c == '{':
				depth += 1
			elif c == '}':
				score += depth
				depth -=1
			elif c == '<':
				garbage = True

		if garbage:
			if c == '>':
				garbage = False
			elif c == '!':
				bang = True

	return score

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines[0])

