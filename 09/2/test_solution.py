
import unittest

from solution import run

cases = [
	("<>", 0),
	("<random characters>", 17),
	("<<<<>", 3),
	("<{!>}>", 2),
	("<!!>", 0),
	("<!!!>>", 0),
	("<{o'i!a,<{i<a>", 10),
]

class Test(unittest.TestCase):

	def test_inputs(self):
		for case, output in cases:
			self.assertEquals(run(case), output)

