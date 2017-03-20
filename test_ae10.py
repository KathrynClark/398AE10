import AE10

class TestBasics(unittest.TestCase):
	def test_isEven(self):
		result = isEven(8)
		self.assertEqual(TRUE, result)