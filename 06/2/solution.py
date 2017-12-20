
def next_step(buckets):
	num = max(buckets)
	idx = buckets.index(num)
	assert buckets[idx] == num
	buckets[idx] = 0
	size = len(buckets)
	for _ in range(num):
		idx += 1
		idx %= size
		buckets[idx] += 1

def run(case):
	buckets = [int(i) for i in case.split(' ')]

	seen = {}
	count = 0
	target = ""
	while True:
		k = ",".join([str(i) for i in buckets])

		if k == target:
			return count
		elif seen.get(k) and target == "":
			target = k
			count = 0
		else:
			seen[k] = True
		next_step(buckets)
		count += 1


if __name__ == "__main__":
	print run("14 0 15 12 11 11 3 5 1 6 8 4 9 1 8 4")

