

import unittest

from rotate import run


cases = [
	("1212", 6),
	("1221", 0),
	("123425", 4),
	("123123", 12),
	("12131415", 4),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

