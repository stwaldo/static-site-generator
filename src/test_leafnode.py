import unittest

from node_types.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
        
        def test_to_html(self):
            node = LeafNode("div", "This is a leaf node")
            self.assertEqual(node.to_html(), "<div>This is a leaf node</div>")
    
        def test_props_to_html(self):
            node = LeafNode("div", "This is a leaf node", {"class": "container"})
            self.assertEqual(node.props_to_html(), ' class="container"')
            
        def test_init_no_value(self):
            with self.assertRaises(ValueError):
                LeafNode("div", None)