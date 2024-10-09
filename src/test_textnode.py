import unittest
from textnode import (TextNode,
                      text_node_to_html_node,
                      extract_markdown_links,
                      extract_markdown_images)


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


class TestExtractImage(unittest.TestCase):
    def test_one_image(self):
        text = "Text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)."
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), result)

    def test_two_images(self):
        text1 = "1. ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        text2 = " 2. ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text = text1 + text2
        result = [
                    ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                 ]
        self.assertEqual(extract_markdown_images(text), result)

class TestExtractLink(unittest.TestCase):
    def test_one_link(self):
        text = "Text with [wtrmln chat](https://wtrmln.chat)."
        result = [("wtrmln chat", "https://wtrmln.chat")]
        self.assertEqual(extract_markdown_links(text), result)

    def text_two_links(self):
        text1 = "1. [walter](https://walter.melon) site"
        text2 = "2. [wet](https://walter.wet) site"
        text = text1 + text2
        result = [
                    ("walter", "https://walter.melon"),
                    ("wet", "https://walter.wet")
                 ]
        self.assertEqual(extract_markdown_links(text), result)


if __name__ == "__main__":
    unittest.main()

