import unittest
from extracttitle import extract_title
    
class TestExtractTitle(unittest.TestCase):

    def test_extract_title_with_h1(self):
        markdown = "# This is a title"
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_title_with_multiple_lines(self):
        markdown = """
Some text
# This is a title
More text
        """
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_title_no_h1(self):
        markdown = """
Some text
## This is a subtitle
More text
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_h1_not_at_start(self):
        markdown = """
Some text
More text
# This is a title
        """
        self.assertEqual(extract_title(markdown), "This is a title")

if __name__ == '__main__':
    unittest.main()