from app.services.pdf_extractor import PDFExtractor

extractor = PDFExtractor()

document = extractor.extract("data/sample.pdf")

print(f"Document: {document.filename}, Total Pages: {document.total_pages}")
print(document.pages[0].text[:200])  