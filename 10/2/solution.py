import functools


def rev(A, idx, l):
	size = len(A)
	old = A
	if idx + l > len(A):
		first = len(A) - idx
		rest = l - first
		r = A[idx:idx+first] + A[0:rest]
		r.reverse()
		A = r[first:] + A[rest:idx] + r[0:first]
	else:
		A = A[0:idx] + A[idx:idx + l][::-1] + A[idx+l:]
		assert size == len(A)
	return A


def run_circle(idx, skip, A, case):
	for l in case:
		A = rev(A, idx, l)
		idx += l + skip
		idx %= len(A)
		skip += 1

	return idx, skip, A

def run(case):
	nums = []
	for c in case:
		nums.append(ord(c))
	nums += [17, 31, 73, 47, 23]

	idx = 0
	skip = 0
	A = range(256)
	for _ in range(64):
		idx, skip, A = run_circle(idx, skip, A, nums)

	hexs = []
	for i in range(16):
		hexs.append(functools.reduce(lambda a, b: a ^ b, A[16*i:16*(i+1)]))

	result = ""
	for h in hexs:
		if h < 16:
			result += '0'
		result += str(hex(h))[2:]

	assert len(result) == 32

	return result




if __name__ == "__main__":
	print run("83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100")

