class UniqueItem(object):
    '''
    Class that represents the unique item entry. For this project specifically, we will be using (product, year) as
    our unique ID. For example, mortgage,2019 and mortgage,2018 would be considered as separate items due to the year
    difference.
    '''
    def __init__(self, product, year):
        self.product = product
        self.year = year
        self.company_map = {}  # map that stores each company's count for product and year item
        self.total_complaints = 0  # tally the total complaints for product and year item

        # keep track of the max company count to avoid doing a O(n) search algorithm for each item
        self.max_count = 0  # TODO set to -1 ?
        self.max_key = ''

    # update the count for the set of companies for each item
    def update_company_complaint_count(self, company_name):
        if company_name in self.company_map:
            val = self.company_map[company_name]
            val += 1
            self.company_map[company_name] = val
        else:
            self.company_map[company_name] = 1
            val = 1
        if val >= self.max_count:
            self.max_count = val
            self.max_key = company_name
        self.total_complaints += 1

    # GET methods
    def get_product(self):
        return self.product

    def get_year(self):
        return self.year

    def get_total_complaints(self):
        return self.total_complaints

    def get_num_of_companies(self):
        return len(self.company_map)

    def get_highest_percentage(self):
        x = self.max_count / self.total_complaints
        return round(x * 100)
