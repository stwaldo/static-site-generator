from blocktoblocktype import block_to_block_type
from markdowntoblocks import markdown_to_blocks
from node_types.leafnode import LeafNode
from node_types.parentnode import ParentNode
from nodeconverter import text_node_to_html_node
from texttotextnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode(tag='div', children=[])
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case "heading":
                parent_node.add_child(create_heading_node(block))
            case "code":
                parent_node.add_child(create_code_node(block))
            case "quote":
                parent_node.add_child(create_quote_node(block))
            case "unordered_list":
                parent_node.add_child(create_unordered_list_node(block))
            case "ordered_list":
                parent_node.add_child(create_ordered_list_node(block))
            case "paragraph":
                parent_node.add_child(create_paragraph_node(block))    
            case _:
                raise ValueError(f"Invalid block type: {block_type}")
            
    return parent_node

def create_heading_node(block):
    heading_level = len(block.split()[0])
    heading_text = block[heading_level + 1:].strip()
    heading_children = text_to_children(heading_text)
    return ParentNode(tag=f'h{heading_level}', children=heading_children)

def create_code_node(block):
    code_content = block[3:-3].strip()
    return ParentNode(tag='pre', children=[LeafNode(tag='code', value=code_content)])

def create_quote_node(block):
    quote_text = block[2:].strip()
    quote_children = text_to_children(quote_text)
    return ParentNode(tag='blockquote', children=quote_children)

def create_unordered_list_node(block):
    return ParentNode(tag='ul', children=create_list_children(block))

def create_ordered_list_node(block):
    return ParentNode(tag='ol', children=create_list_children(block))

def create_list_children(block):
    list_items = block.split('\n')
    list_children = []
    for item in list_items:
        list_children.append(ParentNode(tag='li', children=text_to_children(item[2:].strip())))  # Trim leading spaces
    return list_children

def create_paragraph_node(block):
    return ParentNode(tag='p', children=text_to_children(block))


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children
