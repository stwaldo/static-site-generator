import unittest

from leafnode import LeafNode
from nodeconverter import text_node_to_html_node
from textnode import TextNode

class TestTextNodeConverter(unittest.TestCase):
    
    def test_text_node_type_text(self):
        text_node = TextNode("Hello", "text")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode(None, "Hello"))

    def test_text_node_type_bold(self):
        text_node = TextNode("Hello", "bold")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("b", "Hello"))

    def test_text_node_type_italic(self):
        text_node = TextNode("Hello", "italic")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("i", "Hello"))

    def test_text_node_type_code(self):
        text_node = TextNode("Hello", "code")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("code", "Hello"))

    def test_text_node_type_link(self):
        text_node = TextNode("Hello", "link", "http://example.com")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("a", "Hello", {"href": "http://example.com"}))

    def test_text_node_type_image(self):
        text_node = TextNode("Hello", "image", "http://example.com/image.jpg")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("img", "", {"src": "http://example.com/image.jpg", "alt": "Hello"}))
    
    def test_text_node_type_invalid(self):
        text_node = TextNode("Hello", "invalid")
        self.assertRaises(ValueError, text_node_to_html_node, text_node)
