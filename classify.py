import dspy
import sys
import json
from business_logic import classify_text

# Example usage: python classify.py input.md

def read_markdown(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python classify.py <markdown_file>")
        sys.exit(1)
    md_file = sys.argv[1]
    text = read_markdown(md_file)
    category = classify_text(text)
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
