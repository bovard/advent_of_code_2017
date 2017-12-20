def valid_line(line):
	words = line.split(' ')
	seen = {}
	for w in words:
		if seen.get(w):
			return False
		seen[w] = True
	return True

def run(lines):
	num_valid = 0 
	for line in lines:
		line = line.strip()
		if valid_line(line):
			num_valid += 1
	return num_valid

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

