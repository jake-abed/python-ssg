from textnode import TextNode


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
            node1 = TextNode(split_text[0], node.text_type, node.url)
            node2 = TextNode(split_text[1], text_type, node.url)
            node3 = TextNode(split_text[2], node.text_type, node.url)
            new_nodes.extend([node1, node2, node3])

    if delimiter_found:
        return split_nodes_delimiter(new_nodes, delimiter, text_type)
    else:
        return new_nodes

