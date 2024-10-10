class HTMLNode():
    # At initialization, any property of an HTMLNode can be None. This is
    # because no tag is just text, certain nodes can have no value, no
    # children, or no props. It makes sense, just seems odd.
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # The tag type represented as a string
        self.value = value  # The value of the tag as a string, typically text.
        self.children = children  # All children next tags underneath it.
        self.props = props  # A dictionary of kv pairs of attributes, eg class.

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = ""
        if self.props is None:
            return props
        for prop in self.props:
            props.join(f" {prop}=\"{self.props[prop]}\"")
        return props

    def __repr__(self):
        html_props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {html_props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag!")
        elif self.children is None or self.children == []:
            raise ValueError("ParentNode must have at least one child!")
        else:
            opening_tag = f"<{self.tag}{self.props_to_html()}>"
            closing_tag = f"</{self.tag}>"
            children = list(map(lambda node: node.to_html(), self.children))
            joined_children = "".join(children)
            return opening_tag + joined_children + closing_tag


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value!")
        elif self.tag is None:
            return str(self.value)
        else:
            opening_tag = f"<{self.tag}{self.props_to_html()}>"
            closing_tag = f"</{self.tag}>"
            return opening_tag + self.value + closing_tag

