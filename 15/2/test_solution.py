
import unittest

from solution import run

cases = [
	((65, 8921), 309),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

