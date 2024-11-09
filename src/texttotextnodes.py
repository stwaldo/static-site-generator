import re
from node_types.textnode import TextNode
from nodeconverter import TextType

def text_to_textnodes(text):
    # Define regex patterns for different text types
    patterns = {
        TextType.BOLD: re.compile(r"\*\*(.*?)\*\*"),
        TextType.ITALIC: re.compile(r"(?<!\*)\*(?!\*)(.*?)\*(?!\*)"),
        TextType.CODE: re.compile(r"`(.*?)`"),
        TextType.IMAGE: re.compile(r"!\[([^\]]+)\]\(([^)]+)\)"),
        TextType.LINK: re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    }

    # Function to find all matches for a given pattern
    def find_all_matches(pattern, text):
        return [(m.start(), m.end(), m.groups()) for m in pattern.finditer(text)]

    # Find all matches for each pattern
    matches = []
    for text_type, pattern in patterns.items():
        matches.extend([(start, end, text_type, groups) for start, end, groups in find_all_matches(pattern, text)])

    # Sort matches by their start position
    matches.sort(key=lambda x: x[0])

    # Create TextNode objects based on the matches
    nodes = []
    last_end = 0
    for start, end, text_type, groups in matches:
        if start > last_end:
            nodes.append(TextNode(text[last_end:start], TextType.TEXT))
        if text_type in [TextType.IMAGE, TextType.LINK]:
            nodes.append(TextNode(groups[0], text_type, groups[1]))
        else:
            nodes.append(TextNode(groups[0], text_type))
        last_end = end

    # Add any remaining text as a plain text node
    if last_end < len(text):
        nodes.append(TextNode(text[last_end:], TextType.TEXT))

    return nodes