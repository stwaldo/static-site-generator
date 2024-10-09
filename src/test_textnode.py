import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_url(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_url_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_text_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()