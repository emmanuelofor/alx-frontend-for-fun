#!/usr/bin/python3
"""
Script for converting Markdown files to HTML format.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Transforms a Markdown file into its HTML representation.
    """
    # Ensure the provided Markdown file exists
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read and convert the Markdown content to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Convert Markdown headers to HTML headers
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Save the converted content to the specified output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    # Ensure correct command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Retrieve input and output filenames from arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Perform the conversion
    convert_markdown_to_html(input_file, output_file)

    # Signal successful completion
    sys.exit(0)

