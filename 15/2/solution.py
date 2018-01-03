FACT_A = 16807
FACT_B = 48271
DIVISOR = 2147483647
CRIT_A = 4
CRIT_B = 8
NUM = 5000000


class bingen:
	def __init__(self, number, start, factor, divisor, criteria):
		self.i = 0
		self.number = number
		self.current = start
		self.factor = factor
		self.divisor = divisor
		self.criteria = criteria

	def __iter__(self):
		return self

	def next(self):
		if self.i == self.number:
			raise StopIteration()
		self.current = (self.current * self.factor) % self.divisor
		while self.current % self.criteria != 0:
			self.current = (self.current * self.factor) % self.divisor
		self.i += 1
		return self.current

def run(case):
	matches = 0

	gena = bingen(NUM, case[0], FACT_A, DIVISOR, CRIT_A)
	genb = bingen(NUM, case[1], FACT_B, DIVISOR, CRIT_B)
	for a,b in zip(gena,genb):
		if format(a, "016b")[-16:] == format(b, "016b")[-16:]:
			matches += 1
	return matches

	

if __name__ == "__main__":
	print run((289, 629))

