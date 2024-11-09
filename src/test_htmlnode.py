import unittest

from node_types.htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

    def test_props_to_html_none(self):
        node = HTMLNode("div", "This is a div", [])
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(repr(node), 'HTMLNode(div, This is a div, [], {\'class\': \'container\'})')

    def test_to_html(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertRaises(NotImplementedError, node.to_html)