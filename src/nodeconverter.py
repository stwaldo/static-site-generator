from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT_TYPE_TEXT = "text"
    TEXT_TYPE_BOLD = "bold"
    TEXT_TYPE_ITALIC = "italic"
    TEXT_TYPE_CODE = "code"
    TEXT_TYPE_LINK = "link"
    TEXT_TYPE_IMAGE = "image"

# accepts a TextNode and returns a LeafNode
def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if isinstance(text_type, str):
        text_type = TextType(text_type)

    match text_type:
        case TextType.TEXT_TYPE_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.TEXT_TYPE_BOLD:
            return LeafNode("b", text_node.text)
        case TextType.TEXT_TYPE_ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.TEXT_TYPE_CODE:
            return LeafNode("code", text_node.text)
        case TextType.TEXT_TYPE_LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.TEXT_TYPE_IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid text type")
        