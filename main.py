import os
import re

def process_lines(lines):
    response = []

    for line in lines:
        # Handle headings
        heading_match = re.match(r'^(#{1,6}) (.*)', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)
            # Check if there's a link in this heading... if so, replace it with an HTML link
            heading_text = re.sub(r'\[(.*?)]\((.*?)\)', r'<a href="\2">\1</a>', heading_text)
            response.append(f'<h{heading_level}>{heading_text}</h{heading_level}>')
        # Handle links and paragraphs
        elif re.match(r'.*\[(.*?)]\((.*?)\).*', line):
            # Replace Markdown links with HTML links in paragraphs
            line = re.sub(r'\[(.*?)]\((.*?)\)', r'<a href="\2">\1</a>', line)
            response.append(f'<p>{line}</p>')
        # Handle paragraphs
        elif line.strip() != '':
            response.append(f'<p>{line}</p>')
        # Ignore blank lines
        else:
            continue

    return response

def markdown_to_html(markdown_text):
    # Divide and conquer... split the Markdown text into lines
    lines = markdown_text.split('\n')

    response = process_lines(lines)

    return '\n'.join(response)

if __name__ == "__main__":
    # Read input from input.md
    with open('input.md', 'r') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown_to_html(markdown_content)

    # Delete output.html if it exists
    output_file = 'output.html'
    if os.path.exists(output_file):
        print(f"Old {output_file} was found. File will be deleted.")
        os.remove(output_file)

    # Write output to output.html
    with open('output.html', 'w') as file:
        file.write(html_content)

    print("Success!! Check output.html for the converted HTML content.")
