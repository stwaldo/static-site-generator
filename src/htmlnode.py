class HTMLNode():
    # tag: str - the tag of the node
    # value: str - the value of the node
    # children: list - the children of the node
    # props: dict - the properties of the node
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props = ""
        if self.props:
            for key, value in self.props.items():
                props += f' {key}="{value}"'
        return props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    