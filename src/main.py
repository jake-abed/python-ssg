from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    textnode = TextNode("Hello there!", "normal")
    l1 = LeafNode("Hello! ", "p")
    l2 = LeafNode("Are you hungry?", "em")
    pnode = ParentNode("span", [l1, l2])
    pnode2 = ParentNode("div", [pnode])
    print(textnode)
    print(pnode2.to_html())


main()

