import math


def get_inner_neighbors_sum(i, old_row, step):
	if i % step == 0 or i % step == step - 2:
		return old_row[i/2] + old_row[i/2 - 1]
	if i % step == step - 1:
		return old_row[i/2]
	return old_row[i/2-1] + old_row[i/2] + old_row[i/2+1]


def run(case):
	case = int(case)
	# edge case
	if case == 1:
		return 2

	step = 2
	row = [1, 2, 4, 5, 10, 11, 23, 25]

	for _ in range(10000):
		step += 2
		#print "NEW ROW"
		row_len = 4 * step
		nxt = [0] * row_len
		for i in range(row_len):
			inner_sum = get_inner_neighbors_sum(i, row, step)
			if i % step == 0:
				nxt[i] = nxt[i-1] + nxt[i-2] + inner_sum
			elif i >= row_len - 2:
				nxt[i] = nxt[i-1] + nxt[0] + inner_sum
			else:
				nxt[i] = nxt[i-1] + inner_sum
			if nxt[i] > case:
				return nxt[i]
		#print nxt
		#print len(nxt)
		row = nxt

if __name__ == "__main__":
	print run("347991")

