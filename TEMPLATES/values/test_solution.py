
import unittest

from solution import run

cases = [
	("1212", 1),
	("121", 1),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

