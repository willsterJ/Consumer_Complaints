import collections
from src.uniqueItem import UniqueItem


class ItemLookupTableManager(object):
    '''
    Data Structure Class that implements the table lookup. It handles the mapping between Key=product to another mapping
    that maps Key=year to a unique item
    '''

    def __init__(self):
        self.lookup_table = {}

    # Update table entry that holds reference to unique item
    def update_table(self, product, year, company):
        item = self.fetch_item(product, year)
        item.update_company_complaint_count(company)

    # Fetches item from table. Hops through map layers to arrive at item entry
    def fetch_item(self, product, year):
        if product not in self.lookup_table:  # for newly discovered product, we create new map
            self.lookup_table[product] = {}

        if year not in self.lookup_table[product]:  # we generate a new unique item and assign it to table
            item = UniqueItem(product, year)
            self.lookup_table[product][year] = item
            return item

        return self.lookup_table[product][year]

    # sort the table by order of product followed by year
    def sort_table(self):
        # First sort table by product name
        ordered_dict = collections.OrderedDict(sorted(self.lookup_table.items()))
        # Then for each table[product], sort by year
        for key_year in ordered_dict:
            ordered_dict[key_year] = collections.OrderedDict(sorted((ordered_dict[key_year].items())))

        self.lookup_table = ordered_dict

