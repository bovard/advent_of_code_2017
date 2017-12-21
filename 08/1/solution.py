
from collections import defaultdict

def run(lines):
	register = defaultdict(int)
	for line in lines:
		line = line.strip()
		parts = line.split(' ')
		assert len(parts) == 7
		assert parts[3] == 'if'

		con_val = register.get(parts[4])
		con_str = "{} {} {}".format(con_val, parts[5], int(parts[6]))
		if eval(con_str):
			if parts[1] == 'inc':
				register[parts[0]] += int(parts[2])
			elif parts[1] == 'dec':
				register[parts[0]] -= int(parts[2])
			else:
				assert False, "op not found"

	print register
	return max(register.values())




if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

