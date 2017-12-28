

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


def run(size, case):
	A = range(size)
	pos = 0
	skip = 0
	for l in case:
		A = rev(A, pos, l)
		pos += l + skip
		pos %= size
		skip += 1

	return A[0] * A[1]

if __name__ == "__main__":
	print run(256, [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100])

