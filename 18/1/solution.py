from collections import defaultdict

def run(lines):
	lines = [l.strip() for l in lines]
	idx = 0
	reg = defaultdict(int)
	played = 0
	for _ in range(100000000):
		inst = lines[idx]
		if inst.startswith('snd'):
			idx += 1
			played = reg[inst.split(' ')[1]]
		elif inst.startswith('rcv'):
			idx += 1
			if played > 0:
				return played
		else:
			cmd, r, val = inst.split(' ')
			if val.isalpha():
				val = reg[val]
			else:
				val = int(val)

			if cmd == 'set':
				reg[r] = val
			elif cmd == 'add':
				reg[r] = reg[r] + val
			elif cmd == 'mul':
				reg[r] = reg[r] * val
			elif cmd == 'mod':
				reg[r] = reg[r] % val

			if cmd == 'jgz' and reg[r] > 0:
				idx += val
			else:
				idx += 1



if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

