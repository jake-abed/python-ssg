from textnode import TextNode
from htmlnode import ParentNode, LeafNode
import delimit
import blocks


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

    test_text2 =  """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


   

* This is the first list item in a list block
* This is a list item
* This is another list item

* This is yet another list item"""
    print(blocks.markdown_to_blocks(test_text2))


main()

