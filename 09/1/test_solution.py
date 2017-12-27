
import unittest

from solution import run

cases = [
	("{}", 1),
	("{{{}}}", 6),
	("{{},{}}", 5),
	("{{{},{},{{}}}}", 16),
	("{<a>,<a>,<a>,<a>}", 1),
	("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
	("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
	("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

