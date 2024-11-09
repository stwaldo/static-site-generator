import re
from linkextractor import extract_markdown_links
from linkextractor import extract_markdown_images
from nodeconverter import TextType
from node_types.textnode import TextNode

def split_nodes_images(old_nodes):
    # accepts a list of TextNodes, and for each node returns a list of TextNodes with any image links split into separate nodes
    # empty TextNodes are not added to the list

    new_nodes = []
    for node in old_nodes:
        if node.text:
            images = extract_markdown_images(node.text)
            if images:
                parts = re.split(r"(!\[.*?\]\(.*?\))", node.text)
                for part in parts:
                    if part.startswith('![') and part.endswith(')'):
                        match = re.match(r"!\[([^\]]+)\]\(([^)]+)\)", part)
                        if match:
                            new_nodes.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
                    else:
                        if part:
                            new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_links(old_nodes):
    # accepts a list of TextNodes, and for each node returns a list of TextNodes with any URL links split into separate nodes
    # empty TextNodes are not added to the list

    new_nodes = []

    for node in old_nodes:
        if node.text:
            links = extract_markdown_links(node.text)
            if links:
                parts = re.split(r"(\[[^\]]+\]\([^)]+\))", node.text)
                for part in parts:
                    if part.startswith('[') and part.endswith(')'):
                        match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
                        if match:
                            new_nodes.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
                    else:
                        if part:
                            new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes
