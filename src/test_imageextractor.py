import unittest
from linkextractor import extract_markdown_images

class TestImageExtractor(unittest.TestCase):

    def test_extract_single_image_from_string(self):
        text = "This is an example of an image ![foo bar](http://example.com/image.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("foo bar", "http://example.com/image.jpg")])

    def test_extract_multiple_images_from_string(self):
        text = "This is an example of an image ![foo bar](http://example.com/image.jpg) and another image ![baz](http://example.com/another.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("foo bar", "http://example.com/image.jpg"), ("baz", "http://example.com/another.jpg")])

    def test_no_images_returns_empty_list(self):
        text = "This is an example of a link [foo bar](http://example.com)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])