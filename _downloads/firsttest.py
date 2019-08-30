import unittest


class OurFirstTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)
    
    def test_false(self):
        self.assertFalse(False)

    def test_will_never_pass(self):
        self.assertEqual(0,1)
