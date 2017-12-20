
import unittest

from solution import run

cases = [
	("0 2 7 0", 4),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

