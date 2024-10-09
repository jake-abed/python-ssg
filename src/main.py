from textnode import TextNode
from htmlnode import ParentNode, LeafNode
import delimit


def main():
    textnode = TextNode("Hello there!", "normal")
    l1 = LeafNode("Hello! ", "p")
    l2 = LeafNode("Are you hungry?", "em")
    pnode = ParentNode("span", [l1, l2])
    pnode2 = ParentNode("div", [pnode])
    print(textnode)
    print(pnode2.to_html())

    test_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(delimit.text_to_textnodes(test_text))


main()

