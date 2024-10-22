from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, RecursiveJsonSplitter, Language
from langchain_text_splitters import HTMLHeaderTextSplitter, HTMLSectionSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter, MarkdownTextSplitter
import requests

# =================================================================== Text Splitter  ===================================================================
# ======================== CharacterTextSplitter ========================

text = "AI is one of the most exciting advancements in recent years."

chunk_size = 50
chunk_overlap = 20

character_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    # separator="",
    separator="\n\n",
)

c_chunks = character_splitter.split_text(text)
print("========== CharacterTextSplitter ==========")
print(c_chunks)
print(len(c_chunks))

# ======================== RecursiveCharacterTextSplitter ========================
text = "AI is one of the most exciting advancements in recent years."

chunk_size = 50
chunk_overlap = 20

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", " ", ".", ",", "",]
)

r_chunks = recursive_splitter.split_text(text)
print("========== RecursiveCharacterTextSplitter ==========")
print(r_chunks)
print(len(r_chunks))

# ================================================ Json Splitter  ================================================
# This is a large nested json object and will be loaded as a python dict
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()

json_splitter = RecursiveJsonSplitter(max_chunk_size=500)

# This is a large nested json object and will be loaded as a python dict
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()

json_splitter = RecursiveJsonSplitter(max_chunk_size=300)

# Recursively split json data - If you need to access/manipulate the smaller json chunks
j_chunks = json_splitter.split_json(json_data)

print("========== RecursiveJsonSplitter ==========")
# print(j_chunks)  # This print huge amount of JSON data
print(len(j_chunks))
print(j_chunks[0])
print(j_chunks[0]["openapi"])
print(j_chunks[0]["info"])
print(j_chunks[0]["paths"])

# ================================================ Code Splitter  ================================================

# ==================== RecursiveCharacterTextSplitter with out language class ====================
# Sample code to be split
code_text = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def __init__(self):
        self.result = 0

    def calculate(self, func, a, b):
        self.result = func(a, b)
        return self.result
"""

# Initialize the RecursiveCharacterTextSplitter with specific chunk sizes
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Size of each chunk in characters
    chunk_overlap=10,  # Overlap between chunks
    separators=["\n\n", "\n", " "]  # Separators to prioritize splitting
)

# Split the code into chunks
c_chunks = splitter.split_text(code_text)

print("========== RecursiveCharacterTextSplitter ==========")
print(len(c_chunks))
print(c_chunks)

# ==================== RecursiveCharacterTextSplitter with language class ====================

# Sample code to be split
python_code = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""

# Initialize the RecursiveCharacterTextSplitter with specific chunk sizes
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0
)

# Split the code into chunks
c_l_chunks = python_splitter.split_text(python_code)

print("========== RecursiveCharacterTextSplitter with language ==========")
print(len(c_l_chunks))
print(c_l_chunks)

# ================================================ HTML Splitter  ================================================

# ==================== HTMLHeaderTextSplitter ====================

html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on)

header_splits = html_splitter.split_text(html_string)

print("========== HTMLHeaderTextSplitter ==========")

print(header_splits)
print(header_splits[0].page_content)
print(header_splits[0].metadata)

print(header_splits[1].page_content)
print(header_splits[1].metadata)
print(header_splits[1].metadata["Header 1"])

print(header_splits[4].metadata)
print(header_splits[4].metadata["Header 1"])
print(header_splits[4].metadata["Header 2"])
print(header_splits[4].metadata["Header 3"])
print(header_splits[4].page_content)

# ==================== HTMLHeaderTextSplitter ====================
html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

html_splitter = HTMLSectionSplitter(headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)

print("========== HTMLSectionSplitter ==========")
print(html_header_splits)

print(html_header_splits[0].page_content)
print(html_header_splits[0].metadata)

print(html_header_splits[1].page_content)
print(html_header_splits[1].metadata)
print(html_header_splits[1].metadata["Header 2"])

# ================================================ Markdown Splitter  ================================================
# Sample markdown text
markdown_text = """
# Introduction
This is the introduction to the document.

## History
The history section covers the early days of technology.

### Ancient Tech
People have been using technology since the beginning of time.

## Current Technology
We are living in a highly advanced technological world.

### AI and Machine Learning
AI is one of the most exciting advancements in recent years.

# Conclusion
This is the conclusion of the document.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_text)

print("========== MarkdownHeaderTextSplitter ==========")
print(md_header_splits)

print(md_header_splits[0].metadata)
print(md_header_splits[0].page_content)

print(md_header_splits[4].metadata)
print(md_header_splits[4].metadata["Header 1"])
print(md_header_splits[4].metadata["Header 2"])
print(md_header_splits[4].metadata["Header 3"])
print(md_header_splits[4].page_content)
