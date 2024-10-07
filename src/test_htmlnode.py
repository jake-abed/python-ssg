import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


if __name__ == "__main__":
    unittest.main()
