
def run(case):
	checksum = 0 
	depth = 0
	garbage = False
	score = 0
	bang = False
	garbage_count = 0
	for c in case:
		if bang:
			bang = False
		elif not garbage:
			if c == '{':
				depth += 1
			elif c == '}':
				score += depth
				depth -=1
			elif c == '<':
				garbage = True
		else:
			if c == '>':
				garbage = False
			elif c == '!':
				bang = True
			else:
				garbage_count += 1

	return garbage_count

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines[0])

