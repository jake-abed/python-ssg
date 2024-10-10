from textnode import TextNode
from re import findall, split


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delimiter_found = False

    if len(old_nodes) == 0:
        return old_nodes

    for node in old_nodes:
        if delimiter not in node.text:
            new_nodes.append(node)
        else:
            delimiter_found = True
            split_text = node.text.split(delimiter, 2)
            nodes_to_add = []
            node1 = TextNode(split_text[0], node.text_type, node.url)
            node2 = TextNode(split_text[1], text_type, node.url)
            node3 = TextNode(split_text[2], node.text_type, node.url)
            for node in [node1, node2, node3]:
                if node.text != "":
                    nodes_to_add.append(node)
            new_nodes.extend(nodes_to_add)

    if delimiter_found:
        return split_nodes_delimiter(new_nodes, delimiter, text_type)
    else:
        return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, "text")
    nodes = split_old_nodes_image([node])
    nodes = split_old_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    return nodes


def split_old_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        split_text = split(r"!\[[^\[\]]*\]\([^\(\)]*\)", node.text)
        for text in split_text:
            if text != "":
                new_text_node = TextNode(text, node.text_type, node.url)
                new_nodes.append(new_text_node)
            if len(images) > 0:
                image_data = images.pop(0)
                new_image_node = TextNode(image_data[0], "image", image_data[1])
                new_nodes.append(new_image_node)

    return new_nodes


def split_old_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        split_text = split(r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)", node.text)
        for text in split_text:
            if text != "":
                new_text_node = TextNode(text, node.text_type, node.url)
                new_nodes.append(new_text_node)
            if len(links) > 0:
                link_data = links.pop(0)
                new_link_node = TextNode(link_data[0], "link", link_data[1])
                new_nodes.append(new_link_node)

    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return findall(pattern, text)

