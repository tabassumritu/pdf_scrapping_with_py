import PyPDF2

from pdf_scrapper import PDFScraper
from typing import List, Dict

"""Extracting all text from pdf"""


class SimpleScraper(PDFScraper):
    def scrape(self) -> str:
        all_text = ''
        for page_num in range(len(self.pdf_reader.pages)):
            page = self.pdf_reader.pages[page_num]
            all_text += page.extractText() + "\n"

        return all_text


"""Extract data by keyword"""


class KeywordScraper(PDFScraper):
    def __init__(self, pdf_reader: PyPDF2.PdfReader, keywords: List[str]):
        super().__init__(pdf_reader)
        self.keywords = keywords

    def scrape(self) -> Dict[int, str]:
        result = {}

        for page_num in range(len(self.pdf_reader.pages)):
            page = self.pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if any(keyword in page_text for keyword in self.keywords):
                result[page_num + 1] = page_text

        return result
