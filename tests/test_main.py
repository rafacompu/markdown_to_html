import unittest
from main import markdown_to_html

class TestMarkdownToHTMLConversion(unittest.TestCase):

    def test_heading_conversion(self):
        # Test single heading conversion
        input_md = "# Heading 1"
        expected_html = "<h1>Heading 1</h1>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_multiple_heading_conversion(self):
        # Test multiple headings conversion
        input_md = "# Heading 1\n## Heading 2\n### Heading 3"
        expected_html = "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_paragraph_conversion(self):
        # Test paragraph conversion
        input_md = "This is a paragraph."
        expected_html = "<p>This is a paragraph.</p>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_link_conversion(self):
        # Test link conversion
        input_md = "[OpenAI](https://www.openai.com)"
        expected_html = '<p><a href="https://www.openai.com">OpenAI</a></p>'
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_link_in_paragraph(self):
        # Test conversion of a paragraph with a link
        input_md = "This is a paragraph with a [link](https://example.com)."
        expected_html = '<p>This is a paragraph with a <a href="https://example.com">link</a>.</p>'
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_link_in_heading(self):
        # Test conversion of a heading with a link
        input_md = "## Heading with a [link](https://example.com)"
        expected_html = '<h2>Heading with a <a href="https://example.com">link</a></h2>'
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_blank_lines(self):
        # Test conversion ignoring blank lines
        input_md = "\n\n# Heading 1\n\nParagraph\n\n"
        expected_html = "<h1>Heading 1</h1>\n<p>Paragraph</p>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_combined_input(self):
        # Test combined input with multiple elements
        input_md = "# Header one\n\nHello there\n\nHow are you?\nWhat's going on?\n\n## Another Header\n\nThis is a paragraph [with an inline link](http://google.com). Neat, eh?\n\n## This is a header [with a link](http://yahoo.com)"
        expected_html = "<h1>Header one</h1>\n<p>Hello there</p>\n<p>How are you?</p>\n<p>What's going on?</p>\n<h2>Another Header</h2>\n<p>This is a paragraph <a href=\"http://google.com\">with an inline link</a>. Neat, eh?</p>\n<h2>This is a header <a href=\"http://yahoo.com\">with a link</a></h2>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_empty_input(self):
        # Test empty input
        input_md = ""
        expected_html = ""
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_input_with_only_spaces(self):
        # Test input with only spaces
        input_md = "   "
        expected_html = ""
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_malformed_link(self):
        # Test input with malformed link
        input_md = "This is a [broken link(https://example.com)"
        expected_html = "<p>This is a [broken link(https://example.com)</p>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_escaped_markdown_characters(self):
        # Test input with escaped markdown characters
        input_md = "#Not a heading"
        expected_html = "<p>#Not a heading</p>"
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_multiple_links_in_line(self):
        # Test input with multiple links in one line
        input_md = "This line has [link1](https://example1.com) and [link2](https://example2.com)."
        expected_html = '<p>This line has <a href="https://example1.com">link1</a> and <a href="https://example2.com">link2</a>.</p>'
        self.assertEqual(markdown_to_html(input_md), expected_html)


if __name__ == "__main__":
    unittest.main()
