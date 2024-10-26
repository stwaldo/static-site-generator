import unittest

from nodeconverter import TextType
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_single_node_split(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]

        self.assertEqual(new_nodes, expected)

    def test_multiple_node_split(self):
        node_1 = TextNode("This is text with a `code block` word", TextType.CODE)
        node_2 = TextNode("This is another text with a `different code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node_1, node_2], "`", TextType.CODE)

        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT), TextNode("This is another text with a ", TextType.TEXT), TextNode("different code block", TextType.CODE), TextNode(" word", TextType.TEXT)]

        self.assertEqual(new_nodes, expected)

    def test_single_node_with_no_other_text(self):
        node = TextNode("`code block`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("code block", TextType.CODE)]

        self.assertEqual(new_nodes, expected)

    def test_single_node_with_delimiter_first(self):
        node = TextNode("`code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]

        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimiters_raises_exception(self):
        node = TextNode("This is text with a `code block word", TextType.CODE)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)