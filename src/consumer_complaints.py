import argparse
from src.csvWorker import CSVWorker
from src.itemLookupTable import ItemLookupTable

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='../input/complaints.csv', help='input file path')
parser.add_argument('--output', type=str, default='../output/report.csv', help='output file path')
args = parser.parse_args()

input_path = args.input
output_path = args.output
lookup_table = ItemLookupTable()

csv_worker = CSVWorker()
csv_worker.read_file_and_populate_table(input_path, lookup_table)

lookup_table.sort()

csv_worker.write_report(lookup_table, output_path)

