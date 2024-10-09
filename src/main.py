from textnode import TextNode, split_old_nodes_link, split_old_nodes_image
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    textnode = TextNode("Hello there!", "normal")
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    l1 = LeafNode("Hello! ", "p")
    l2 = LeafNode("Are you hungry?", "em")
    pnode = ParentNode("span", [l1, l2])
    pnode2 = ParentNode("div", [pnode])
    print(textnode)
    print(pnode2.to_html())
    node = TextNode(
    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    "text"
)
    new_nodes = split_old_nodes_image([node])

    print(new_nodes)


main()

