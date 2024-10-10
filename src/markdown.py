import blocks
import delimit
from htmlnode import ParentNode
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    split_blocks = blocks.markdown_to_blocks(markdown)
    converted_blocks = []
    for block in split_blocks:
        html_node = unknown_block_to_html_node(block)
        if html_node is not None:
            converted_blocks.append(html_node)
    return ParentNode("div", converted_blocks)


def unknown_block_to_html_node(block):
    block_type = blocks.block_to_block_type(block)
    match block_type:
        case "heading":
            return heading_to_html_node(block)
        case "code":
            return code_block_to_html_node(block)
        case "quote":
            return quote_block_to_html_node(block)
        case "unordered_list":
            return ul_block_to_html_node(block)
        case "ordered_list":
            return ol_block_to_html_node(block)
        case "paragraph":
            return paragraph_block_to_html_node(block)
        case _:
            return None


def heading_to_html_node(block):
    hashtags = block.split(" ")[0]
    h_count = len(hashtags)
    text = block[h_count + 1:]
    return ParentNode(f"h{h_count}", text_nodes_to_html_nodes(text))


def code_block_to_html_node(block):
    text = block.lstrip("```").rstrip("```")
    return ParentNode("code", text_nodes_to_html_nodes(text))


def quote_block_to_html_node(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        deformatted = line[1:]
        line_children = text_nodes_to_html_nodes(deformatted)
        children.append(ParentNode("p", line_children))
    return ParentNode("blockquote", children)


def ul_block_to_html_node(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        deformatted = line[2:]
        line_children = text_nodes_to_html_nodes(deformatted)
        children.append(ParentNode("li", line_children))
    return ParentNode("ul", children)


def ol_block_to_html_node(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        deformatted = line[3:]
        line_children = text_nodes_to_html_nodes(deformatted)
        children.append(ParentNode("li", line_children))
    return ParentNode("ol", children)


def paragraph_block_to_html_node(block):
    text = block.replace("\n", "<br>")
    children = text_nodes_to_html_nodes(text)
    return ParentNode("div", children)


def text_nodes_to_html_nodes(text):
    children = delimit.text_to_textnodes(text)
    return list(map(lambda tn: text_node_to_html_node(tn), children))

