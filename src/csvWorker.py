import csv
from datetime import datetime
import os

class CSVWorker(object):
    '''
    Worker that handles the reads and writes of inputs and outputs. It takes in a .csv file and reads the inputs
    that follow the format found here: https://cfpb.github.io/api/ccdb/fields.html
    '''
    def __init__(self):
        pass

    # read the file specified by input_path and let table_manager handle the data updates
    def read_file_and_populate_table(self, input_path, table_manager):
        # before populating the table, check the validity of the headings
        self.check_heading(input_path)

        # begin processing the rows
        print("Processing rows...")
        with open(input_path, mode='r', encoding="utf8") as file:
            csv_reader = csv.DictReader(file)
            # set the headings to lower case
            csv_reader.fieldnames = [name.lower() for name in csv_reader.fieldnames]

            for row in csv_reader:
                if len(row) == len(csv_reader.fieldnames):  # skip rows that don't conform to headings
                    self.process_row(row, table_manager)

    # check if we have necessary headings
    def check_heading(self, input_path):
        print("Checking file at %s" % input_path)
        if os.stat(input_path).st_size == 0:
            print('Error: File is empty.')
            exit(1)
        # check the headings
        with open(input_path, mode='r', encoding="utf8") as file:
            line = file.readline()
            category = set(line.lower().strip().split(','))
            if not category:
                print('Error: Headings are missing.')
                exit(1)
            if not {'product', 'company', 'date received'}.issubset(category):
                print('Error: File is missing one of the headings: Product, Company, Date Received.')
                exit(1)
            return

    # extract the row data and let table_manager update the table
    def process_row(self, row, table_manager):
        try:
            product = row["product"]
            dt = datetime.strptime(row["date received"], '%Y-%m-%d')  # parse date format
            company = row["company"]
        except Exception:
            return
        table_manager.update_table(product.lower(), dt.year, company.lower())

    # write results to output file to specification
    def write_report(self, table_manager, output_path):
        print("Writing report to %s" % output_path)
        with open(output_path, mode='w', encoding="utf8") as file:
            csv_writer = csv.writer(file, delimiter=',', lineterminator='\n')

            for product_key, year_map in table_manager.lookup_table.items():
                for year_key, item in year_map.items():
                    csv_writer.writerow([item.get_product(), item.get_year(), item.get_total_complaints(),
                                         item.get_num_of_companies(), item.get_highest_percentage()])