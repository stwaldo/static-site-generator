import unittest
from linkextractor import extract_markdown_links

class TestLinkExtractor(unittest.TestCase):
    
        def test_extract_single_link_from_string(self):
            text = "This is an example of a link [foo bar](http://example.com)"
            links = extract_markdown_links(text)
            self.assertEqual(links, [("foo bar", "http://example.com")])
    
        def test_extract_multiple_links_from_string(self):
            text = "This is an example of a link [foo bar](http://example.com) and another link [baz](http://example.com/another)"
            links = extract_markdown_links(text)
            self.assertEqual(links, [("foo bar", "http://example.com"), ("baz", "http://example.com/another")])
    
        def test_no_links_returns_empty_list(self):
            text = "This is an example of an image ![foo bar](http://example.com/image.jpg)"
            links = extract_markdown_links(text)
            self.assertEqual(links, [])