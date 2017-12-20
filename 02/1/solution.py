
def run(lines):
	checksum = 0 
	for line in lines:
		line = line.strip()
		line = [int(l) for l in line.split('\t')]
		checksum += max(line) - min(line)
	return checksum

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

