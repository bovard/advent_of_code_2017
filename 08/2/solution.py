
from collections import defaultdict

def run(lines):
	register = defaultdict(int)
	largest = 0
	for line in lines:
		line = line.strip()
		r, op, op_val, _, comp_r, comp, comp_val = line.split(' ')

		comp_r_val = register[comp_r]
		comp_str = "{} {} {}".format(comp_r_val, comp, comp_val)
		if eval(comp_str):
			if op == 'inc':
				register[r] += int(op_val)
			elif op == 'dec':
				register[r] -= int(op_val)
			else:
				assert False, "op not found"
		largest = max(largest, max(register.values()))

	return largest


if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)
