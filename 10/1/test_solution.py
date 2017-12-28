
import unittest

from solution import run

cases = [
	(5, [3,4,1,5], 12),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for l, case, output in cases:
			self.assertEquals(run(l, case), output)

