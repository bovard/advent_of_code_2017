FACT_A = 16807
FACT_B = 48271
DIVISOR = 2147483647

def run(case):
	a, b = case
	matches = 0
	for i in range(40000000):
		a *= FACT_A
		a %= DIVISOR
		b *= FACT_B
		b %= DIVISOR
		if format(a, "016b")[-16:] == format(b, "016b")[-16:]:
			matches += 1
	return matches

	

if __name__ == "__main__":
	print run((289, 629))

