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


class TestBlockToBlockType(unittest.TestCase):
    def test_to_heading_one(self):
        block = "# Scooby dooby doo"
        self.assertEqual(blocks.block_to_block_type(block), "heading")

    def test_to_heading_three(self):
        block = "### Scooby tooby tree"
        self.assertEqual(blocks.block_to_block_type(block), "heading")

    def test_heading_six(self):
        block = "###### Devil"
        self.assertEqual(blocks.block_to_block_type(block), "heading")

    def test_code(self):
        block = """``` l337 h4x0r
            == === "trash" ```"""
        self.assertEqual(blocks.block_to_block_type(block), "code")

    def test_single_line_quote(self):
        block = "> Something, someting..."
        self.assertEqual(blocks.block_to_block_type(block), "quote")

    def test_multi_line_quote(self):
        block = """>Hi!
            >You look happy!
            >But are you?
            > -Benjamin Button"""
        self.assertEqual(blocks.block_to_block_type(block), "quote")


if __name__ == "__main__":
    unittest.main()

