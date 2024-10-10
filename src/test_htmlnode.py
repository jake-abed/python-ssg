import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import markdown_to_html_node, extract_title


class TestHTMLNode(unittest.TestCase):
    def test_init_to_none(self):
        node = HTMLNode()
        node1 = HTMLNode()
        self.assertEqual(node.tag, node1.tag)

    def test_init_simple(self):
        node = HTMLNode("p", "Hello!")
        node2 = HTMLNode("p", "Hello!")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)

    def test_props_to_html(self):
        node = HTMLNode("p", "Hello!", None, {"class": "grass", "href": "chef"})
        node2 = HTMLNode("p", "Hello!", None, {"class": "grass", "href": "chef"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())


class TestParentNode(unittest.TestCase):
    def test_init_with_no_child(self):
        node = ParentNode(None, None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_simple_nesting(self):
        leaf = LeafNode("Hi!", "b", {"class": "p-leaf"})
        node = ParentNode("p", [leaf])
        node2 = ParentNode("p", [leaf])
        self.assertEqual(node.to_html(), node2.to_html())

    def test_nesting(self):
        leaf = LeafNode("A", "span", {"class": "test", "id": "A"})
        leaf2 = LeafNode("B", "p", {"class": "best", "id": "B"})
        leaf3 = LeafNode("C", "a", {"class": "rest", "id": "C", "href": "/"})
        node = ParentNode("div", [leaf, leaf2, leaf3], {"class": "grass"})
        node2 = ParentNode("section", [node], {"class": "mass"})
        node3 = ParentNode("section", [node], {"class": "mass"})
        self.assertEqual(node3.to_html(), node2.to_html())

    def test_nesting_value_error(self):
        node = ParentNode("div", [], {"class": "grass"})
        node2 = ParentNode("section", [node], {"class": "mass"})
        with self.assertRaises(ValueError):
            node2.to_html()


class TestLeafNode(unittest.TestCase):
    def test_init_to_none(self):
        node = LeafNode(None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_equal_leaf(self):
        node = LeafNode("Welcome to hell", "p", {"href": "https://wtrmln.chat"})
        node2 = LeafNode("Welcome to hell", "p", {"href": "https://wtrmln.chat"})
        self.assertEqual(node.to_html(), node2.to_html())

    def test_empty_tag(self):
        node = LeafNode("Hello!")
        node2 = LeafNode("Hello!")
        self.assertEqual(node.to_html(), node2.to_html())


class TestMarkDownToHTMLNodes(unittest.TestCase):
    def test_simplest_case(self):
        md = "# Hi!"
        node = markdown_to_html_node(md)
        ln = LeafNode("Hi!")
        pn = ParentNode("h1", [ln])
        rn = ParentNode("div", [pn])
        self.assertEqual(node.to_html(), rn.to_html())

    def test_single_header_nested(self):
        md = "# Hi **friend**!"
        node = markdown_to_html_node(md)
        ln = LeafNode("Hi ")
        ln2 = LeafNode("friend", "b")
        ln3 = LeafNode("!")
        pn = ParentNode("h1", [ln, ln2, ln3])
        rn = ParentNode("div", [pn])
        self.assertEqual(node.to_html(), rn.to_html())

    def test_big_md(self):
        md = """# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."

In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in *The Lord of the Rings*. You can find the [wiki here](https://lotr.fandom.com/wiki/Main_Page).

## Introduction

This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its *legendarium*. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.

## A Rich Tapestry of Lore

One cannot simply discuss *The Lord of the Rings* without acknowledging the bedrock upon which it stands: **The Silmarillion**. This compendium of mythopoeic tales sets the stage for Middle-earth's history, from the creation myth of Eä to the epic sagas of the Elder Days. It is a testament to Tolkien's unparalleled skill as a linguist and myth-maker, crafting:

1. [ ] An elaborate pantheon of deities (the `Valar` and `Maiar`)
2. [ ] The tragic saga of the Noldor Elves
3. [ ] The rise and fall of great kingdoms such as Gondolin and Númenor

```
print("Lord")
print("of")
print("the")
print("Rings")
```

## The Art of **World-Building**

### Crafting Middle-earth

Tolkien's Middle-earth is a realm of breathtaking diversity and realism, brought to life by his meticulous attention to detail. This world is characterized by:

- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as Quenya and Sindarin, each with its own grammar and lexicon.
- **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of Mordor, is depicted with such vividness that it feels as tangible as our own world.
- **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at bygone eras, giving the world a lived-in, authentic feel."""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h2>The Art of <b>", html)
        self.assertIn("<div><img", html)
        self.assertEqual(html.count("<li>"), 6)


class TestExtractH1FromMd(unittest.TestCase):
    def test_simple_md(self):
        md = "# An H1"
        self.assertEqual(extract_title(md), "An H1")

    def test_no_h1_simple(self):
        md = ">Dog"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_deep_h1(self):
        md = """[Start]("/")

        - A Thing
        - Another Thing
        - Sonic?

        Some **text** to read.

        ## H2

        # H1"""

        self.assertEqual(extract_title(md), "H1")


if __name__ == "__main__":
    unittest.main()
