import os
import PyPDF2
from typing import List

class PDFLoader:

    """"Loads pdf from directory"""
    def __init__(self, directory: str):
        self.directory = directory
        self.pdf_files = self._get_pdf_files()

    def _get_pdf_files(self) -> List[str]:
        """get list of pdf files in the directory"""
        return [file for file in os.listdir(self.directory) if file.endswith(".pdf")]

    def load_pdf(selfself, file_name: str) -> PyPDF2.PdfReader:
        """loads a single single pdf file"""
        file_path = os.path.join(self.directory, file_name)
        try:
            with open(file_path, 'rb') as file:
                return PyPDF2.PdfReader(file)
        except FileNotFoundError:
            raise FileNotFoundError(f'File{file_path} not found')

    def get_pdf_files(self)-> List[str]:
        """Return list of pdf files in the directopry"""
        return self.pdf_files

