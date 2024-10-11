from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value cannot be None")
        super().__init__(tag, value, [], props)

    def to_html(self):
        tag = self.tag
        if self.tag is None:
            open_tag = ""
            close_tag = ""
        else:
            open_tag = f"<{tag}{self.props_to_html()}>"
            close_tag = f"</{tag}>"
        return f"{open_tag}{self.value}{close_tag}"