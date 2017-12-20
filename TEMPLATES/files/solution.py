
def run(lines):
	checksum = 0 
	for line in lines:
		line = line.strip()
		if "\t" in line:
			line = [int(l) for l in line.split('\t')]
		else:
			line = [int(l) for l in line.split(' ')]
		checksum += max(line) - min(line)
	return checksum

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

