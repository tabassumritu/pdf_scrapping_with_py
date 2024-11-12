import sqlite3
from typing import Dict

"""Handles Database operations for storing scraping logs and data"""


class DatabaseHandler:

    def __init__(self, db_name: str = "scraping_log.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """creates necessary tables for logs and data"""

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pdf_log (
                id INTEGER PRIMARY KEY,
                file_name TEXT,
                status TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scraped_data (
                id INTEGER PRIMARY KEY,
                file_name TEXT,
                page_number INTEGER,
                content TEXT
            )
        """)
        self.connection.commit()

    def saved_pdf_log_status(self, file_name: str, status: str):
        """log status of a pdf scraping operation"""
        self.cursor.execute("INSERT INTO pdf_log(file_name, status) VALUES(?,?)", (file_name, status))
        self.connection.commit()

    def update_pdf_status(self, file_name: str, status: str):
        """Update the status of a pdf in the log."""
        print(f"Uploading status for {file_name}: {status}")
        self.cursor.execute("UPDATE pdf_log SET status = ? WHERE file_name = ?", (status, file_name))
        self.connection.commit()


    def is_pdf_scraped(self, file_name: str):
        """Checking if a pdf file has been already scraped"""
        self.cursor.execute("SELECT 1 FROM pdf_log Where file_name = ? LIMIT 1", (file_name,))
        result = self.cursor.fetchone() is not None
        print(f"{file_name} scraped status: {'Already scraped' if result else 'Not Scraped yet'}")
        return result

    def saved_scraped_data(self, file_name: str, data: Dict[int, str]):
        """saves scraped data to the database"""
        for page_num, content in data.items():
            self.cursor.execute("INSERT INTO scraped_data (file_name, page_number, content) VALUES(?,?,?)",
                                (file_name, page_num, content)
                                )

        self.connection.commit()

    def close_connection(self):
        """close connection of the database"""
        self.connection.close()
