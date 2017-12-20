import math

def run(case):
	case = int(case)
	# edge case
	if case == 1:
		return 0

	level = math.sqrt(case)
	level = int(level)
	#print 'level idx:',level
	if level % 2 == 0:
		level -= 1

	lower = int(math.pow(level, 2))
	upper = int(math.pow(level + 2, 2))

	#print 'level:', lower, case, upper
	assert case > lower and case < upper, "Not getting the correct level"
	assert (upper - lower) % 4 == 0

	step = (upper - lower)/4
	#print step

	bracket = (lower + 1, lower + step)
	while case > bracket[1]:
		bracket = (bracket[0] + step, bracket[1] + step)

	assert bracket[0] <= case and case <= bracket[1], "not getting the correct side"

	#print 'side:', bracket[0], case, bracket[1]

	middle = (sum(bracket) - 1)/2

	#print 'move from level', (level - 1)/2 + 1
	#print 'move from side', abs(case - middle)

	return (level - 1)/2 + 1 + abs(case - middle)


if __name__ == "__main__":
	print run("347991")

