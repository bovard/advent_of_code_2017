
import unittest

from solution import run

cases = [
	("330", 351),
	("362", 747),
	("57", 59),
	("931", 957),
	("957", 1968),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

