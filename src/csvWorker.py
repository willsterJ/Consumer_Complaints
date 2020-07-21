import csv
from datetime import datetime


class CSVWorker(object):

    def __init__(self):
        pass

    def read_file_and_populate_table(self, input_path, table):
        with open(input_path, mode='r', encoding="utf8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                self.process_row(row, table)

    def process_row(self, row, table):
        try:
            product = row["Product"]
            dt = datetime.strptime(row["Date received"], '%Y-%m-%d')  # parse date format
            company = row["Company"]
        except Exception:
            return
        table.update_table(product.lower(), dt.year, company.lower())

    def write_report(self, table, output_path):
        with open(output_path, mode='w', encoding="utf8") as file:
            csv_writer = csv.writer(file, delimiter=',', lineterminator='\n')

            for product_key, year_map in table.lookup_table.items():
                for year_key, item in year_map.items():
                    csv_writer.writerow([item.get_product(), item.get_year(), item.get_total_complaints(),
                                         item.get_num_of_companies(), item.get_highest_percentage()])