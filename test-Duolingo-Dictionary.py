import unittest
import random
import os
from string import ascii_letters
from duolingo.db import DuoDictionary
from time import gmtime, strftime


class TestDuoDictionary(unittest.TestCase):
    def setUp(self):
        self.tess = DuoDictionary(
            'test-story', sqlite3_filename=self.test_name())
        self.tess.append('one', 'eins')
        self.tess.append('two', 'zwei')

    def tearDown(self):
        os.remove(self.tess.sqlite3_filename)
        return super().tearDown()

    @staticmethod
    def test_name():
        return 'db-testcase-'+strftime('%Y%m%d%H%M%S', gmtime())+'.db'
        # return ":MEMORY:"

    @staticmethod
    def randString(maxlength=20):
        choices = ascii_letters+"ÄäÖöÜüß"+' '
        return ''.join((random.choice(choices) for i in range(random.randint(1, maxlength))))

    def test_one_eins(self):
        self.assertEqual('one', self.tess.pair('eins'))

    def test_two_zwei(self):
        self.assertEqual('zwei', self.tess.pair('two'))

    def test_random_string_shouldnot_exist(self):
        self.assertIsNone(self.tess.pair(self.randString()))

    def test_insert_random_pair(self):
        a = self.randString()
        b = self.randString()
        self.tess.append(a, b)
        self.assertEqual(a, self.tess.pair(b))
        self.assertEqual(b, self.tess.pair(a))


if __name__ == '__main__':
    unittest.main()
