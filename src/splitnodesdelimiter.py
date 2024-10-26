from textnode import TextNode
from nodeconverter import TextType

# takes a list of old nodes, a delimiter, and a text type
# returns a new list of nodes, where any "text" type nodes in the input list are (potentially) split into new nodes base on the syntax

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # if there are unmmatched delimiters, raise an exception
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid markdown syntax: Unmatched delimiters") 
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes