import unittest
from textnode import TextNode, text_node_to_html_node
from delimit import (extract_markdown_links,
                     extract_markdown_images,
                     split_old_nodes_image,
                     split_old_nodes_link,
                     text_to_textnodes)


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


class TestTextNodesSplitImage(unittest.TestCase):
    def test_one_node(self):
        text = "Text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)."
        node = TextNode(text, "text")
        result1 = TextNode("Text with a ", "text")
        result2 = TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif")
        result3 = TextNode(".", "text")
        results = [result1, result2, result3]
        self.assertEqual(split_old_nodes_image([node]), results)

    def test_two_nodes(self):
        text = "Text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)."
        text2 = "Shrek a doo ![grip](dip.com) in your shoe!"
        node2 = TextNode(text2, "text")
        node = TextNode(text, "text")
        result1 = TextNode("Text with a ", "text")
        result2 = TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif")
        result3 = TextNode(".", "text")
        result4 = TextNode("Shrek a doo ", "text")
        result5 = TextNode("grip", "image", "dip.com")
        result6 = TextNode(" in your shoe!", "text")
        results = [result1, result2, result3, result4, result5, result6]
        self.assertEqual(split_old_nodes_image([node, node2]), results)


class TestTextNodesSplitLink(unittest.TestCase):
    def test_one_node(self):
        text = "Text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)."
        node = TextNode(text, "text")
        result1 = TextNode("Text with a ", "text")
        result2 = TextNode("rick roll", "link", "https://i.imgur.com/aKaOqIh.gif")
        result3 = TextNode(".", "text")
        results = [result1, result2, result3]
        self.assertEqual(split_old_nodes_link([node]), results)

    def test_two_nodes(self):
        text = "Text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)."
        text2 = "Shrek a doo [grip](dip.com) in your shoe!"
        node2 = TextNode(text2, "text")
        node = TextNode(text, "text")
        result1 = TextNode("Text with a ", "text")
        result2 = TextNode("rick roll", "link", "https://i.imgur.com/aKaOqIh.gif")
        result3 = TextNode(".", "text")
        result4 = TextNode("Shrek a doo ", "text")
        result5 = TextNode("grip", "link", "dip.com")
        result6 = TextNode(" in your shoe!", "text")
        results = [result1, result2, result3, result4, result5, result6]
        self.assertEqual(split_old_nodes_link([node, node2]), results)


class TestTextToTextNodes(unittest.TestCase):
    def test_small(self):
        text = "Hello **my** friend."
        nodes = text_to_textnodes(text)
        expected1 = TextNode("Hello ", "text")
        expected2 = TextNode("my", "bold")
        expected3 = TextNode(" friend.", "text")
        all_expected = [expected1, expected2, expected3]
        self.assertEqual(nodes, all_expected)

    def test_normal(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", "text"),
                    TextNode("text", "bold"),
                    TextNode(" with an ", "text"),
                    TextNode("italic", "italic"),
                    TextNode(" word and a ", "text"),
                    TextNode("code block", "code"),
                    TextNode(" and an ", "text"),
                    TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", "text"),
                    TextNode("link", "link", "https://boot.dev")
                    ]
        self.assertEqual(nodes, expected)

    def test_opening_with_bold_ending_with_italic(self):
        text = "**This** is *that*"
        nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This", "bold"),
                    TextNode(" is ", "text"),
                    TextNode("that", "italic")
                    ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()

