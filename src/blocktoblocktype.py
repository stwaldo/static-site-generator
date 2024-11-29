import re


def block_to_block_type(block):
    # takes a single block of markdown text as input and returns a string representing the type of block it is. You can assume all leading and trailing whitespace was already stripped

    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    header_pattern = re.compile(r"^(#{1,6})\s")
    if header_pattern.match(block):
        return "heading"
    # Code blocks must start with 3 backticks and end with 3 backticks.
    code_pattern = re.compile(r"^```[\s\S]*?```$")
    if code_pattern.match(block):
        return "code"
    # Every line in a quote block must start with a > character.
    quote_pattern = re.compile(r"^>\s")
    if quote_pattern.match(block):
        return "quote"
    # Every line in an unordered list block must start with a * or - character, followed by a space.
    unordered_list_pattern = re.compile(r"^[*-]\s")
    if unordered_list_pattern.match(block):
        return "unordered_list"

    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    lines = block.split('\n')
    if all(re.match(rf"^{i+1}\.\s", line) for i, line in enumerate(lines)):
        return "ordered_list"
    
    # If none of the above conditions are met, the block is a normal paragraph.
    return "paragraph"
    