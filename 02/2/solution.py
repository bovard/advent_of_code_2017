
def _get_divisors(line):
	for i in range(len(line)):
		for j in range(i + 1, len(line)):
			if line[i] == 0 or line[j] == 0:
				continue
			if float(line[i]) / line[j] == line[i] / line[j]:
				return line[i] / line[j]
			if float(line[j]) / line[i] == line[j] / line[i]:
				return line[j] / line[i]
	assert False, "Divosors not found"


def run(lines):
	checksum = 0 
	for line in lines:
		line = line.strip()
		line = [int(l) for l in line.split('\t')]

		checksum += _get_divisors(line)

	return checksum

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

