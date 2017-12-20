
import unittest

from solution import run

cases = [
	("1", 0),
	("12", 3),
	("23", 2),
	("1024", 31),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

