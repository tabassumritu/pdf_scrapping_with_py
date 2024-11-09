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
        #self.file_handler = FileHandler


    def run_simple_scraping(self, file_name: str):
        """Scrapes a simgle pdf file and exports data based on user preferences"""

        try:
            #Load the pdf
            loader = PDFLoader(self.directory)
            pdf_reader = loader.load_pdf(file_name)

            #scraping simple scraper for extracting all text
            scraper = SimpleScraper(pdf_reader)

            #perform scraping
            scraped_data = scraper.scrape()

            #log success and save to the database
            self.db_handler.saved_scraped_data(file_name, scraped_data)
            self.db_handler.saved_pdf_log_status(file_name, 'Success')

            #export to requested formats
            if 'json' in self.export_formats:
                self.export_to_json(scraped_data, file_name)

            if 'csv' in self.export_formats:
                self.export_to_csv(scraped_data, file_name)


        except Exception as e:
            print(f'An error occured {e}')
            self.db_handler.saved_pdf_log_status(file_name, f'An error occured {e}')