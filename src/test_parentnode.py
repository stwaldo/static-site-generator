import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
        )
        test_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), test_string)

    
    def test_to_html_none(self):
        node = ParentNode([], None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_props_to_html(self):
        node = ParentNode([], "div", {"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

    