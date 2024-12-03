import unittest
from src.tafqit import Tafqit


class TestTafqit(unittest.TestCase):
    def test_arabic_number_to_text(self):
        tafqit = Tafqit()
        self.assertEqual(tafqit.number_to_text("٣", "ar"), "٣")

    def test_english_number_to_text(self):
        tafqit = Tafqit()
        self.assertEqual(tafqit.number_to_text("3", "en"), "3")


if __name__ == "__main__":
    unittest.main()
