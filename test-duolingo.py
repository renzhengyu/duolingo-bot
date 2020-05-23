import unittest
from duolingo.main import Duobot


class TestDuobot(unittest.TestCase):
    def setUp(self):
        self.tess = Duobot(
            '/lessons/de-verkehrskontrolle-teil-1-adaptation-a2')

    def tearDown(self):
        self.tess.driver.quit()
        return super().tearDown()

    def test_word_pairs_filename(self):
        self.assertEqual(self.tess.word_pairs_filename,
                         'de-verkehrskontrolle-teil-1-adaptation-a2.json')


if __name__ == '__main__':
    unittest.main()
