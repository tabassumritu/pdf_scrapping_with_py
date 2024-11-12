import os
import PyPDF2
from typing import List, Tuple


class PDFLoader:
    """"Loads pdf from directory"""

    def __init__(self, directory: str):
        self.directory = directory
        self.pdf_files = self._get_pdf_files()

    def _get_pdf_files(self) -> List[str]:
        """get list of pdf files in the directory"""
        return [file for file in os.listdir(self.directory) if file.endswith(".pdf")]

    def load_pdf(self, file_name: str) -> Tuple[PyPDF2.PdfReader, 'file']:
        """loads a single pdf file"""
        file_path = os.path.join(self.directory, file_name)
        try:
            file = open(file_path, 'rb')
            pdf_reader = PyPDF2.PdfReader(file)
            return pdf_reader, file
        except FileNotFoundError:
            raise FileNotFoundError(f'File{file_path} not found')

    def get_pdf_files(self) -> List[str]:
        """Return list of pdf files in the directory"""
        return self.pdf_files
