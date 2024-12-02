import unittest
from markdowntohtmlnode import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_heading(self):
        markdown = "# Heading 1"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'h1')
        self.assertEqual(html_node.children[0].children[0].value, 'Heading 1')
        
    def test_heading2(self):
        markdown = "## Heading 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'h2')
        self.assertEqual(html_node.children[0].children[0].value, 'Heading 2')

    def test_code_block(self):
        markdown = "```\ncode block\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'pre')
        self.assertEqual(html_node.children[0].children[0].tag, 'code')
        self.assertEqual(html_node.children[0].children[0].value, 'code block')

    def test_blockquote(self):
        markdown = "> This is a quote"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'blockquote')
        self.assertEqual(html_node.children[0].children[0].value, 'This is a quote')

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'ul')
        self.assertEqual(html_node.children[0].children[0].tag, 'li')
        self.assertEqual(html_node.children[0].children[0].children[0].value, 'Item 1')
        self.assertEqual(html_node.children[0].children[1].tag, 'li')
        self.assertEqual(html_node.children[0].children[1].children[0].value, 'Item 2')

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'ol')
        self.assertEqual(html_node.children[0].children[0].tag, 'li')
        self.assertEqual(html_node.children[0].children[0].children[0].value, 'First item')
        self.assertEqual(html_node.children[0].children[1].tag, 'li')
        self.assertEqual(html_node.children[0].children[1].children[0].value, 'Second item')

    def test_paragraph(self):
        markdown = "This is a paragraph."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'p')
        self.assertEqual(html_node.children[0].children[0].value, 'This is a paragraph.')

if __name__ == '__main__':
    unittest.main()