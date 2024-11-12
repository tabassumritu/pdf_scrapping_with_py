from pdf_scraping_manager import PDFScrapingManager
from task_scheduler import TaskScheduler
from scrap_mode import ScrapeMode

if __name__ == '__main__':
    directory = './pdf_directory'
    mode = ScrapeMode.ALL_TEXT
    export_format = ['json', 'csv']

    # initialize the manager with user-specified format
    print('initialize PDF Scraping manager and scheduler')
    scraping_manager = PDFScrapingManager(directory, mode, export_format)
    schedular = TaskScheduler(scraping_manager)

    schedular.schedule_task(5, 'seconds')