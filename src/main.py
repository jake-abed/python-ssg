from textnode import TextNode, extract_markdown_images
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
    print(extract_markdown_images(text))

main()

