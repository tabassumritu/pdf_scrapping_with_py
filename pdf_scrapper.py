from abc import ABC, abstractmethod
from typing import Union, Dict
import PyPDF2


class PDFScraper(ABC):

    def __init__(self, pdf_reader: PyPDF2.PdfReader):
        self.pdf_reader = pdf_reader

    @abstractmethod
    def scrape(self) -> Union[str, Dict[int, str]]:
        """"Abstract method for scraping PDF content"""
        pass
