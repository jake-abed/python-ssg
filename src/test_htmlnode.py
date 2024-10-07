import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_init_to_none(self):
        node = HTMLNode()
        node1 = HTMLNode()
        self.assertEqual(node.tag, node1.tag)
        print("Nodes initialized with nothing have equal tags")
    
    def test_init_simple(self):
        node = HTMLNode("p", "Hello!")
        node2 = HTMLNode("p", "Hello!")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        print("Nodes initialized with simple values are equal")

    def test_props_to_html(self):
        node = HTMLNode("p", "Hello!", None, {"class": "grass", "href": "chef"})
        node2 = HTMLNode("p", "Hello!", None, {"class": "grass", "href": "chef"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        print("Nodes props to html method creates same result.")


class TestLeafNode(unittest.TestCase):
    def test_init_to_none(self):
        node = LeafNode(None)

        with self.assertRaises(ValueError):
            node.to_html()
        print("Node with None value raises an error!")


if __name__ == "__main__":
    unittest.main()
