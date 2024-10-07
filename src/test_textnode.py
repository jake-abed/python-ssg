import unittest
from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("Text node!", "normal")
        node2 = TextNode("Text node!", "normal", None)
        self.assertEqual(node, node2)

    def test_text_diff(self):
        node = TextNode("Test node!", "bold")
        node2 = TextNode("Text node?", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_diff(self):
        node = TextNode("Test node!", "text")
        node2 = TextNode("Test node!", "bold")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_text(self):
        node = TextNode("Test node", "text")
        node2 = TextNode("Test node", "text")
        html = text_node_to_html_node(node)
        html2 = text_node_to_html_node(node2)
        self.assertEqual(html.to_html(), html2.to_html())

    def test_text_node_to_html_unknown(self):
        node = TextNode("Best node", "dog")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_text_node_to_html_bold(self):
        node = TextNode("Hi!", "bold")
        node2 = TextNode("Hi!", "bold")
        html = text_node_to_html_node(node)
        html2 = text_node_to_html_node(node2)
        self.assertEqual(html.to_html(), html2.to_html())

    def test_text_node_to_html_link(self):
        node = TextNode("Hi!", "link", "/")
        node2 = TextNode("Hi!", "link", "/")
        html = text_node_to_html_node(node)
        html2 = text_node_to_html_node(node2)
        self.assertEqual(html.to_html(), html2.to_html())

    def test_text_node_to_html_img(self):
        node = TextNode("Hi!", "image", "/")
        node2 = TextNode("Hi!", "image", "/")
        html = text_node_to_html_node(node)
        html2 = text_node_to_html_node(node2)
        self.assertEqual(html.to_html(), html2.to_html())



if __name__ == "__main__":
    unittest.main()

