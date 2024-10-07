import unittest
from htmlnode import HTMLNode, LeafNode


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
