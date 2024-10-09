from enum import Enum
from htmlnode import LeafNode
from re import findall


class TextNodeLeafType(Enum):
    text = 1
    bold = 2
    italic = 3
    code = 4
    link = 5
    image = 6


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_equal = self.text == other.text
        text_type_equal = self.text_type == other.text_type
        url_equal = self.url == other.url

        return (text_equal and text_type_equal and url_equal)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextNodeLeafType.text.name:
            return LeafNode(text_node.text)
        case TextNodeLeafType.bold.name:
            return LeafNode(text_node.text, "b")
        case TextNodeLeafType.italic.name:
            return LeafNode(text_node.text, "i")
        case TextNodeLeafType.code.name:
            return LeafNode(text_node.text, "code")
        case TextNodeLeafType.link.name:
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        case TextNodeLeafType.image.name:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("TextNode must be one of the accepted LeafTypes")


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\((\)]*)\)"
    return findall(pattern, text)


