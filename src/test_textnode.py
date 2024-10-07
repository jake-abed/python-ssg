import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        print("Standard nodes are equal")

    def test_url(self):
        node = TextNode("Text node!", "normal")
        node2 = TextNode("Text node!", "normal", None)
        self.assertEqual(node, node2)
        print("TextNodes are equal with or without url provided")

    def test_text_diff(self):
        node = TextNode("Test node!", "bold")
        node2 = TextNode("Text node?", "bold")
        self.assertNotEqual(node, node2)
        print("Different nodes are not equal")


if __name__ == "__main__":
    unittest.main()

