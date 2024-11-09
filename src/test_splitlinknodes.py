import unittest
from nodeconverter import TextType
from splitlinknodes import split_nodes_links
from splitlinknodes import split_nodes_images
from textnode import TextNode

class TestSplitLinkNodes(unittest.TestCase):
        
        def test_split_single_link_node(self):
            node1 = TextNode("This is an example of a link [foo bar](http://example.com)", TextType.TEXT)
            old_nodes = [node1]
            new_nodes = split_nodes_links(old_nodes)
            self.assertEqual(new_nodes, [
                 TextNode("This is an example of a link ", TextType.TEXT),
                 TextNode(text="foo bar", text_type=TextType.LINK, url="http://example.com")
                 ])
        
        def test_split_multiple_link_nodes(self):
            node1 = TextNode("This is an example of a link [foo bar](http://example.com) and another link [baz](http://example.com/another)", TextType.TEXT)
            old_nodes = [node1]
            new_nodes = split_nodes_links(old_nodes)
            self.assertEqual(new_nodes, [
                TextNode("This is an example of a link ", TextType.TEXT), 
                TextNode("foo bar", TextType.LINK, "http://example.com"), 
                TextNode(" and another link ", TextType.TEXT), 
                TextNode("baz", TextType.LINK, "http://example.com/another")])
        
        def test_no_link_nodes_returns_original_list_with_image(self):
            node1 = TextNode("This is an example of an image ![foo bar](http://example.com/image.jpg)", TextType.TEXT)
            old_nodes = [node1]
            new_nodes = split_nodes_links(old_nodes)
            self.assertEqual(new_nodes, [TextNode("This is an example of an image ![foo bar](http://example.com/image.jpg)", TextType.TEXT)])
        
        def test_split_single_image_node(self):
            old_nodes = [TextNode("This is an example of an image ![foo bar](http://example.com/image.jpg)", TextType.TEXT)]
            new_nodes = split_nodes_images(old_nodes)
            self.assertEqual(new_nodes, [
                 TextNode("This is an example of an image ", TextType.TEXT), 
                 TextNode("foo bar", TextType.IMAGE, "http://example.com/image.jpg")
                          ])
        
        def test_split_multiple_image_nodes(self):
            old_nodes = [TextNode("This is an example of an image ![foo bar](http://example.com/image.jpg) and another image ![baz](http://example.com/another.jpg)", TextType.TEXT)]
            new_nodes = split_nodes_images(old_nodes)
            self.assertEqual(new_nodes, [
                TextNode("This is an example of an image ", TextType.TEXT), 
                TextNode("foo bar", TextType.IMAGE, "http://example.com/image.jpg"), 
                TextNode(" and another image ", TextType.TEXT), 
                TextNode("baz", TextType.IMAGE, "http://example.com/another.jpg")])
            
        def test_no_image_nodes_returns_original_list(self):
            old_nodes = [TextNode("This is an example of a link [foo bar](http://example.com)", TextType.TEXT)]
            new_nodes = split_nodes_images(old_nodes)
            self.assertEqual(new_nodes, [TextNode("This is an example of a link [foo bar](http://example.com)", TextType.TEXT)])