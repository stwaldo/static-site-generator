import re

def extract_markdown_images(text):
    # accepts a string of markdown text with an image link in format ![foo bar](http://example.com/image.jpg)
    # returns a list of tuples, ie. [("foo bar", "http://example.com/image.jpg")]

    return re.findall(r"!\[([^\]]+)\]\(([^)]+)\)", text)

def extract_markdown_links(text):
    # accepts a string of markdown text with a link in format [foo bar](http://example.com)
    # returns a list of tuples, ie. [("foo bar", "http://example.com")]
    # ignores images

    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)