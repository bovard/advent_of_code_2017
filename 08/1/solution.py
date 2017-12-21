
LT = "<"
GT = ">"
GTE = ">="
LTE = "<="
NE = "!="
E = "=="

INC = "inc"
DEC = "dec"

from collections import defaultdict

def comp(var_val, comp, val):
	if comp == LT:
		return var_val < val
	elif comp == GT:
		return var_val > val
	elif comp == LTE:
		return var_val <= val
	elif comp == GTE:
		return var_val >= val
	elif comp == NE:
		return var_val != val
	elif comp == E:
		return var_val == val
	assert False, "comp not found {}".format(op)


def run(lines):
	register = defaultdict(int)
	for line in lines:
		line = line.strip()
		parts = line.split(' ')
		assert len(parts) == 7
		assert parts[3] == 'if'
		assert parts[5] in (LT, GT, GTE, LTE, NE, E)

		var_val = register.get(parts[4])
		if comp(var_val, parts[5], int(parts[6])):
			if parts[1] == INC:
				register[parts[0]] += int(parts[2])
			elif parts[1] == DEC:
				register[parts[0]] -= int(parts[2])
			else:
				assert False, "op not found"

	print register
	return max(register.values())




if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

