
import unittest

from solution import run

cases = [
	("flqrgnkx", 1242),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

