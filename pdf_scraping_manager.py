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
        self.loader = PDFLoader(directory)
        print("Pdf Scraping manager initialized")

    def run_single_scraping(self, file_name: str):
        """Scrapes a single pdf file and exports data based on user preferences"""
        db_handler = DatabaseHandler()
        try:
            print(f'Starting Scraping for {file_name}')
            pdf_reader, file_handle = self.loader.load_pdf(file_name)

            # scraping simple scraper for extracting all text
            scraper = SimpleScraper(pdf_reader)
            print(f'Scraping content from {file_name}')
            # perform scraping
            scraped_data = scraper.scrape()

            # check if scraped_data is a string or dictionary
            if isinstance(scraped_data, str):
                # do something
                db_handler.saved_pdf_log_status(file_name, "Success")
                db_handler.saved_scraped_data(file_name, {1: scraped_data})
            elif isinstance(scraped_data, dict):
                db_handler.saved_pdf_log_status(file_name, "Success")
                db_handler.saved_scraped_data(file_name, scraped_data)
            else:
                raise ValueError("Unexpected data format returned by scraper")



            # export to requested formats
            if 'json' in self.export_formats:
                print(f'Exporting {file_name} to JSON format')
                self.export_to_json(scraped_data, file_name)

            # if 'csv' in self.export_formats:
            #     print(f'Exporting {file_name} to csv format')
            #     self.export_to_csv(scraped_data, file_name)
        except Exception as e:
            print(f'An error occurred {e}')
            print(f'Failed to scrape {file_name}. error: {e}')
            db_handler.saved_pdf_log_status(file_name, f'Failed: {str(e)}')
        finally:
            # close the file handle after processing is complete
            file_handle.close()
            db_handler.close_connection()


    def run_all_scraping(self):
        """scrap all pdf files in the directory"""
        print("Checking directory for pdf file")
        pdf_files = self.loader.get_pdf_files()
        db_handler = DatabaseHandler()
        try:
            print('Checking directory for PDF file')
            pdf_files = self.loader.get_pdf_files()
            if not pdf_files:
                print("No PDF files found in the directory")
            else:
                for file_name in pdf_files:
                    if not db_handler.is_pdf_scraped(file_name):
                        print(f'Scraping the file {file_name}....')
                        self.run_single_scraping(file_name)
                    else:
                        print(f"Skipping already scraped file: {file_name}")

        finally:
            db_handler.close_connection()


