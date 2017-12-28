
import unittest

from solution import run

cases = [
	("ne,ne,ne", 3),
	("ne,ne,sw,sw", 2),
	("ne,ne,s,s", 2),
	("se,sw,se,sw,sw", 3),
	("s,s,s,ne,ne", 3)
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

