import csv
import json
from datetime import datetime
from typing import Dict


#method for get current date
def get_current_date():
    """Returns Current date in 'YYYY-MM-DD' format"""
    return datetime.now().strftime("%Y-%m-%d")
#mixin class export as csv, and export as json
class ExportMixin:
    """Mixin for exporting scraped data to json and csv with custom file name"""

    def export_to_csv(self, data:Dict[int,str], original_file_name: str) -> None:
        """Exports scraped data to a csv file with  a custom name"""
        current_date = get_current_date()
        file_name = f"{original_file_name.replace('.pdf', ' ')}_scraped_data_{current_date}.csv"

        with open(file_name, mode = 'w', newline= ' ') as file:
            writer = csv.writer(file)
            writer.writerow(['Page Number', 'Content'])
            for page_num, content in data.items():
                writer.writerow([page_num,content])

        print(f'Data exported to csv:{file_name}')

    def export_to_json(self, data: Dict[int, str], original_file_name: str) -> None:
        """Exports scraped data to a json file with  a custom name"""
        current_date = get_current_date()
        file_name = f"{original_file_name.replace('.pdf', ' ')}_scraped_data_{current_date}.json"

        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent =4)

        print(f'Data exported to json:{file_name}')