import unittest

from blocktoblocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_heading_type(self):
        text = "# This is a header"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "heading")

    def test_block_to_heading_type_multiple(self):
        text = "###### This is a header"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "heading")

    def test_block_to_heading_type_no_space(self):
        text = "#This is a header"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_code_type(self):
        text = "```This is a code block```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "code")

    def test_block_to_code_type_no_closure(self):
        text = "```This is a code block"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_quote_type(self):
        text = "> This is a quote"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "quote")

    def test_block_to_quote_type_no_space(self):
        text = ">This is a quote"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_unordered_list_type(self):
        text = "* This is a list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "unordered_list")
    
    def test_block_to_unordered_list_type_no_space(self):
        text = "*This is a list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_ordered_list_type(self):
        text = "1. This is a list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "ordered_list")

    def test_block_to_ordered_list_type_no_space(self):
        text = "1.This is a list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_ordered_list_type_multiple(self):
        text = "1. This is a list item\n2. This is another list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "ordered_list")

    def test_block_to_ordered_list_out_of_order(self):
        text = "1. This is a list item\n3. This is another list item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_paragraph_type(self):
        text = "This is a paragraph"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")