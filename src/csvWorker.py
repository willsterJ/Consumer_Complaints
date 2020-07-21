import csv
from datetime import datetime


class CSVWorker(object):
    '''
    Worker that handles the reads and writes of inputs and outputs. It takes in a .csv file and reads the inputs
    that follow the format found here: https://cfpb.github.io/api/ccdb/fields.html
    '''
    def __init__(self):
        pass

    # read the file specified by input_path and let table_manager handle the data updates
    def read_file_and_populate_table(self, input_path, table_manager):
        with open(input_path, mode='r', encoding="utf8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                self.process_row(row, table_manager)

    # extract the row data and let table_manager update the table
    def process_row(self, row, table_manager):
        try:
            product = row["Product"]
            dt = datetime.strptime(row["Date received"], '%Y-%m-%d')  # parse date format
            company = row["Company"]
        except Exception:
            return
        table_manager.update_table(product.lower(), dt.year, company.lower())

    # write results to output file to specification
    def write_report(self, table_manager, output_path):
        with open(output_path, mode='w', encoding="utf8") as file:
            csv_writer = csv.writer(file, delimiter=',', lineterminator='\n')

            for product_key, year_map in table_manager.lookup_table.items():
                for year_key, item in year_map.items():
                    csv_writer.writerow([item.get_product(), item.get_year(), item.get_total_complaints(),
                                         item.get_num_of_companies(), item.get_highest_percentage()])