def is_caught(delay, lines):
	for line in lines:
		scanner, depth = line.split(": ")
		scanner = int(scanner)
		depth = int(depth)
		if (delay + scanner) % (2*(depth - 1)) == 0:
			return True

	return False

def run(lines):
	for i in range(10000000):
		if not is_caught(i, lines):
			return i

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

