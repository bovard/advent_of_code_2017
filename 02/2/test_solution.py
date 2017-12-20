
import unittest

from solution import run

cases = [
	("test.txt", 9)
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			with open(case) as f:
				lines = f.readlines()
				self.assertEquals(run(lines), output)

