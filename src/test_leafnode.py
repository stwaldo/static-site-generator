import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
        
        def test_to_html(self):
            node = LeafNode("This is a leaf node", "div")
            self.assertEqual(node.to_html(), "<div>This is a leaf node</div>")
    
        def test_to_html_none(self):
            node = LeafNode(None, "div")
            with self.assertRaises(ValueError):
                node.to_html()
    
        def test_props_to_html(self):
            node = LeafNode("This is a leaf node", "div", {"class": "container"})
            self.assertEqual(node.props_to_html(), ' class="container"')