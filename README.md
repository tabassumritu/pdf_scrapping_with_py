# PDF Scraper and Exporter

This project is a PDF scraping tool built in Python. It allows you to extract content from PDF files, validate the presence of English alphabetic text, and export the results to both JSON and CSV formats. The tool is designed to handle dynamic file processing, where newly added PDF files are automatically detected and processed.

## Features

- **Dynamic Directory Checking**: Continuously monitors a specified directory for new PDFs and processes them without needing a restart.
- **Text Extraction**: Extracts text from each page of the PDF.
- **English Validation**: Validates the presence of English alphabetic characters on each page to flag potential "garbage" or non-English content.
- **Multiple Export Options**: Supports exporting scraped data in both JSON and CSV formats.
- **Scheduling**: Set up regular intervals for scraping with a built-in scheduler.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place PDFs in the Specified Directory:  
   Ensure all PDFs you want to process are in the directory specified in the code (default: `./pdf_directory`).

2. Run the Script:
    ```bash
    python main.py
    ```

    The script will:
    - Check for PDF files in the specified directory.
    - Extract and process content from each PDF.
    - Validate if each page contains English alphabetic text.
    - Export results to JSON and CSV formats.

3. **Exported Data**:  
   JSON and CSV files are saved in the same directory as the script. Each export file is named with the format: `<original_filename>_scrapped_data_<date>.json` or `.csv`.

## Scheduling Options

The script includes a scheduler that runs at regular intervals, checking the directory for new files. You can configure the interval by adjusting the `schedule_task` function in `main.py`.

## Configuration

- **Directory**: Update the directory path in `main.py` where PDF files are stored.
- **Scheduler Interval**: Change the interval for the scheduler in `main.py`.
- **Export Formats**: Customize the export formats (JSON, CSV) in `main.py`.

## Project Structure

- `main.py`: Entry point to start the scraping process and schedule tasks.
- `pdf_loader.py`: Handles loading of PDF files from the specified directory.
- `pdf_scraping_manager.py`: Manages the scraping workflow and coordinates export tasks.
- `task_scheduler.py`: Sets up and manages scheduled scraping tasks.
- `database_handler.py`: Interacts with the SQLite database to track scraped files and store data.
- `export_mixin.py`: Handles exporting data to JSON and CSV formats and includes content validation for English text.
- `requirements.txt`: Lists Python dependencies.

## Example Output

**JSON**
```json
{
  "1": "This is an English text example.",
  "2": "Another page with valid content.",
  "3": "Some special characters @#!",
  "4": "Potential non-English or garbage text here."
}
