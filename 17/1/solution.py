
def run(spins):
	pos = 1
	spin = [0,1]
	for i in range(2, 2018):
		pos = (pos + spins) % len(spin)
		pos += 1
		spin.insert(pos, i)
		pos %= len(spin)

	return spin[spin.index(2017) + 1]
	

if __name__ == "__main__":
	print run(377)

