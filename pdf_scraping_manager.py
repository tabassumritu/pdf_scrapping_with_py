from pdf_loader import PDFLoader
from specialized_scraper import SimpleScraper
from database_handler import DatabaseHandler
from export_mixin import ExportMixin
from scrap_mode import ScrapeMode
from typing import List


class PDFScrapingManager(ExportMixin):
    """Manage PDF scraping tasks and handles data exports"""

    def __init__(self, directory: str, mode: ScrapeMode, export_formats: List[str]):
        self.directory = directory
        self.mode = mode
        self.export_formats = export_formats
        self.db_handler = DatabaseHandler()
        self.loader = PDFLoader(directory)
        print("Pdf Scraping manager initialized")

    def run_single_scraping(self, file_name: str):
        """Scrapes a single pdf file and exports data based on user preferences"""

        try:
            print(f'Starting Scraping for {file_name}')
            pdf_reader, file_handle = self.loader.load_pdf(file_name)

            # scraping simple scraper for extracting all text
            scraper = SimpleScraper(pdf_reader)
            print(f'Scraping content from {file_name}')
            # perform scraping
            scraped_data = scraper.scrape()

            # log success and save to the database
            self.db_handler.saved_scraped_data(file_name, {1: scraped_data})
            self.db_handler.saved_pdf_log_status(file_name, 'Success')

            # export to requested formats
            if 'json' in self.export_formats:
                print(f'Exporting {file_name} to JSON format')
                self.export_to_json(scraped_data, file_name)

            if 'csv' in self.export_formats:
                print(f'Exporting {file_name} to csv format')
                self.export_to_csv(scraped_data, file_name)


        except Exception as e:
            print(f'An error occured {e}')
            print(f'Failed to scrape {file_name}. error: {e}')
            self.db_handler.saved_pdf_log_status(file_name, f'An error occured {e}')

    def run_all_scraping(self):
        """scrap all pdf files in the directory"""
        print("Checking directory for pdf file")
        pdf_files = self.loader.get_pdf_files()


        if not pdf_files:
            print("No PDF files found in the directory")
        else:
            for file_name in pdf_files:
                print(f'Scraping the file {file_name}')
                self.run_single_scraping(file_name)