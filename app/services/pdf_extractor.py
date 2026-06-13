from ..models.document import Document
from ..models.page import Page
import pymupdf  # PyMuPDF


class PDFExtractor:

    """
    PDF extraction service.

    Converts PDF files into Document objects containing
    Page objects for downstream chunking and retrieval.

    This service is responsible only for extraction.
    Chunking and embedding are handled separately.
    """

    def extract(self, pdf_path: str) -> Document:
        """
        Extract text from a PDF and convert it into
        a Document object containing Page objects.
        """
        pdf = pymupdf.open(pdf_path)  

        total_pages = pdf.page_count

        pages = []
        
        for page_number in range(total_pages):
            page = pdf.load_page(page_number)

            text = page.get_text()

            page_obj = Page( page_number = page_number + 1, text = text)
            pages.append(page_obj)
            
        pdf.close()
        document = Document(filename = pdf_path, total_pages = total_pages, pages = pages)
        return document
