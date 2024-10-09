import unittest
import blocks


class TestDocToBlock(unittest.TestCase):
    def test_simple_doc_to_block(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
                    "# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    """* This is the first list item in a list block
* This is a list item
* This is another list item"""
                    ]
        self.assertEqual(blocks.markdown_to_blocks(text), expected)

    def test_one_line_doc_to_block(self):
        text = "# Heading time!"
        expected = ["# Heading time!"]
        self.assertEqual(blocks.markdown_to_blocks(text), expected)


if __name__ == "__main__":
    unittest.main()

