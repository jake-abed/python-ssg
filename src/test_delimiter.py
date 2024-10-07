import unittest
from delimit import split_nodes_delimiter
from textnode import TextNode


class DelimiterTest(unittest.TestCase):
    def test_simple_text_node(self):
        node = TextNode("Hi!", "text")
        all_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(all_nodes), 1)

    def test_simple_node_bold(self):
        node = TextNode("Hi! **Wow**!!!", "text")
        all_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(all_nodes), 3)
        self.assertEqual(all_nodes[1].text, "Wow")

    def test_many_nodes_bold(self):
        node = TextNode("Hi, **dude**!", "text")
        node2 = TextNode("You are **so** dang **cool**, huh?", "text")
        all_nodes = split_nodes_delimiter([node, node2], "**", "bold")
        self.assertEqual(len(all_nodes), 8)
        self.assertEqual(all_nodes[1].text, "dude")
        self.assertEqual(all_nodes[7].text_type, "text")
        self.assertEqual(all_nodes[6].text_type, "bold")

    def test_node_chain(self):
        node = TextNode("Hi, **friend**. Are you *hungry*?", "text")
        all_nodes = split_nodes_delimiter([node], "**", "bold")
        all_nodes = split_nodes_delimiter(all_nodes, "*", "italic")
        self.assertEqual(len(all_nodes), 5)
        self.assertEqual(all_nodes[1].text_type, "bold")
        self.assertEqual(all_nodes[3].text_type, "italic")

