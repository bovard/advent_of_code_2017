
def run(spins):
	ppos = 1
	l = 2
	target = 1
	for i in range(2, 50000000):
		ppos = (ppos + spins) % l
		ppos += 1
		if ppos == 1:
			target = i
		l += 1
		ppos %= l

	return target
	

if __name__ == "__main__":
	print run(377)

