import argparse
import time
import os
from src.csvWorker import CSVWorker
from src.itemLookupTableManager import ItemLookupTableManager

abs_path = os.path.abspath(os.getcwd())  # path of current working directory

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default=abs_path+'/input/complaints.csv', help='input file path')
parser.add_argument('--output', type=str, default=abs_path+'/output/report.csv', help='output file path')
args = parser.parse_args()

# extract arguments
input_path = args.input
output_path = args.output

# initialize data handler. The table will handle the updating of unique items (i.e. product, year pairs)
table_manager = ItemLookupTableManager()
csv_worker = CSVWorker()  # IO worker to handle reads and writes

csv_worker.read_file_and_populate_table(input_path, table_manager)
csv_worker.write_report(table_manager, output_path)


