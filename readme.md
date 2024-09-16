# Markdown to HTML Converter

This project is a simple Markdown to HTML converter implemented in Python. It converts a subset of Markdown syntax to HTML, handling headings, paragraphs, and links. The converter reads from an `input.md` file and outputs the converted content to an `output.html` file.

## Features

- Converts Markdown headings (`# Heading 1` to `###### Heading 6`) to corresponding HTML headings (`<h1>` to `<h6>`).
- Transforms Markdown links (`[Link text](URL)`) to HTML links (`<a href="URL">Link text</a>`).
- Wraps plain text and paragraphs in `<p>` tags.
- Ignores blank lines and handles special characters correctly by escaping them.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. **Clone the Repository** (if hosted on a version control system like GitHub):

   ```bash
   git clone https://github.com/yourusername/markdown-to-html.git
   cd markdown-to-html


2. **Download the Source Code** (if hosted as a ZIP file):

   ```bash
   
    cd markdown-to-html-master
   
    ```
   

### Usage

1. Add your Markdown content to the `input.md` file.
2. Run the Python script:

   ```bash
   python main.py
   ```
   
3. Open the `output.html` file to view the converted HTML content.

## Example

### Running tests

```bash
python -m unittest test_main.py
```

