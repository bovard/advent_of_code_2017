
import unittest

from solution import run

cases = [
	((5, "s1,x3/4,pe/b"), "baedc"),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case[0], case[1]), output)

