import unittest


import main


class TestMain(unittest.TestCase):

    def test_func_a(self):
        self.assertTrue(main.func_a())
