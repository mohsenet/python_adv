#### The 'pypdf' library (previously known as PyPDF2) is quite powerful for basic PDF operations.

```python
from pypdf import PdfReader


# Create a PDF reader object
reader = PdfReader("example.pdf")

# Get the number of pages
print(f"Number of pages: {len(reader.pages)}")

# Extract text from the first page
first_page = reader.pages[0]
text = first_page.extract_text()
print("Text from first page:")
print(text)
```